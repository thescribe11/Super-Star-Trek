# stdlib imports
import math
import random
from typing import Final

# user-defined modules.
import displays  # I should probably find a way to fold this into SST.py, but it's too much work.

## The date of the Treaty of Algeron.
## It forbids the Federation from using cloaking devices, so the Romulans
## will get annoyed if they catch the Enterprise using the one it stole from them.
ALGERON: Final = 2311.0
IDIDIT: bool = False  # Controls if the Romulans are antagonistic

class Upcoming:
    '''
    Buffer for user input.
    '''

    def __init__(self, *args, **kwargs):
        self.upcoming_input = []

    def get(self) -> str or None:
        '''
        Return the top element in the event stack
        '''
        try:
            return self.upcoming_input.pop()
        except IndexError:
            return None

    def add(self, incoming):
        '''
        Add an element to the stack
        '''
        assert isinstance(incoming, str)
        self.upcoming_input.append(incoming)


UPCOMING_EVENTS: dict = []


## Controls whether debug features like print_debug() are active.
DEBUG = True
TESTING_MOVEMENT = True

## Unfortunately, Python doesn't have a convenient way to make float ranges.
## As a result, my only choices were (a) put it here, or (b) initialize it
## every time I use it. The latter is inefficient, so I just decided to
## make a global variable.
POSSIBLE_DAMAGES = [i / 10 for i in range(50, 79)]


def print_debug(string) -> None:
    if DEBUG:
        print(string)


