"""
I would have put this in classes, but that creates a really nasty circular import that I decided wasn't worth it.
"""

import displays
import random
import math
from helper_funcs import create_array

DEBUG = True  # Determines whether or not some features are enabled.

POSSIBLE_DAMAGES = [i / 10 for i in range(50, 79)]


def print_debug(*args, **kwargs) -> None:
    """
    I regret ever creating it, but now I'm stuck with it since I don't want to go through and find every reference.

    Next time I'll just use the logging module.
    """
    pass


class Enterprise(object):
    def __init__(self, testing=False):
        super().__init__()
        self.alive = True
        self.leave_attempts = 0
        self.energy = 3000
        self.shield_stat = False
        self.shields = 1500
        self.torpedoes = 8
        self.crystals = 0  # I may or may not keep this

        self.gvert, self.ghoriz, self.svert, self.shoriz = (  # Place the Enterprise at a random location.
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
            random.randint(0, 9),
        )

        self.klingons = 0
        self.warp_speed = 5
        self.environment_reserves = 100.0
        self.docked = False
        self.date = 100.0 * int(31.0 * random.random() + 20.0)
        self.time_remaining = random.randint(8, 15)
        self.cloaked = False

        global_klingons = create_array(10, 10)
        global_starbases = create_array(10, 10)
        global_stars = create_array(10, 10)

        self.galaxy = create_array(10, 10, value=[0, 0, 0])

        self.sector = create_array(10, 10, value=".")
        self.quadrants_visited = create_array(10, 10, value=False)

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

    def check_movement_collision(self, new_vert: int, new_horiz: float, old_horiz: float) -> (bool, float):
        """
        Check to see if the Enterprise has crashed into anything while moving.

        TODO: Add logic.
        """

        found: bool = False

        int_new_horiz: int = math.floor(new_horiz)
        int_old_horiz = math.floor(old_horiz)
        print_debug(self.sector[new_vert][int_new_horiz])
        print(f"{int_new_horiz=}, {int_old_horiz=}")

        step = 1 if int_new_horiz >= int_old_horiz else -1

        for horiz in range(int_old_horiz, int_new_horiz, step):
            print("test iter #1")
            if self.sector[new_vert][horiz] == '.':
                return False, 0
            elif self.sector[new_vert][horiz] == 'K':
                for klingon in self.local_klingons_list:
                    if klingon.is_at(new_vert, horiz):
                        print("Klingon detected!")
                        found = True

                        if (
                                (
                                        yorn := input(
                                            "WARNING: Klingon detected in the Enterprise's flight path.\nRam it? > "))
                                            .upper()
                                            .startswith("Y")
                        ):
                            pass  # Make a kill_klingon() function that kills the Klingon, adds score, and cleans up
                            # the starmap &cetera.

                if not found:
                    raise LookupError(  # I wasn't sure what type of error to use; this was the closest I could find.
                        'It appears that the Klingon is not where it should be.\nHOUSTON, WE HAVE A PROBLEM!')

        print("Activating fail-safe in check_movement_collision()!")
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

    def klingons_attack(self):
        """
        It wouldn't be fair for the Klingons if they weren't allowed to fire back...
        """

        total_units = 0
        if self.galaxy[self.gvert][self.ghoriz][0] > 0:
            print("[*Lt. SULU*] Sir, the Klingons are attacking.")
            if self.shield_stat:  # The shields block most attacks, but only if they are turned on.
                for i in self.local_klingons_list:
                    print()
                    to_add = random.randint(50, 200)
                    self.shields -= to_add
                    total_units += to_add
                    if self.shields < 0:
                        self.shields = 0
                        self.shield_stat = False

                    if self.shield_stat or random.randint(0, 10) == 1:
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
                for _i in self.local_klingons_list:
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
        """
        Try to enter quadrant at (new_gvert, new_ghoriz).
        """
        if (new_gvert < 0) or (new_gvert >= 10) or (new_ghoriz < 0) or (new_ghoriz >= 10):
            self.NOPE()
            return False
        else:
            return True
