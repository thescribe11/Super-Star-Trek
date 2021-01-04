# stdlib imports
import math
import random
import re
from typing import Final, Union

# user-defined modules.
from Enterprise import Enterprise
import classes
from classes import CommandKind
import displays  # I should probably find a way to fold this into SST.py, but it's too much work.

# The date of the Treaty of Algeron.
# It forbids the Federation from using cloaking devices, so the Romulans
# will get annoyed if they catch the Enterprise using the one it stole from them.
ALGERON: Final = 2311.0
HITME: bool = False  # Controls if the Romulans are antagonistic

UPCOMING_EVENTS = classes.Upcoming()

# Controls whether debug features like print_debug() are active.
DEBUG = True
TESTING_MOVEMENT = True

ent = Enterprise()


# Regular Expressions for use in parsing commands:
NUMBER = re.compile(r'\d*[.]?\d*')
WORD = re.compile(r'[a-zA-Z]+')


def calcvector(direction):
    # Work out the direction increment vector
    # hinc = horizontal increment
    # vinc = vertical increment
    if 3 < direction < 7:
        hinc = -1
    elif direction < 3 or direction > 7:
        hinc = 1
    else:
        hinc = 0
    if 5 > direction > 1:
        vinc = -1
    elif direction > 5:
        vinc = 1
    else:
        vinc = 0
    return hinc, vinc


def photons(self: Enterprise):
    if self.torpedoes == 0:
        print("[*ARMORY*] I'm afraid that we are out of torpedoes, sir.")
        return

    if type(UPCOMING_EVENTS.scan()) != float:
        try:
            fire_number = int(
                input("[*ARMORY*] How many torpedoes would you like to fire?\n> ")
            )
        except ValueError:
            print(
                "\n[*ARMORY*] Sir, can you please speak more clearly? I cannot understand what you just said."
            )
            return
    else:
        fire_number = int(UPCOMING_EVENTS.get())
    print(fire_number)
    if 3 < fire_number < self.torpedoes:
        if type(UPCOMING_EVENTS.scan()) == classes.Decision:
            fire_anyway = UPCOMING_EVENTS.get().which
        else:
            print("\n[*ARMORY*] Captain, firing that many would melt the tubes!")
            fire_anyway = input(
                "\nWould you like to fire anyway? (WARNING: Doing so will incur damage)\n> "
            )

        if fire_anyway.upper() in {'Y', 'YES'}:
            launch_torps(self, fire_number)
            for i in range(fire_number):
                self.damage["Photon Torpedoes"] += random.choice([0.1, 0.2, 0.3])

    elif fire_number > self.torpedoes:
        print(
            "\n[*ARMORY*] What do you think we are, the Bank of Ferenginar?! We don't HAVE that many torpedoes!"
        )

    else:
        launch_torps(self, fire_number)
    UPCOMING_EVENTS.add(classes.KlingonsRespond)


