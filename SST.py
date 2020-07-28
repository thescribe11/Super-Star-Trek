import math
import random
from sys import stdout
from typing import Final
import time

import displays

## The date of the Treaty of Algeron.
## It forbids the Federation from using cloaking devices, so the Romulans
## will get annoyed if they catch the Enterprise using the one it stole from them.
ALGERON: Final = 2311.0
IDIDIT: bool = False  # Controls if the Romulans are antagonistic

## Controls whether debug features like print_debug() are active.
DEBUG = True

## Unfortunately, Python doesn't have a convenient way to make float ranges.
## As a result, my only choices were (a) put it here, or (b) initialize it
## every time I use it. The latter is inefficient, so I just decided to
## make a global variable.
POSSIBLE_DAMAGES = [
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1,
    1.1,
    1.2,
    1.3,
    1.4,
    1.5,
    1.6,
    1.7,
    1.8,
    1.9,
    2,
    2.1,
    2.2,
    2.3,
    2.4,
    2.5,
    2.6,
    2.7,
    2.8,
    2.9,
    3,
    3.1,
    3.2,
    3.3,
    3.4,
    3.5,
    3.6,
    3.7,
    3.8,
    3.9,
    4,
    4.1,
    4.2,
    4.3,
    4.4,
    4.5,
    4.6,
    4.7,
    4.8,
    4.9,
    5,
    5.1,
    5.2,
    5.3,
    5.4,
    5.5,
    5.6,
    5.7,
    5.8,
    5.9,
    6,
    6.1,
    6.2,
    6.3,
    6.4,
    6.5,
    6.6,
    6.7,
    6.8,
    6.9,
    7,
    7.1,
    7.2,
    7.3,
    7.4,
    7.6,
]


def print_debug(string: str):
    if DEBUG:
        print(string)


