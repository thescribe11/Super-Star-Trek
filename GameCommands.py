import random
import sys
import math

def srs(quadrant, ent_location, klingons:int):
    current_sector = [['.' for _ in range(10)] for y in range(10)]
    print(quadrant)
    i = 0

    current_sector[ent_location[0]][ent_location[1]] = 'E'

    while i < quadrant[0]/100:
        i += 1
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        if current_sector[y][x] == '.':
            current_sector[y][x] = 'K'
        else:
            i -= 1
        
    i = 0
    if quadrant[1] == 1:
        while i < 1:
            i += 1
            x = random.randint(0, 9)
            y = random.randint(0, 9)

            if current_sector[y][x] == '.':
                current_sector[y][x] = 'B'
            else:
                i -= 1
    
    i = 0
    while i < quadrant[2]:
        i += 1
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        if current_sector[y][x] == '.':
            current_sector[y][x] = '*'
        else:
            i -= 1
    
    print(current_sector)
    print("\n")
    return current_sector


def quadrant_printer(current_quad, enterprise):
    i = -1
    for it in current_quad:
        i += 1
        sys.stdout.write(str(int(i) + 1))
        
        to_print = '  '
        if int(math.log10(i + 1)) + 1 == 2:
            to_print = ' '
        sys.stdout.write(to_print)

        for j in it:
            sys.stdout.write(f" {j}")

        sys.stdout.write("  ")

        if i == 0:
            sys.stdout.write("Energy: " + str(enterprise.energy) + "\n")
        elif i == 1:
            sys.stdout.write("Torpedoes: " + str(enterprise.torps) + "\n")
        elif i == 2:
            sys.stdout.write("Klingons: " + str(enterprise.klingons) + "\n")
        else:
            sys.stdout.write("\n")