def launch_torps(self: Enterprise, to_fire: int):
    if to_fire > self.torpedoes:
        print(
            "[*ARMORY*] What do you think we are, the Bank of Ferenginar?! We don't even HAVE that many torepdoes!"
        )
        return

    queue: list = []
    for i in range(1, to_fire + 1):
        x = input(f"Input the target direction for torpedo #{i}\n> ")
        _placeholder = x.split(" ")
        queue.append(int(x))

    current_torp = 0

    for direction in queue:
        current_torp += 1
        print(f"\n* Torpedo #{current_torp}\nTorpedo track:")
        if 1 <= direction <= 9:
            # Work out the horizontal and vertical co-ordinates
            # of the Enterprise in the current sector
            # 0,0 is top left and 9,9 is bottom right
            horiz = self.shoriz
            vert = self.svert
            # And calculate the direction to fire the torpedo
            hinc, vinc = calcvector(direction)
            # A torpedo only works in the current sector and stops moving
            # when we hit something solid
            out = False
            while not out:
                print(f"({vert + 1},{horiz + 1}) ", end="")
                # Calculate the movement vector
                vert = vert + vinc
                horiz = horiz + hinc

                # Is the torpedo still in the sector?
                if vert < 0 or vert > 9 or horiz < 0 or horiz > 9:
                    print("\nTorpedo missed.\n")
                    break
                elif self.sector[vert][horiz] != ".":
                    out = True
                # Have we hit an object?
                if self.sector[vert][horiz] == "K":
                    # Hit and destroyed a Klingon!
                    out = True
                    self.sector[vert][horiz] = "."
                    for i in self.local_klingons_list:
                        if i.y == vert and i.x == horiz:
                            self.local_klingons_list.remove(i)
                    self.galaxy[self.gvert][self.ghoriz][0] -= 1
                    self.klingons -= 1
                    print(f"\n***Klingon at sector ({vert}, {horiz}) destroyed.")
                elif self.sector[vert][horiz] == "B":
                    # Destroying a starbase ends the game.
                    out = True
                    self.sector[vert][horiz] = "."
                    self.alive = False
                    displays.type_slow(
                        f"\n\n*** Starbase at ({vert}, {horiz}) destroyed. ***\n\nYou monster.\n"
                    )
                elif self.sector[vert][horiz] == "+":
                    # Shooting a torpedo into a star has no effect... usually.
                    out = True
                    if random.randint(0, 7) < 7:
                        print("\nTorpedo impacts star... no effect.")
                    else:
                        print("\nTorpedo impacts star... the star explodes.")
                        self.galaxy[self.gvert][self.ghoriz][2] -= 1
                        self.sector[vert][horiz] = "."
                        for i in self.local_klingons_list:
                            if [i.y, i.x] in [
                                [vert - 1, horiz - 1],
                                [vert - 1, horiz],
                                [vert - 1, horiz + 1],
                                [vert, horiz - 1],
                                [vert, horiz],
                                [vert, horiz + 1],
                                [vert + 1, horiz - 1],
                                [vert + 1, horiz],
                                [vert + 1, horiz + 1],
                            ]:
                                print(
                                    f"***Klingon at sector ({i.y}, {i.x}) destroyed in the explosion."
                                )
                                self.local_klingons_list.remove(i)
                                self.galaxy[self.gvert][self.ghoriz][0] -= 1
                                self.klingons -= 1
                        if [self.svert, self.shoriz] in [
                            [vert - 1, horiz - 1],
                            [vert - 1, horiz],
                            [vert - 1, horiz + 1],
                            [vert, horiz - 1],
                            [vert, horiz],
                            [vert, horiz + 1],
                            [vert + 1, horiz - 1],
                            [vert + 1, horiz],
                            [vert + 1, horiz + 1],
                        ]:
                            print(
                                "\nThe Enterprise is caught in the shockwave",
                                end="",
                            )
                            if self.shield_stat:
                                damage_amount = random.randint(500, 700)
                                if damage_amount < self.shields:
                                    print(
                                        ", dealing %i damage to the shields."
                                        % damage_amount
                                    )
                                    self.shields -= damage_amount
                                else:
                                    print(
                                        ". The blast overwhelms the shields, disabling the shield generator."
                                    )
                                    self.damage["Shields"] += random.randint(5, 30) / 10
                                    self.add_collision_damage(1)
                            else:
                                print(", which causes massive damage.")
                                self.add_collision_damage(3)

            # One fewer torpedo
            self.torpedoes -= 1


def change_shields(self):
    """
    Add/subtract energy from the shields.
    """

    try:
        amount = input(
            "\n[*SHIELD CONTROL*] How much energy would you like to transfer? (negative values return energy to "
            "main capacitors)\n> "
        )
    except ValueError:
        print("[*SHIELD CONTROL*] Sir, that is not a valid amount.")

    # TODO Add energy amount changing.


