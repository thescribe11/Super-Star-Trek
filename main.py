import random
import sys
from GameMethods import Enterprise, Torpedo, MakeUniverse

import pprint # For debuggin purposes only. Delete when done.

def main():
    universe = MakeUniverse().return_universe()
    enterprise = Enterprise({'quadrant': (random.randint(0, 9),random.randint(0,9)), 'sector': (random.randint(0, 9), random.randint(0, 9))})
    
    printer = pprint.PrettyPrinter(2)
    printer.pprint(universe)
    return None

if __name__ == "__main__":
    main()