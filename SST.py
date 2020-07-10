import math
import random
from sys import stdout

import displays

ALGERON = 2311.0  # The date of the Treaty of Algeron.


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

        self.time_left: float = 10.0

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

        for i in range(0, 9):
            for j in range(0, 9):
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
                    self.add_quadrant_to_lrscan()  # Update the starchart.
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

            elif (
                command == "t"
                or command == "torp"
                or command == "torps"
                or command == "torpedoes"
                or command == "photons"
            ):
                if self.damage["Photon Torpedoes"] == 0:
                    self.photons()
                else:
                    print("[*ARMORY*] Sir, the launching systems are inoperable.")

            elif command == "d" or command == "damage":
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

            elif command == "shields":
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

            elif command == "move" or command == "mov" or command == "m":
                self.warp_move()
                self.klingons_attack()

            elif command == "lrs" or command == "Lrs" or command == "lrscan":
                displays.print_lrs(
                    self.galaxy,
                    self.quadrants_visited,
                    self.gvert,
                    self.ghoriz,
                    (True if self.damage["Long-Range Sensors"] > 0 else False),
                )

    def change_shields(self):
        try:
            amount = int(
                input(
                    "\n[*SHIELD CONTROL*] How much energy would you like to transfer? (negative values return energy to main capacitors)\n> "
                )
            )
        except ValueError:
            print("[*SHIELD CONTROL*] Sir, that is not a valid amount.")
        if amount >= 0:
            if amount > 1500:
                print(
                    "[*SHIELD CONTROL*] Shields are maximised, returning excess energy to main capacitors."
                )
                to_add = amount - 1500
                if self.energy - to_add <= 0:
                    print(
                        "[*SHIELD CONTROL*] Sir, that would leave us with insufficient energy for ship operations."
                    )
                self.shields += to_add
                self.energy -= to_add
                return
            elif self.energy - amount > 0:
                print(f"[*SHIELD CONTROL*] Transferring {amount} energy to shields.")
                self.shields += amount
                self.energy -= amount
                return
            else:
                print(
                    "[*SHIELD CONTROL*] Sir, that would leave us with insufficient energy for ship operations."
                )
                return
        elif amount < 0:
            if self.shields - amount < 0:
                print(
                    "[*SHIELD CONTROL*] Shields reduced to 0%, transferring energy to main capacitors."
                )
                self.energy += self.shields
                self.shields = 0
            else:
                print(
                    "[*SHIELD CONTROL*] Transferring %i energy to main capacitors."
                    % amount
                )
                self.shields -= amount
                self.energy += amount

    def warp_move(self):
        blooey = False

        """
        dist = sqrt(deltax*deltax + deltay*deltay);
	    direc = atan2(deltax, deltay)*1.90985932;
        """

        if self.damage["Warp Drive"] > 10:
            print(
                "[*ENGINEERING*] The warp engines are badly damaged, sir; we'd better not use them until I can get this damage repaired."
            )
            return
        elif self.damage["Warp Drive"] > 0 and self.warp_speed > 4:
            print(
                "[*ENGINEERING*] Captain, the warp engines are damaged. I can only give you warp 4 until this damage is repaired."
            )
            return

        which = input("[*Lt. SULU*] Automatic or manual movement?\n> ")
        if which[0] == "a" or which[0] == "A":
            automatic = True
        elif which[0] == "m" or which[0] == "M":
            automatic = False
        else:
            print("[*Lt. SULU*] Captain, that doesn't make sense.")
            return

        distance = 0
        slope = 0
        power = 0
        dgvert = 0
        dghoriz = 0
        dsvert = 0
        dshoriz = 0
        gvert_diff = 0
        ghoriz_diff = 0
        svert_diff = 0
        shoriz_diff = 0

        if automatic:
            destination: list = [
                int(i) - 1
                for i in input("Please input destination coordinates\n> ").split(" ")
            ]
            if len(destination) == 2:
                print("Destination length: 2")
                for i in destination:
                    if not -1 < i < 10:
                        print("[*COMPUTER*] *ERROR* COORDINATES INVALID.")
                        return
                # dsvert = destination's vertical coord, dshoriz = destination's horizontal coord
                dsvert = int(destination[0])
                dshoriz = int(destination[1])
                svert_diff = dsvert - self.svert
                shoriz_diff = dshoriz - self.shoriz
                if svert_diff != 0:
                    slope = (self.shoriz - dshoriz) / (self.svert - dsvert)
                    distance = math.sqrt(svert_diff ** 2 + shoriz_diff ** 2)
                else:
                    slope = math.inf
                    distance = shoriz_diff

                trip_time = 10 * distance / self.warp_speed
                power = (
                    (distance + 0.05)
                    * (self.warp_speed ** 3)
                    * (2 if self.shield_stat == True else 1)
                )
                if power >= self.energy:
                    print("[*ENGINEERING*] Scotty here. ", end="")
                    iwarp = pow((self.energy / (distance + 0.05)), 0.333333333)
                    if iwarp <= 0:
                        print(
                            "I'm sorry captain, but we canna do it! We have insufficient energy; there's nothing I can do about it."
                        )
                        return
                    else:
                        print(
                            "We don't have enough energy, although we could do it at warp %.2f"
                            % iwarp,
                            end="",
                        )
                        if self.shield_stat:
                            print(", if you'll lower the shields.")
                        else:
                            print(".")
                    return

            elif len(destination) == 4:
                print("Destination length: 4")
                dgvert = destination[0]
                dghoriz = destination[1]
                dsvert = destination[2]
                dshoriz = destination[3]

                svert_diff = dsvert - self.svert
                shoriz_diff = dshoriz - self.shoriz
                gvert_diff = dgvert - self.gvert
                ghoriz_diff = dghoriz - self.ghoriz

                if (gvert_diff * 10) + svert_diff != 0:
                    slope = (
                        (shoriz_diff + (ghoriz_diff * 10))
                        - ((self.ghoriz * 10) + self.shoriz)
                    ) / (
                        (svert_diff + (gvert_diff * 10))
                        - ((self.gvert * 10) + self.svert)
                    )
                    distance = math.sqrt(
                        (svert_diff + (gvert_diff * 10)) ** 2
                        + (shoriz_diff + (ghoriz_diff * 10)) ** 2
                    )
                else:
                    slope = math.inf
                    distance = shoriz_diff + (ghoriz_diff * 10)
                trip_time = 10 * distance / self.warp_speed
                power = (
                    (distance + 0.05)
                    * (self.warp_speed ** 3)
                    * (1.5 if self.shield_stat else 1)
                    / 10
                )

                if power >= self.energy:
                    print("[*ENGINEERING*] Scotty here. ", end="")
                    iwarp = pow((self.energy / (distance + 0.05)), 0.333333333)
                    if iwarp <= 0:
                        print(
                            "I'm sorry captain, but we canna do it! We have insufficient energy; there's nothing I can do about it."
                        )
                        return
                    else:
                        print(
                            "We don't have enough energy, although we could do it at warp %.2f"
                            % iwarp,
                            end="",
                        )
                        if self.shield_stat:
                            print(", if you'll lower the shields.")
                        else:
                            print(".")
                    return
            else:
                print("[*COMPUTER*] *ERROR* COORDINATES INVALID.")

        else:
            deltas: list = input("Please input x and y displacements\n> ").split(" ")

        self.move(slope, gvert_diff, ghoriz_diff, svert_diff, shoriz_diff)
        self.energy -= power

    def move(self, slope, gvert_diff, ghoriz_diff, svert_diff, shoriz_diff):
        self.sector[self.svert][self.shoriz] = "."
        if gvert_diff == 0 and ghoriz_diff == 0:
            print("Regular movement.")
            if svert_diff > 0:
                for i in range(svert_diff):
                    new_vert = self.svert + 1
                    new_horiz = self.shoriz + slope
                    try:
                        if self.sector[new_vert][round(new_horiz)] == ".":
                            self.svert, self.shoriz = new_vert, round(new_horiz)
                        else:
                            self.emergency_stop(new_vert, new_horiz)
                            break
                    except IndexError:
                        self.change_quadrant(randomize_pos=True)
            elif svert_diff < 0:
                for i in range(abs(svert_diff)):
                    new_vert = self.svert - 1
                    new_horiz = self.shoriz - slope
                    try:
                        if self.sector[new_vert][round(new_horiz)] == ".":
                            self.svert, self.shoriz = new_vert, round(new_horiz)
                    except IndexError:
                        self.change_quadrant(randomize_pos=True)
            else:
                if shoriz_diff > 0:
                    for i in range(shoriz_diff):
                        new_horiz = self.shoriz + 1
                        try:
                            if self.sector[self.svert][new_horiz] == ".":
                                self.shoriz = new_horiz
                            else:
                                self.emergency_stop(self.shoriz, new_horiz)
                                break
                        except IndexError:
                            self.change_quadrant(randomize_pos=True)

                elif shoriz_diff < 0:
                    for i in range(abs(shoriz_diff)):
                        new_horiz = self.shoriz - 1
                        try:
                            if self.sector[self.svert][new_horiz] == ".":
                                self.shoriz = new_horiz
                            else:
                                self.emergency_stop(self.shoriz, new_horiz)
                                break
                        except IndexError:
                            self.change_quadrant(randomize_pos=True)
            self.sector[self.svert][self.shoriz] = "E"

        else:
            print("Extra-quadrant movement")
            # TODO Use slope to get to edge of quadrant regularly, and then navigate to the next quadrant.
            print(svert_diff)
            if svert_diff > 0:
                vdist_to_edge = 10 - self.svert
                hdist_to_edge = 10 - self.shoriz
                for i in range(
                    20
                ):  # 20 units should be more than enough to get reach the edge.
                    print(i)
                    new_vert = self.svert + 1
                    new_horiz = self.shoriz + slope
                    try:
                        if self.sector[new_vert][round(new_horiz)] == ".":
                            self.svert = new_vert
                            self.shoriz = round(new_horiz)
                            self.sector[self.svert][self.shoriz] = "E"
                        else:
                            self.emergency_stop(new_vert, round(new_horiz))
                            return
                    except IndexError:
                        print("Done")
                        break
            elif svert_diff < 0:
                for i in range(20):
                    print(i)
                    new_vert = self.svert - 1
                    new_horiz = self.shoriz - slope
                    try:
                        if self.sector[new_vert][round(new_horiz)] == ".":
                            self.svert = new_vert
                            self.shoriz = round(new_horiz)
                            self.sector[self.svert][self.shoriz] = "E"
                        else:
                            self.emergency_stop(new_vert, round(new_horiz))
                    except IndexError:
                        print("Done.")
                        break
            elif svert_diff == 0:
                for i in range(20):
                    print(i)
                    new_horiz = self.shoriz + 1
                    try:
                        if self.sector[self.svert][new_horiz] == ".":
                            self.shoriz = new_horiz
                            self.sector[self.svert][self.shoriz] = "E"
                        else:
                            self.emergency_stop(self.vert, new_horiz)
                    except IndexError:
                        print("Done.")
                        break

        self.sector[self.svert][self.shoriz] = "E"

    def emergency_stop(self, vert, horiz):
        print(
            "***WARNING*** Object detected at sector (%i, %.0f);\nEmergency stop requires %i units of energy."
            % (vert, horiz, (to_sub := random.randint(110, 130)))
        )
        self.energy -= to_sub

    def add_quadrant_to_lrscan(self):
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
                        print(
                            f"\nStarbase at ({vert}, {horiz}) destroyed. You monster.\n"
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
                self.torpedoes = self.torpedoes - 1

    def add_collision_damage(self, severity):
        """
        Collision damage is *really* annoying.
        """
        possible_damages = [
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
        for i in range(severity):
            decider = random.randint(0, 10)
            if decider == 0:
                self.damage["Warp Drive"] += random.choice(possible_damages)
                print("[*DAMAGE CONTROL*] Sir, the warp drive has been damaged.")
            elif decider == 1:
                self.damage["Shields"] += random.choice(possible_damages)
                print("[*DAMAGE CONTROL*] The shield generator is crushed.")
            elif decider == 2:
                self.damage["Photon Torpedoes"] += random.choice(possible_damages)
                print(
                    "[*DAMAGE CONTROL*] Photon torpedo launching systems have been damaged."
                )
            elif decider == 3:
                self.damage["Impulse Drive"] += random.choice(possible_damages)
                print("[*DAMAGE CONTROL*] Captain, the impulse drive is damaged.")
            elif decider == 4:
                self.damage["Communications"] += random.choice(possible_damages)
                print(
                    "[*DAMAGE CONTROL*] The subspace communications equipment has been smashed."
                )
            elif decider == 5:
                self.damage["Short-Range Sensors"] += random.choice(possible_damages)
                print(
                    "[*DAMAGE CONTROL*] Short-range sensors have been rendered inoperable."
                )
            elif decider == 6:
                self.damage["Long-Range Sensors"] += random.choice(possible_damages)
                print(
                    "[*DAMAGE CONTROL*] Long-range sensors have been rendered inoperable."
                )
            elif decider == 7:
                self.damage["Life Support"] += random.choice(possible_damages)
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
                "[*ARMORY*] Sir, can you please speak more clearly? I cannot understand what you just said."
            )
            return
        if fire_number > 3 and fire_number < self.torpedoes:
            print("[*ARMORY*] Captain, firing that many would melt the tubes!")
            fire_anyway = input(
                "Would you like to fire anyway? (Doing so will incur damage)\n> "
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
                "[*ARMORY*] What do you think we are, the Bank of Ferenginar?! We don't HAVE that many torpedoes!"
            )

        else:
            self.launch_torps(fire_number)
        self.klingons_attack()  # The Klingons get a chance to fire back.

    def klingons_attack(self):
        possible_damages = [
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
        ]  # Sorry that this is so long; Python doesn't like to make float ranges.

        total_units = 0
        if self.galaxy[self.gvert][self.ghoriz][0] > 0:
            print("[*Lt. SULU*] Sir, the Klingons are attacking.")
            if (
                self.shield_stat == True
            ):  # The shields block most attacks, but only if they are turned on.
                for i in self.local_klingons_list:
                    to_add = random.randint(50, 200)
                    self.shields -= to_add
                    total_units += to_add
                    if self.shields < 0:
                        self.shields = 0
                        self.shield_stat = False

                    if self.shield_stat == False or random.randint(0, 10) == 1:
                        decider = random.randint(0, 10)
                        if decider == 0:
                            self.damage["Warp Drive"] += random.choice(possible_damages)
                            print(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Subspace Radio damaged."
                            )
                        elif decider == 1:
                            self.damage["Shields"] += random.choice(possible_damages)
                            print(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Shield Generator fused."
                            )
                        elif decider == 2:
                            self.damage["Photon Torpedoes"] += random.choice(
                                possible_damages
                            )
                            print(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Photon Torpedo launching systems have been damaged."
                            )
                        elif decider == 3:
                            self.damage["Impulse Drive"] += random.choice(
                                possible_damages
                            )
                            print(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Impulse Drive disabled."
                            )
                        elif decider == 4:
                            self.damage["Communications"] += random.choice(
                                possible_damages
                            )
                            print(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Subspace Communications Equipment has been smashed."
                            )
                        elif decider == 5:
                            self.damage["Short-Range Sensors"] += random.choice(
                                possible_damages
                            )
                            print(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Short-Range Sensors have been rendered inoperable."
                            )
                        elif decider == 6:
                            self.damage["Long-Range Sensors"] += random.choice(
                                possible_damages
                            )
                            print(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Long-Range Sensors have been rendered inoperable."
                            )
                        elif decider == 7:
                            self.damage["Life Support"] += random.choice(
                                possible_damages
                            )
                            print(
                                "[*DAMAGE CONTROL*] ***CRITICAL HIT--Life Support disabled. We still have reserves, but they won't last long."
                            )
                print(
                    "%i damage has been incurred, reducing shields to %.0f percent."
                    % (total_units, (self.shields / 1500) * 100)
                )
            else:
                for i in self.local_klingons_list:
                    yorn = random.randint(0, 10)
                    if yorn > 9:
                        print(
                            "[*DAMAGE CONTROL*] Good news sir, they've missed the vital areas of the ship."
                        )
                        return
                    decider = random.randint(0, 10)
                    if decider == 0:
                        self.damage["Warp Drive"] += random.choice(possible_damages)
                        print(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Subspace Radio damaged."
                        )
                    elif decider == 1:
                        self.damage["Shields"] += random.choice(possible_damages)
                        print(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Shield Generator fused."
                        )
                    elif decider == 2:
                        self.damage["Photon Torpedoes"] += random.choice(
                            possible_damages
                        )
                        print(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Photon Torpedo launching systems have been damaged."
                        )
                    elif decider == 3:
                        self.damage["Impulse Drive"] += random.choice(possible_damages)
                        print(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Impulse Drive disabled."
                        )
                    elif decider == 4:
                        self.damage["Communications"] += random.choice(possible_damages)
                        print(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Subspace Communications Equipment has been smashed."
                        )
                    elif decider == 5:
                        self.damage["Short-Range Sensors"] += random.choice(
                            possible_damages
                        )
                        print(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Short-Range Sensors have been rendered inoperable."
                        )
                    elif decider == 6:
                        self.damage["Long-Range Sensors"] += random.choice(
                            possible_damages
                        )
                        print(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Long-Range Sensors have been rendered inoperable."
                        )
                    elif decider == 7:
                        self.damage["Life Support"] += random.choice(possible_damages)
                        print(
                            "[*DAMAGE CONTROL*] ***CRITICAL HIT--Life Support disabled. We still have reserves, but they won't last long."
                        )

                    # TODO add more options as required.

    def change_quadrant(self, randomize_pos=False):
        if self.svert < 0:
            if self.gvert == -1 and self.leave_attempts < 3:
                print(
                    "\nYOU HAVE ATTEMPTED TO CROSS THE NEGATIVE ENERGY BARRIER AT THE EDGE OF THE GALAXY.\nTHE THIRD TIME YOU TRY TO DO THIS THE ENTERPRISE WILL BE DESTROYED."
                )
                self.svert = 0
                self.leave_attempts += 1
            else:
                self.gvert -= 1
                self.sector_current = False
        elif self.svert > 9:
            if self.gvert == 10 and self.leave_attempts < 3:
                print(
                    "\nYOU HAVE ATTEMPTED TO CROSS THE NEGATIVE ENERGY BARRIER AT THE EDGE OF THE GALAXY.\nTHE THIRD TIME YOU TRY TO DO THIS THE ENTERPRISE WILL BE DESTROYED."
                )
                self.svert = 9
                self.leave_attempts += 1
            else:
                self.gvert += 1
                self.sector_current = False
        if self.shoriz < 0:
            if self.ghoriz == -1 and self.leave_attempts < 3:
                print(
                    "\nYOU HAVE ATTEMPTED TO CROSS THE NEGATIVE ENERGY BARRIER AT THE EDGE OF THE GALAXY.\nTHE THIRD TIME YOU TRY TO DO THIS THE ENTERPRISE WILL BE DESTROYED."
                )
                self.shoriz = 0
                self.leave_attempts += 1
            else:
                self.ghoriz -= 1
                self.sector_current = False
        elif self.shoriz > 9:
            if self.ghoriz == 10 and self.leave_attemps < 3:
                print(
                    "\nYOU HAVE ATTEMPTED TO CROSS THE NEGATIVE ENERGY BARRIER AT THE EDGE OF THE GALAXY.\nTHE THIRD TIME YOU TRY TO DO THIS THE ENTERPRISE WILL BE DESTROYED."
                )
                self.shoriz = 9
                self.leave_attempts += 1
            else:
                self.ghoriz += 1
                self.sector_current = False

        if (
            self.leave_attempts >= 3
        ):  # Apparently the player missed the "don't do this" memo.
            print(
                "\nYou have attempted to cross the negative energy barrier at the edge of the galaxy three times.\nYour navigation is abominable."
            )
            self.alive = False
            return

        if randomize_pos:
            self.svert = random.randint(0, 9)
            self.shoriz = random.randint(0, 9)

        print(f"\nEntering quadrant ({self.gvert}, {self.ghoriz}).")


if __name__ == "__main__":
    Enterprise()