def warp_move(self: Enterprise) -> bool:
    """
    Move within quadrant.
    If True is returned, the Enterprise moved;
    otherwise, the maneuver was cancelled.

    Args:
        self (Enterprise):
    """

    blooey = False
    damaged = False
    trip_time: float = 0
    sdistance: float = 0
    sslope: float = 0

    if self.damage["Warp Drive"] > 5:
        print(
            "[*ENGINEERING*] Scotty here. The warp drive is badly damaged, sir; we'd better not use it until I "
            "can get this damage repaired. "
        )
        return False
    elif 0 < self.damage["Impulse Drive"] < 5 and self.warp_speed > 4:
        print(
            "[*ENGINEERING*] Sir, the impulse drive is damaged; I can only give you warp 4 until it is repaired."
        )

    which = input("[*Lt. SULU*] Automatic or manual movement?\n> ")
    try:
        if which[0] == "a" or which[0] == "A":
            automatic = True
        elif which[0] == "m" or which[0] == "M":
            automatic = False
        else:
            print("[*Lt. SULU*] Sir? That doesn't make sense.")
            return False
    except IndexError:
        print("[*Lt. SULU*] Aborting manuever.")
        return False

    if automatic:
        # noinspection PyPep8,PyPep8,PyPep8
        try:
            destination: list = [
                int(i) - 1
                for i in input("Please input destination coordinates\n> ").split(
                    " "
                )
            ]
        except:  # Yes, the bare except is on purpose.
            print("[*COMPUTER*] *ERROR* COORDINATES INVALID.")
            return False
        if len(destination) == 2:
            for i in destination:
                if not -1 < i < 10:
                    print("[*COMPUTER*] *ERROR* COORDINATES INVALID.")
                    return False
            # dsvert = destination's vertical coord, dshoriz = destination's horizontal coord
            dsvert = int(destination[0])
            dshoriz = int(destination[1])
            svert_diff = dsvert - self.svert
            shoriz_diff = dshoriz - self.shoriz
            if svert_diff != 0:
                sslope = (self.shoriz - dshoriz) / (self.svert - dsvert)
                sdistance = math.sqrt(svert_diff ** 2 + shoriz_diff ** 2)
            else:
                sslope = math.inf
                sdistance = shoriz_diff

            trip_time = 10 * sdistance / 5
            power = (sdistance + 0.05) * 15 * (2 if self.shield_stat else 1)
            if power >= self.energy:
                print(
                    "[*ENGINEERING*] Scotty here. I'm sorry captain, but we canna' do it!\n[*ENGINEERING*] We "
                    "simply don't have enough power remaining. "
                )
                return False

        else:
            print("[*COMPUTER*] *ERROR* COORDINATES INVALID.")

    else:
        deltas: list = input("Vertical and Horizontal displacements\n> ").split(" ")
        # Any way to get it down to one number conversion here would be welcome!
        svert_diff = int(float(deltas[0]) * 10)
        shoriz_diff = int(float(deltas[1]) * 10)
        if svert_diff != 0:
            sslope = shoriz_diff / svert_diff
            sdistance = math.sqrt(svert_diff ** 2 + shoriz_diff ** 2)
        else:
            sslope = math.inf
            sdistance = shoriz_diff

        trip_time = sdistance / 15
        power = (sdistance + 0.05) * 15 * (2 if self.shield_stat else 1)
        if power >= self.energy:
            print(
                "[*ENGINEERING*] Scotty here. I'm sorry captain, but we canna' do it!\n[*ENGINEERING*] We simply "
                "don't have enough power remaining. "
            )

    print_debug(f"{sslope=}")

    impulse_move(self, sslope, svert_diff, shoriz_diff)
    self.energy -= power
    self.time_remaining -= trip_time
    return True


