import random
import sys
from GameMethods import Enterprise, Torpedo, MakeUniverse
from GameCommands import srs, quadrant_printer

import pprint  # For debuggin purposes only. Delete when done.

def GetInput(prompt):
    print(prompt)
    return input("> ")

def main():
    universe = MakeUniverse()
    klingons = universe.klingons
    universe = universe.return_universe()
    enterprise = Enterprise({'quadrant': [random.randint(0, 7),random.randint(0,7)], 'sector': [random.randint(0, 9), random.randint(0, 9)]}, klingons)
    
    printer = pprint.PrettyPrinter(2)
    printer.pprint(universe)

    score = 0
    current_sector_configuration = None
    scan_is_current = False

    while score >= 0 and enterprise.destroyed == False:
        x = GetInput("")

        if x == "srs":
            if scan_is_current == False:
                location = enterprise.get_location()
                sector_location = enterprise.get_sector_location()
                print(location)
                current_sector_configuration = srs(universe[location[0]][location[1]], sector_location, klingons)
                scan_is_current = True  # Hyper important; don't delete this.
            
            quadrant_printer(current_sector_configuration, enterprise)

        elif x == "impulse":
            enterprise.move(current_sector_configuration)

    return None
# Some stuff to trigger a commit.

if __name__ == "__main__":
    main()