class Enterprise(object):
    def __init__(self):
        super().__init__()
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

        self.leave_attempts = 0

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
                if self.sector_current == False:
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
                        "[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings until it is repaired.\n"
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
                        "[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings until it is repaired.\n"
                    )
                self.klingons_attack()

            elif command[0] == "S" or command[0] == "s":
                if self.damage["Shields"] != 0:
                    print(
                        "[*SHIELD CONTROL*] The shield generator is fused, sir; I cannot change the settings until it is repaired.\n"
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
                "\n[*SHIELD CONTROL*] How much energy would you like to transfer? (negative values return energy to main capacitors)\n> "
            )
        except ValueError:
            print("[*SHIELD CONTROL*] Sir, that is not a valid amount.")

        ## TODO Add energy amount changing.

    def warp_move(self) -> bool:
        """
        Move within quadrant.
        If True is returned, the Enterprise moved;
        otherwise, the manuever was cancelled.
        """

        blooey = False
        damaged = False
        trip_time: float = 0
        sdistance: float = 0
        sslope: float = 0

        if self.damage["Warp Drive"] > 5:
            print(
                "[*ENGINEERING*] Scotty here. The warp drive is badly damaged, sir; we'd better not use it until I can get this damage repaired."
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
                power = (sdistance + 0.05) * 15 * (2 if self.shield_stat == True else 1)
                if power >= self.energy:
                    print(
                        "[*ENGINEERING*] Scotty here. I'm sorry captain, but we canna' do it!\n[*ENGINEERING*] We simply don't have enough power remaining."
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
                    "[*ENGINEERING*] Scotty here. I'm sorry captain, but we canna' do it!\n[*ENGINEERING*] We simply don't have enough power remaining."
                )

        print_debug(f"{sslope=}")

        self.impulse_move(sslope, svert_diff, shoriz_diff)
        self.energy -= power
        self.time_remaining -= trip_time
        return True

    def impulse_move(self, unprocessed_slope, svert_diff, shoriz_diff):
        """
        Intra-quadrant movement

        TODO: Add a call to `enter_quadrant()` at the end which is triggered
        by the Enterprise changing quadrants.
        """
        self.sector[self.svert][self.shoriz] = "."

        slope = (
            unprocessed_slope * 1 if svert_diff > 0 else -1
        )  ## In other words, +slope if the Enterprise is moving vertically, otherwise -slope.

        if svert_diff != 0:
            old_vert, old_horiz = self.svert, self.shoriz
            for i in range(abs(svert_diff)):
                new_vert = old_vert + 1 if svert_diff > 0 else -1
                new_horiz = old_horiz + slope

                try:
                    assert new_vert > -1
                except AssertionError:
                    new_vert = 9
                    self.sector = [["." for i in range(10)] for i in range(10)]
                    self.gvert -= 1
                    self.sector_current = False

                try:
                    assert new_vert < 10
                except AssertionError:
                    if self.gvert < 10:
                        new_vert = 0
                        self.sector = [["." for i in range(10)] for i in range(10)]
                        self.gvert += 1
                        self.sector_current = False
                    else:
                        self.NOPE()
                        break

                try:
                    assert new_horiz > -1
                except AssertionError:
                    if self.ghoriz > 0:
                        new_horiz = 9
                        self.sector = [["." for i in range(10)] for i in range(10)]
                        self.ghoriz -= 1
                        self.sector_current = False
                    else:
                        self.NOPE()
                        break

                try:
                    assert new_horiz < 10
                except AssertionError:
                    if self.ghoriz < 9:
                        new_horiz = 0
                        self.sector = [["." for i in range(10)] for i in range(10)]
                        self.ghoriz += 1
                        self.sector_current = False
                    else:
                        self.NOPE()
                        break

                x = self.check_movement_collision(new_vert, new_horiz)
                print_debug(x)
                if x:
                    break

                old_vert = new_vert
                old_horiz = new_horiz
            self.svert, self.shoriz = old_vert, round(old_horiz)

        else:
            old_horiz = new_horiz = self.shoriz

            for _ in range(abs(shoriz_diff)):
                new_horiz += 1 if shoriz_diff > 1 else -1

                try:
                    assert new_horiz >= 0
                except AssertionError:
                    if self.ghoriz > 0:
                        self.ghoriz -= 1
                        self.sector_current = False
                    else:
                        self.NOPE()

                try:
                    assert new_horiz <= 9
                except AssertionError:
                    if self.ghoriz < 9:
                        self.ghoriz += 1
                        self.sector_current = False
                    else:
                        self.NOPE()

                if not (x := self.check_movement_collision(self.svert, new_horiz)):
                    print_debug(x)
                    old_horiz = new_horiz
                else:
                    print_debug(x)
                    new_horiz = old_horiz  ## Prevent the Enterprise from taking up the wrong real estate.
                    break
            self.shoriz = new_horiz

        self.sector[self.svert][self.shoriz] = "E"

    def check_movement_collision(self, new_vert: int, new_horiz: float) -> bool:
        """
        Check to see if the Enterprise has crashed into anything while moving.
        """

        int_new_horiz = round(
            new_horiz
        )  # new_horiz as an int, in order to avoid excess calls to int().
        print_debug(self.sector[new_vert][int_new_horiz])
        if (
            self.sector[new_vert][int_new_horiz] == "."
        ):  ## Sector is empty; move into it.
            return False
        elif self.sector[new_vert][int_new_horiz] in (
            "+",
            "B",
        ):  # Sector is occupied by a friendly/neutral object; emergency stop.
            self.emergency_stop(new_vert, int_new_horiz)
            return True
        elif self.sector[new_vert][int_new_horiz] in (
            "K",
            "R",
        ):  ## Sector is occupied by an enemy; ram it if the player give approval.
            ## TODO: Add more enemies as necessary.
            yorn = input(
                "[*Cmdr SPOCK*] Sir, sensors have detected an enemy ship in our path. Should we ram it?\n> "
            )
            if yorn.startswith("Y") or yorn.startswith("y"):
                displays.type_fast(
                    "*AWHOOOGAH!*   *AWHOOOGAH!*\nAll hands, brace for impact!\n\n"
                )
                self.add_collision_damage(random.randint(3, 6))
                for i in self.local_klingons_list:
                    if i.x == new_vert and i.y == int_new_horiz:
                        self.local_klingons_list.remove(i)
                if self.sector[new_vert][int_new_horiz] == "K":
                    self.klingons -= 1
                    displays.type_fast(
                        f"***Klingon at ({new_vert}, {int_new_horiz}) destroyed in collision."
                    )
                elif self.sector[new_vert][int_new_horiz] == "R":
                    displays.type_fast(
                        f"***Romulan at ({new_vert}, {int_new_horiz}) destroyed in collision."
                    )
                else:
                    displays.type_fast(
                        f"*** ??? at ({new_vert}, {int_new_horiz}) destroyed in collision."
                    )
                time.sleep(0.3)

                if random.randint(0, 5) == 5:
                    self.alive = (
                        False  ## TODO add special game-over text for ship crushed.
                    )
                return True  ## The collision will stop the Enterprise, regardless of whether or not it survives.
            else:
                self.emergency_stop(new_vert, int_new_horiz)
                return True

        print("Houston, we have a problem!")
        return False  ## This should never be executed; it's just here to keep MyPy from bugging out.

    def emergency_stop(self, vert, horiz):
        """
        Performs emergency stopping manuevers.
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
        if direction < 5 and direction > 1:
            vinc = -1
        elif direction > 5:
            vinc = 1
        else:
            vinc = 0
        return (hinc, vinc)

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
            try:
                queue.append(int(x))
            except:
                print("[*ARMORY*] Sir, that command does not make sense.")
                return

        current_torp = 0

        for direction in queue:
            current_torp += 1
            print(f"\n* Torpedo #{current_torp}\nTorpedo track:")
            if direction >= 1 and direction <= 9:
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
                while out == False:
                    print(f"({vert+1},{horiz+1}) ", end="")
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
                                if self.shield_stat == True:
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
                                        self.damage["Shields"] += random.randint(0.5, 3)
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
                    "[*DAMAGE CONTROL*] Sir, life support has been critically damaged! We still have reserves, but they won't last long."
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
        if fire_number > 3 and fire_number < self.torpedoes:
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

    def change_quadrant(self, gvert, ghoriz, randomize_pos=False):
        ## Checks if the Enterprise has tried to leave the galaxy.
        quadrant_changed = False
        if self.svert < 0:
            if self.gvert == -1 and self.leave_attempts < 3:
                self.svert = 0
                self.NOPE()
            else:
                self.gvert -= 1
                self.sector_current = False
                quadrant_changed = True
        elif self.svert > 9:
            if self.gvert == 10 and self.leave_attempts < 3:
                self.NOPE()
                self.svert = 9
            else:
                self.gvert += 1
                self.sector_current = False
                quadrant_changed = True
        if self.shoriz < 0:
            if self.ghoriz == -1 and self.leave_attempts < 3:
                self.shoriz = 0
                self.NOPE()
            else:
                self.ghoriz -= 1
                self.sector_current = False
                quadrant_changed = True
        elif self.shoriz > 9:
            if self.ghoriz == 10 and self.leave_attemps < 3:
                self.NOPE()
                self.shoriz = 9
            else:
                self.ghoriz += 1
                self.sector_current = False
                quadrant_changed = True

        if randomize_pos:
            self.svert = random.randint(0, 9)
            self.shoriz = random.randint(0, 9)

        if quadrant_changed:
            self.sector, self.local_klingons_list, self.panic = displays.enter_quadrant(
                self.galaxy[self.gvert][self.ghoriz],
                self.ghoriz,
                self.gvert,
                self.svert,
                self.shoriz,
                self.energy,
            )
            self.sector_current = True

        print(f"\nEntering quadrant ({self.gvert}, {self.ghoriz}).")

    def NOPE(self):
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
                "\nYOU HAVE ATTEMPTED TO CROSS THE NEGATIVE ENERGY BARRIER AT THE EDGE OF THE GALAXY.\nTHE THIRD TIME YOU TRY TO DO THIS THE ENTERPRISE WILL BE DESTROYED."
            )
            self.leave_attempts += 1
        else:
            displays.type_slow(
                "\nYou have attempted to cross the negative energy barrier at the edge of the galaxy three times.\n\nYour navigation is abominable."
            )
            self.alive = False


if __name__ == "__main__":
    Enterprise()