def impulse_move(self: Enterprise, unprocessed_slope, svert_diff, shoriz_diff):
    """
    Intra-quadrant movemement
    """
    if not DEBUG:
        self.sector[self.svert][self.shoriz] = "."

    # In other words, +slope if the Enterprise is moving vertically, otherwise -slope.
    slope = (unprocessed_slope * (1 if svert_diff > 0 else -1))

    def reset_leaving():
        for i in leaving:
            leaving[i] = False

    direction = 1 if svert_diff > 0 else -1

    old_svert: int = self.svert
    old_shoriz: int = self.shoriz
    old_gvert: int = self.gvert
    old_ghoriz: int = self.ghoriz

    new_svert: int
    new_shoriz: int

    if not math.isinf(slope):  # Old code: "abs(slope) != math.inf". Which is better?
        leaving: dict = {'north': False, 'south': False, 'east': False, 'west': False}

        for i in range(abs(svert_diff)):
            new_svert = old_svert + direction
            new_shoriz = old_shoriz + slope
            print(
                f'Iteration #{i}: {new_svert=}, {new_shoriz=}. *Current* galactic position: {old_gvert=}, {old_ghoriz=}'
            )

            if new_svert < 0:
                # Out of quadrant (v-)
                print_debug("Leaving quadrant (-v)")
                leaving['north'] = True

            elif new_svert > 9:
                # Out of quadrant (v+)
                print_debug("Leaving quadrant (+v)")
                leaving['south'] = True

            if new_shoriz < 0:
                # Out of quadrant (h-)
                print_debug("Leaving quadrant (-h)")
                leaving['west'] = True

            elif new_shoriz > 9:
                # Out of quadrant (h+)
                print_debug("Leaving quadrant (+h)")
                leaving['east'] = True

            if True in leaving.values():
                print(f'{leaving=}')

                new_gvert = old_gvert
                new_ghoriz = old_ghoriz

                if leaving['north']:
                    new_gvert = old_gvert - 1
                elif leaving['south']:
                    new_gvert = old_gvert + 1
                if leaving['east']:
                    new_ghoriz = old_ghoriz + 1
                if leaving['west']:
                    new_ghoriz = old_ghoriz - 1

                if not self.enter_quadrant(new_gvert, new_ghoriz):
                    # Unfortunately, the Enterprise wasn't able to leave the quadrant. As a result, get sector
                    # coordinates back within normal values.
                    print("*Enterprise failed to leave quadrant")

                    if leaving['north'] or leaving['south']:
                        new_svert = old_svert

                    if leaving['west'] or leaving['east']:
                        new_shoriz = old_shoriz
                    break
                else:
                    # The Enterprise has left the quadrant, and is now going on its merry way.
                    print("*Enterprise has left the quadrant")

                    if leaving['north']:
                        new_svert = 9
                    elif leaving['south']:
                        new_svert = 0

                    if leaving['west']:
                        new_shoriz = new_shoriz + 10
                    elif leaving['east']:
                        new_shoriz = new_shoriz - 10

                    self.gvert = new_gvert
                    self.ghoriz = new_ghoriz
                    old_gvert = new_gvert
                    old_ghoriz = new_ghoriz

                    reset_leaving()

            else:
                x = self.check_movement_collision(new_svert, new_shoriz, old_shoriz)
                print(f"{x=}")
                if x[0]:
                    old_shoriz = x[1]
                    break
            old_svert = new_svert
            old_shoriz = new_shoriz

    else:
        # Horizontal movement

        direction: int = 1 if shoriz_diff > 0 else -1
        leaving: dict = dict(east=False, west=False)
        new_ghoriz: int = self.ghoriz
        killer: bool = False

        for i in range(abs(shoriz_diff)):
            new_shoriz = old_shoriz + direction

            print(f"*Iteration {i}: {new_shoriz=} {new_ghoriz=}")

            if new_shoriz >= 10:
                leaving['east'] = True
                print("Leaving east!")
                new_ghoriz = old_ghoriz + 1
            elif new_shoriz < 0:
                print("Leaving west!")
                leaving['west'] = True
                new_ghoriz = old_ghoriz - 1

            if True in leaving.values():
                if not self.enter_quadrant(self.ghoriz, new_ghoriz):
                    new_svert = old_svert
                    killer = True
                    print("**Enterprise failed to leave the quadrant!")
                else:
                    print("*Enterprise has left the quadrant")

                    if leaving['east']:
                        new_shoriz = 0
                    elif leaving['west']:
                        new_shoriz = 9
                    reset_leaving()

                    self.ghoriz = new_ghoriz
                    old_ghoriz = new_ghoriz
            else:
                x = self.check_h_movement_collision(new_shoriz, old_shoriz)
                if x[0]:
                    print(f"{x[1]=}")
                    old_shoriz = x[1]
                    killer = True

            if killer:
                # For some reason, the Enterprise has to abort the trip.
                break
            old_shoriz = new_shoriz

    self.svert = old_svert
    self.shoriz = round(old_shoriz)
    self.sector[self.svert][self.shoriz] = "E"


def find_kind(token) -> Union[classes.CommandKind, classes.Decision]:
    try:
        if token.startswith('sh'):
            return CommandKind.Shield
        elif token.startswith('sr'):
            return CommandKind.Srscan
        elif token.startswith('lr'):
            return CommandKind.Lrscan
        elif token.startswith('t'):
            return CommandKind.Torpedo
        elif token.startswith('p'):
            return CommandKind.Phaser
        elif token.startswith('m'):
            return CommandKind.Move
        elif token.startswith('r'):
            return CommandKind.Rest
        elif token == 'deathray':
            return CommandKind.ImprobGun
        elif token == 'destruct':
            return CommandKind.SelfDestruct
        elif token.startswith('d'):
            return CommandKind.Damage
        elif token.startswith('sc'):
            return CommandKind.Score
        elif token.startswith('c'):
            return CommandKind.Chart
        elif token.startswith('y'):
            return classes.Decision('Y')
        elif token.startswith('n'):
            return classes.Decision('N')
        else:
            return CommandKind.Error

    except IndexError:
        return CommandKind.Error


def raise_shields() -> None:
    if ent.damage["Shields"] == 0:
        print("[*SHIELD CONTROL*] Raising shields.\n")
        ent.shield_stat = True
    else:
        print(
            '[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings '
            'until it is repaired.\n '
        )


def process_command(raw: str) -> None:
    tokens = raw.lower().split(' ')
    index = 0
    while index < len(tokens):
        token = tokens[index]
        if re.fullmatch(WORD, token):
            UPCOMING_EVENTS.add(find_kind(token))
        elif re.fullmatch(NUMBER, token):
            UPCOMING_EVENTS.add(float(token))
        index += 1