class Enterprise(object):
    def __init__(self):
        super().__init__()
        self.leave_attempts = 0
        self.energy = 3000
        self.shield_stat = False
        self.shields = 1500
        self.torpedoes = 8
        self.crystals = 0  # I may or may not keep this
        self.gvert, self.ghoriz, self.svert, self.shoriz = (
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
        )
        self.klingons = 0
        self.warp_speed = 5
        self.environment_reserves = 100.0
        self.docked = False
        self.date = 100.0 * (int)(31.0 * random.random() + 20.0)
        self.time_remaining = random.randint(8, 15)
        self.cloaked = False

        global_klingons = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        global_starbases = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        global_stars = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        self.galaxy = [
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
        ]
        self.sector = [
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
        ]
        self.quadrants_visited = [  # Used by the LRS system to determine if the Enterprise has vistied a quadrant.
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, False, False, False],
        ]

        self.damage = {
            "Shields": 0,
            "Phasers": 0,
            "Photon Torpedoes": 0,
            "Warp Drive": 0,
            "Impulse Drive": 0,
            "Communications": 0,
            "Short-Range Sensors": 0,
            "Long-Range Sensors": 0,
            "Life Support": 0,
        }

        if not DEBUG:
            for i in range(10):
                for j in range(10):
                    to_add = random.randint(0, 6)
                    if to_add == 5:
                        to_add = 0
                    global_klingons[j][i] = to_add
                    self.klingons += to_add
                    global_stars[j][i] = random.randint(0, 9)

            for i in range(0, random.randint(3, 6)):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                global_starbases[y][x] = 1

            for i in range(10):
                for j in range(10):
                    self.galaxy[j][i][0] = global_klingons[j][i]
                    self.galaxy[j][i][1] = global_starbases[j][i]
                    self.galaxy[j][i][2] = global_stars[j][i]

            self.password = (
                displays.beginning_spiel()
            )  # The password is used for authenticating things like abandoning ship.
            self.sector_current = False

            self.local_klingons_list = []

            self.alive = True
            while self.alive:
                print()
                command = input("Command > ")
                print()
                if command == "srs" or command == "srscan":
                    if not self.sector_current:
                        (
                            self.sector,
                            self.local_klingons_list,
                            self.panic,
                        ) = displays.enter_quadrant(
                            self.galaxy[self.gvert][self.ghoriz],
                            self.ghoriz,
                            self.gvert,
                            self.svert,
                            self.shoriz,
                            self.energy,
                        )  # This is the closest I could get to being PEP8-compliant.
                        self.sector_current = True
                    if self.damage["Short-Range Sensors"] == 0:
                        displays.print_srscan(
                            self.sector,
                            [[self.ghoriz, self.gvert], [self.shoriz, self.svert]],
                            self.panic,
                            self.torpedoes,
                            self.energy,
                            self.klingons,
                            self.shields,
                            self.shield_stat,
                            self.warp_speed,
                            ("ACTIVE" if self.damage["Life Support"] == 0 else "DAMAGED"),
                            self.environment_reserves,
                            self.date,
                            self.time_remaining,
                        )
                    else:
                        displays.print_d_srscan(
                            self.sector,
                            self.gvert,
                            self.gvert,
                            self.shoriz,
                            self.svert,
                            self.panic,
                            self.torpedoes,
                            self.energy,
                            self.klingons,
                            self.shields,
                            self.shield_stat,
                            self.warp_speed,
                            ("ACTIVE" if self.damage["Life Support"] == 0 else "DAMAGED"),
                            self.environment_reserves,
                            self.date,
                            self.time_remaining,
                        )

                elif command[0] == "p" or command[0] == "P":
                    if self.damage["Photon Torpedoes"] == 0:
                        self.photons()
                    else:
                        print("[*ARMORY*] Sir, the launching systems are inoperable.")

                elif command[0] == "d" or command[0] == "D":
                    displays.print_damage(self.damage)

                elif (
                        command == "shields up"
                        or command == "s up"
                        or command == "s u"
                        or command == "shields u"
                ):
                    if self.damage["Shields"] == 0:
                        print("[*SHIELD CONTROL*] Raising shields.\n")
                        self.shield_stat = True
                    else:
                        print(
                            "[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings until it "
                            "is repaired.\n "
                        )
                    self.klingons_attack()

                elif (
                        command == "shields down"
                        or command == "s down"
                        or command == "s d"
                        or command == "shields d"
                ):
                    if self.damage["Shields"] == 0:
                        print("[*SHIELD CONTROL*] Lowering shields.\n")
                        self.shield_stat = False
                    else:
                        print(
                            "[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings until it "
                            "is repaired.\n "
                        )
                    self.klingons_attack()

                elif command[0] == "S" or command[0] == "s":
                    if self.damage["Shields"] != 0:
                        print(
                            "[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings until it "
                            "is repaired.\n "
                        )
                    else:
                        print("[*SHIELD CONTROL*] What do you want me to do?")
                        subcommand = input(
                            "(1 - raise shields, 2 - lower shields, 3 - add/subtract energy\n> "
                        )
                        if subcommand == "1":
                            print("[*SHIELD CONTROL*] Raising shields.\n")
                            self.shield_stat = True
                        elif subcommand == "2":
                            print("[*SHIELD CONTROL*] Lowering shields.\n")
                            self.shield_stat = False
                        elif subcommand == "3":
                            self.change_shields()
                        else:
                            print(
                                "[*SHIELD CONTROL*] Sir, that command does not make sense."
                            )
                    self.klingons_attack()

                elif command[0] == "m" or command[0] == "M":
                    if self.warp_move():
                        self.klingons_attack()

                elif command[0] == "c" or command[0] == "C":
                    displays.print_starchart(
                        self.galaxy,
                        self.quadrants_visited,
                        self.gvert,
                        self.ghoriz,
                        (True if self.damage["Long-Range Sensors"] > 0 else False),
                    )

                elif command in ("LRS", "LRSCAN", "lrs", "lrscan"):
                    displays.print_lrscan(
                        self.galaxy,
                        self.gvert,
                        self.ghoriz,
                        (True if self.damage["Long-Range Sensors"] > 0 else False),
                    )

                elif command in ("QUIT", "quit", "Quit"):
                    quit()

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

        ## TODO Add energy amount changing.

    def warp_move(self) -> bool:
        """
        Move within quadrant.
        If True is returned, the Enterprise moved;
        otherwise, the maneuver was cancelled.
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
            try:
                destination: list = [
                    int(i) - 1
                    for i in input("Please input destination coordinates\n> ").split(
                        " "
                    )
                ]
            except:
                print("[*COMPUTER*] *ERROR* COORDINATES INVALID.")
                return False
            if len(destination) == 2:
                for i in destination:
                    if not -1 < i < 10:
                        print("[*COMPUTER*] *ERROR* COORDINATES INVALID.")
                        return False
                ## dsvert = destination's vertical coord, dshoriz = destination's horizontal coord
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
                power = (sdistance + 0.05) * 15 * (2 if self.shield_stat == True else 1)
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
            ## Any way to get it down to one number conversion here would be welcome!
            svert_diff = int(float(deltas[0]) * 10)
            shoriz_diff = int(float(deltas[1]) * 10)
            if svert_diff != 0:
                sslope = shoriz_diff / svert_diff
                sdistance = math.sqrt(svert_diff ** 2 + shoriz_diff ** 2)
            else:
                sslope = math.inf
                sdistance = shoriz_diff

            trip_time = sdistance / 15
            power = (sdistance + 0.05) * 15 * (2 if self.shield_stat == True else 1)
            if power >= self.energy:
                print(
                    "[*ENGINEERING*] Scotty here. I'm sorry captain, but we canna' do it!\n[*ENGINEERING*] We simply "
                    "don't have enough power remaining. "
                )

        print_debug(f"{sslope=}")

        self.impulse_move(sslope, svert_diff, shoriz_diff)
        self.energy -= power
        self.time_remaining -= trip_time
        return True

    def impulse_move(self, unprocessed_slope, svert_diff, shoriz_diff):
        """
        Intra-quadrant movement
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
                    f'Iteration #{i}: {new_svert=}, {new_shoriz=}. *Current* galactic position: {old_gvert=}, {old_ghoriz=}')

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
                        ## Unfortunately, the Enterprise wasn't able to leave the quadrant. As a result, get sector
                        ## coordinates back within normal values.
                        print("*Enterprise failed to leave quadrant")

                        if leaving['north'] or leaving['south']:
                            new_svert = old_svert

                        if leaving['west'] or leaving['east']:
                            new_shoriz = old_shoriz
                        break
                    else:
                        ## The Enterprise has left the quadrant, and is now going on its merry way.
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
                    if x[0]:
                        old_shoriz = x[1]
                        break
                old_svert = new_svert
                old_shoriz = new_shoriz

        else:
            ## Horizontal movement

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

    def check_movement_collision(self, new_vert: int, new_horiz: float, old_horiz: float) -> (bool, float):
        """
        Check to see if the Enterprise has crashed into anything while moving.

        TODO: Add logic.
        """

        int_new_horiz: int = math.floor(new_horiz)
        print_debug(self.sector[new_vert][int_new_horiz])

        return False, 0

    def check_h_movement_collision(self, new_horiz, old_horiz) -> (bool, int):
        """
        Check to see if the Enterprise has crashed into anything while moving.

        This is a horizontal variant of check_movement_collision().

        TODO: Add logic.
        """
        return False, new_horiz  # For now, just returning an "OK" response.

    def emergency_stop(self, vert, horiz):
        """
        Performs emergency stopping maneuvers.
        """
        print(
            "\n***WARNING*** Object detected at sector (%i, %.0f);\nEmergency stop requires %i units of energy."
            % (vert, horiz, (to_sub := random.randint(110, 130)))
        )
        self.energy -= to_sub

    def add_quadrant_to_chart(self):
        """
        Adds quadrants to the Starchart
        """
        for vert in (self.gvert - 1, self.gvert, self.gvert + 1):
            for horiz in (self.ghoriz - 1, self.ghoriz, self.ghoriz + 1):
                try:
                    self.quadrants_visited[vert][horiz] = True
                except IndexError:
                    continue

    def calcvector(self, direction):
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

    def launch_torps(self, to_fire):
        if to_fire > self.torpedoes:
            print(
                "[*ARMORY*] What do you think we are, the Bank of Ferenginar?! We don't even HAVE that many torepdoes!"
            )
            return

        queue: list = []
        for i in range(1, to_fire + 1):
            x = input(f"Input the target direction for torpedo #{i}\n> ")
            placeholder = x.split(" ")
            # try:
            queue.append(int(x))
            '''except:   
                print("[*ARMORY*] Sir, that command does not make sense.")
                return
            '''

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
                hinc, vinc = self.calcvector(direction)
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

    def add_collision_damage(self, severity):
        """
        Collision damage is *really* annoying.
        """

        for i in range(severity):
            decider = random.randint(0, 10)
            if decider == 0:
                self.damage["Warp Drive"] += random.choice(POSSIBLE_DAMAGES)
                print("[*DAMAGE CONTROL*] Sir, the warp drive has been damaged.")
            elif decider == 1:
                self.damage["Shields"] += random.choice(POSSIBLE_DAMAGES)
                print("[*DAMAGE CONTROL*] The shield generator is crushed.")
            elif decider == 2:
                self.damage["Photon Torpedoes"] += random.choice(POSSIBLE_DAMAGES)
                print(
                    "[*DAMAGE CONTROL*] Photon torpedo launching systems have been damaged."
                )
            elif decider == 3:
                self.damage["Impulse Drive"] += random.choice(POSSIBLE_DAMAGES)
                print("[*DAMAGE CONTROL*] Captain, the impulse drive is damaged.")
            elif decider == 4:
                self.damage["Communications"] += random.choice(POSSIBLE_DAMAGES)
                print(
                    "[*DAMAGE CONTROL*] The subspace communications equipment has been smashed."
                )
            elif decider == 5:
                self.damage["Short-Range Sensors"] += random.choice(POSSIBLE_DAMAGES)
                print(
                    "[*DAMAGE CONTROL*] Short-range sensors have been rendered inoperable."
                )
            elif decider == 6:
                self.damage["Long-Range Sensors"] += random.choice(POSSIBLE_DAMAGES)
                print(
                    "[*DAMAGE CONTROL*] Long-range sensors have been rendered inoperable."
                )
            elif decider == 7:
                self.damage["Life Support"] += random.choice(POSSIBLE_DAMAGES)
                print(
                    "[*DAMAGE CONTROL*] Sir, life support has been critically damaged! We still have reserves, "
                    "but they won't last long. "
                )

    def photons(self):
        if self.torpedoes == 0:
            print("[*ARMORY*] I'm afraid that we are out of torpedoes, sir.")
            return

        try:
            fire_number = int(
                input("[*ARMORY*] How many torpedoes would you like to fire?\n> ")
            )
        except ValueError:
            print(
                "\n[*ARMORY*] Sir, can you please speak more clearly? I cannot understand what you just said."
            )
            return
        print(fire_number)
        if 3 < fire_number < self.torpedoes:
            print("\n[*ARMORY*] Captain, firing that many would melt the tubes!")
            fire_anyway = input(
                "\nWould you like to fire anyway? (Doing so will incur damage)\n> "
            )
            if (
                    fire_anyway == "Y"
                    or fire_anyway == "y"
                    or fire_anyway == "yes"
                    or fire_anyway == "Yes"
            ):
                self.launch_torps(fire_number)
                for i in range(fire_number):
                    self.damage["Photon Torpedoes"] += random.choice([0.1, 0.2, 0.3])

        elif fire_number > self.torpedoes:
            print(
                "\n[*ARMORY*] What do you think we are, the Bank of Ferenginar?! We don't HAVE that many torpedoes!"
            )

        else:
            self.launch_torps(fire_number)
        self.klingons_attack()  # The Klingons get a chance to fire back.

    def klingons_attack(self):
        """
        It wouldn't be fair for the Klingons if they weren't allowed to fire back...
        """

        total_units = 0
        if self.galaxy[self.gvert][self.ghoriz][0] > 0:
            print("[*Lt. SULU*] Sir, the Klingons are attacking.")
            if (
                    self.shield_stat == True
            ):  # The shields block most attacks, but only if they are turned on.
                for i in self.local_klingons_list:
                    print()
                    to_add = random.randint(50, 200)
                    self.shields -= to_add
                    total_units += to_add
                    if self.shields < 0:
                        self.shields = 0
                        self.shield_stat = False

                    if self.shield_stat == False or random.randint(0, 10) == 1:
                        decider = random.randint(0, 10)
                        if decider == 0:
                            self.damage["Warp Drive"] += random.choice(POSSIBLE_DAMAGES)
                            displays.type_fast(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Warp Drive"
                            )
                        elif decider == 1:
                            self.damage["Shields"] += random.choice(POSSIBLE_DAMAGES)
                            displays.type_fast(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Shield Generator"
                            )
                        elif decider == 2:
                            self.damage["Photon Torpedoes"] += random.choice(
                                POSSIBLE_DAMAGES
                            )
                            displays.type_fast(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Photon Torpedoes"
                            )
                        elif decider == 3:
                            self.damage["Impulse Drive"] += random.choice(
                                POSSIBLE_DAMAGES
                            )
                            displays.type_fast(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Impulse Drive"
                            )
                        elif decider == 4:
                            self.damage["Communications"] += random.choice(
                                POSSIBLE_DAMAGES
                            )
                            displays.type_fast(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Subspace Communications Equipment"
                            )
                        elif decider == 5:
                            self.damage["Short-Range Sensors"] += random.choice(
                                POSSIBLE_DAMAGES
                            )
                            displays.type_fast(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Short-Range Sensors"
                            )
                        elif decider == 6:
                            self.damage["Long-Range Sensors"] += random.choice(
                                POSSIBLE_DAMAGES
                            )
                            displays.type_fast(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Long-Range Sensors"
                            )
                        elif decider == 7:
                            self.damage["Life Support"] += random.choice(
                                POSSIBLE_DAMAGES
                            )
                            displays.type_fast(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Life Support"
                            )
                print(
                    "%i damage has been incurred, reducing shields to %.0f percent."
                    % (total_units, (self.shields / 1500) * 100)
                )
            else:
                for i in self.local_klingons_list:
                    print()
                    yorn = random.randint(0, 10)
                    if yorn > 9:
                        return
                    decider = random.randint(0, 10)
                    if decider == 0:
                        self.damage["Warp Drive"] += random.choice(POSSIBLE_DAMAGES)
                        displays.type_fast(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Warp Drive"
                        )
                    elif decider == 1:
                        self.damage["Shields"] += random.choice(POSSIBLE_DAMAGES)
                        displays.type_fast(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Shield Generator"
                        )
                    elif decider == 2:
                        self.damage["Photon Torpedoes"] += random.choice(
                            POSSIBLE_DAMAGES
                        )
                        displays.type_fast(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Photon Torpedoes"
                        )
                    elif decider == 3:
                        self.damage["Impulse Drive"] += random.choice(POSSIBLE_DAMAGES)
                        displays.type_fast(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Impulse Drive"
                        )
                    elif decider == 4:
                        self.damage["Communications"] += random.choice(POSSIBLE_DAMAGES)
                        displays.type_fast(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Subspace Communications Equipment"
                        )
                    elif decider == 5:
                        self.damage["Short-Range Sensors"] += random.choice(
                            POSSIBLE_DAMAGES
                        )
                        displays.type_fast(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Short-Range Sensors"
                        )
                    elif decider == 6:
                        self.damage["Long-Range Sensors"] += random.choice(
                            POSSIBLE_DAMAGES
                        )
                        displays.type_fast(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Long-Range Sensors"
                        )
                    elif decider == 7:
                        self.damage["Life Support"] += random.choice(POSSIBLE_DAMAGES)
                        displays.type_fast(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Life Support"
                        )

                    # TODO add more options as required.

    def NOPE(self) -> None:
        """
        The Player is attempting to leave the galaxy.
        I can't let that happen, so the player gets two warnings.
        The third time they attempt to do this I will be forced to concede that their
        navigation is abominable, and thus kill them.

        It's a hard world we live in; I can't just let any dumb schmuck try to protect
        the Federation from the Klingons.
        """

        if self.leave_attempts <= 3:
            displays.type_slow(
                "\nYOU HAVE ATTEMPTED TO CROSS THE NEGATIVE ENERGY BARRIER AT THE EDGE OF THE GALAXY.\nTHE THIRD TIME "
                "YOU TRY TO DO THIS THE ENTERPRISE WILL BE DESTROYED. "
            )
            self.leave_attempts += 1
        else:
            displays.type_slow(
                "\nYou have attempted to cross the negative energy barrier at the edge of the galaxy three "
                "times.\n\nYour navigation is abominable. "
            )
            self.alive = False

    def enter_quadrant(self, new_gvert, new_ghoriz) -> bool:
        '''
        Try to enter quadrant at (new_gvert, new_ghoriz).
        '''
        if (new_gvert < 0) or (new_gvert >= 10) or (new_ghoriz < 0) or (new_ghoriz >= 10):
            self.NOPE()
            return False
        else:
            return True


if __name__ == "__main__":
    Enterprise()