def main():
    global ent
    while ent.alive:
        print()
        raw_commands = input("Command > ")
        process_command(raw_commands)
        command = UPCOMING_EVENTS.get()
        print()
        if command == "srs" or command == "srscan":
            if not ent.sector_current:
                (
                    ent.sector,
                    ent.local_klingons_list,
                    ent.panic,
                ) = displays.enter_quadrant(
                    ent.galaxy[ent.gvert][ent.ghoriz],
                    ent.ghoriz,
                    ent.gvert,
                    ent.svert,
                    ent.shoriz,
                    ent.energy,
                )  # This is the closest I could get to being PEP8-compliant.
                ent.sector_current = True
            if ent.damage["Short-Range Sensors"] == 0:
                displays.print_srscan(
                    ent.sector,
                    [[ent.ghoriz, ent.gvert], [ent.shoriz, ent.svert]],
                    ent.panic,
                    ent.torpedoes,
                    ent.energy,
                    ent.klingons,
                    ent.shields,
                    ent.shield_stat,
                    ent.warp_speed,
                    ("ACTIVE" if ent.damage["Life Support"] == 0 else "DAMAGED"),
                    ent.environment_reserves,
                    ent.date,
                    ent.time_remaining,
                )
            else:
                displays.print_d_srscan(
                    ent.sector,
                    ent.gvert,
                    ent.gvert,
                    ent.shoriz,
                    ent.svert,
                    ent.panic,
                    ent.torpedoes,
                    ent.energy,
                    ent.klingons,
                    ent.shields,
                    ent.shield_stat,
                    ent.warp_speed,
                    ("ACTIVE" if ent.damage["Life Support"] == 0 else "DAMAGED"),
                    ent.environment_reserves,
                    ent.date,
                    ent.time_remaining,
                )

        elif command[0] == "p" or command[0] == "P":
            if ent.damage["Photon Torpedoes"] == 0:
                photons(ent)
            else:
                print("[*ARMORY*] Sir, the launching systems are inoperable.")

        elif command[0] == "d" or command[0] == "D":
            displays.print_damage(ent.damage)

        elif (
                command == "shields up"
                or command == "s up"
                or command == "s u"
                or command == "shields u"
        ):
            if ent.damage["Shields"] == 0:
                print("[*SHIELD CONTROL*] Raising shields.\n")
                ent.shield_stat = True
            else:
                print(
                    '[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings '
                    'until it is repaired.\n '
                )
            ent.klingons_attack()

        elif (
                command == "shields down"
                or command == "s down"
                or command == "s d"
                or command == "shields d"
        ):
            if ent.damage["Shields"] == 0:
                print("[*SHIELD CONTROL*] Lowering shields.\n")
                ent.shield_stat = False
            else:
                print(
                    "[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings"
                    " until it is repaired.\n "
                )
            ent.klingons_attack()

        elif command[0] == "S" or command[0] == "s":
            if ent.damage["Shields"] != 0:
                print(
                    "[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings "
                    "until it is repaired.\n "
                )
            else:
                print("[*SHIELD CONTROL*] What do you want me to do?")
                subcommand = input(
                    "(1 - raise shields, 2 - lower shields, 3 - add/subtract energy\n> "
                )
                if subcommand == "1":
                    print("[*SHIELD CONTROL*] Raising shields.\n")
                    ent.shield_stat = True
                elif subcommand == "2":
                    print("[*SHIELD CONTROL*] Lowering shields.\n")
                    ent.shield_stat = False
                elif subcommand == "3":
                    change_shields(ent)
                else:
                    print(
                        "[*SHIELD CONTROL*] Sir, that command does not make sense."
                    )
            ent.klingons_attack()

        elif command[0] == "m" or command[0] == "M":
            if warp_move(ent):
                ent.klingons_attack()

        elif command[0] == "c" or command[0] == "C":
            displays.print_starchart(
                ent.galaxy,
                ent.quadrants_visited,
                ent.gvert,
                ent.ghoriz,
                (True if ent.damage["Long-Range Sensors"] > 0 else False),
            )

        elif command in ("LRS", "LRSCAN", "lrs", "lrscan"):
            displays.print_lrscan(
                ent.galaxy,
                ent.gvert,
                ent.ghoriz,
                (True if ent.damage["Long-Range Sensors"] > 0 else False),
            )

        elif command in ("QUIT", "quit", "Quit"):
            quit()


def print_debug(string) -> None:
    if DEBUG:
        print(string)


if __name__ == "__main__":
    main()
