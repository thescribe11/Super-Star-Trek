import random
from sys import stdout
from classes import Klingon


def beginning_spiel() -> str:
    print("""
    =======================
    --- Super Star Trek ---
    =======================
    
    """ )
    password = input("\nPlease input a password for higher-level commands.\n> ")
    print("\nThank you. Starting the game...\n")

    return password

'''
### It is important to know the amount of damage each part of the ship has.
'''
def print_damage(damage):
    amount = 0
    for i in damage:
        if damage[i] > 0:
            amount += 1
            stdout.write("> ")
            print(f"{i}:{''.join([' ' for _ in range(23-len(i))])}{damage[i]}")
    if amount == 0:
        print("*************\n* NO DAMAGE *\n*************")

'''
### Damage to the short-range sensors severely reduces their range.
'''
def print_d_srscan(sector, ghoriz, gvert, shoriz, svert, alert, torps, energy, klingons, shields, shield_stat, speed, e_condition, e_reserves, date, time_remaining):
    print("    1 2 3 4 5 6 7 8 9 10")
    print("  ┏━━━━━━━━━━━━━━━━━━━━━┓")
    for vert in range(10):
        stdout.write(f"{''.join([' ' for _ in range(2-(1 if vert<9 else 2))])}{vert+1}┃")
        for horiz in range(10):
            if ((vert == svert) or (vert == svert - 1) or (vert == svert + 1)) and ((horiz == shoriz) or (horiz == shoriz - 1) or (horiz == shoriz + 1)):
                stdout.write(f" {sector[vert][horiz]}")
            else:
                stdout.write(" ?")
        stdout.write(" ┃   ")
    
        if vert == 0:
            print(f"Sector {svert+1},{shoriz+1} of quadrant {gvert+1},{ghoriz+1}")
        elif vert == 1:
            print(f"Condition:    {alert}")
        elif vert == 2:
            print(f"Torpedoes:    {torps}")
        elif vert == 3:
            print(f"Life Support: {e_condition}", end='')
            if e_condition == "ACTIVE":
                print("")
            else:
                print(f", {e_reserves}% remaining.")
        elif vert == 4:
            print(f"Energy:       {energy}")
        elif vert == 5:
            print(f"Shields:      {('UP' if shield_stat == True else 'DOWN')}, {shields} energy remaining")
        elif vert == 6:
            print(f"Warp speed:   {speed}")
        elif vert == 7:
            print(f"Klingons:     {klingons}")
        elif vert == 8:
            print(f"Stardate:     {date}")
        elif vert == 9:
            print(f"Time left:    {time_remaining}")
        else:
            print("")
    print("  ┗━━━━━━━━━━━━━━━━━━━━━┛")


'''
### Prints the short-range sensor scan.
'''
def print_srscan(sector, position, alert, torps, energy, klingons, shields, shield_stat, speed, e_condition, e_reserves, date, time_remaining):
    print("    1 2 3 4 5 6 7 8 9 10")
    print("  ┏━━━━━━━━━━━━━━━━━━━━━┓")
    for vert in range(10):
        stdout.write(f"{''.join([' ' for _ in range(2-(1 if vert<9 else 2))])}{vert+1}┃")
        for horiz in range(10):
            stdout.write(f" {sector[vert][horiz]}")
        stdout.write(" ┃   ")
        if vert == 0:
            print(f"Sector {position[1][1]+1},{position[1][0]+1} of quadrant {position[0][1]},{position[0][0]}")
        elif vert == 1:
            print(f"Condition:    {alert}")
        elif vert == 2:
            print(f"Torpedoes:    {torps}")
        elif vert == 3:
            print(f"Life Support: {e_condition}", end='')
            if e_condition == "ACTIVE":
                print("")
            else:
                print(f", {e_reserves}% remaining.")
        elif vert == 4:
            print(f"Energy:       {energy}")
        elif vert == 5:
            print(f"Shields:      {('UP' if shield_stat == True else 'DOWN')}, {shields} energy remaining")
        elif vert == 6:
            print(f"Warp speed:   {speed}")
        elif vert == 7:
            print(f"Klingons:     {klingons}")
        elif vert == 8:
            print(f"Stardate:     {date}")
        elif vert == 9:
            print(f"Time left:    {time_remaining}")
        else:
            print("")
    print("  ┗━━━━━━━━━━━━━━━━━━━━━┛")

'''
## Upon entering a new quadrant, one must generate a map of the quadrant.
'''
def enter_quadrant(quadrant: list, gvert, ghoriz, svert, shoriz, energy: int) -> (list, list, str):
    local_klingons_list = []
    placed = 0

    sector = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ]

    sector[svert][shoriz] = 'E'

    if quadrant[0] > 0:
        while placed < quadrant[0]:
            placed += 1
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if sector[y][x] == '.':
                sector[y][x] = 'K'
                local_klingons_list.append(Klingon(x=y, y=x, health=random.randint(200, 600)))
    
    placed = 0
    if quadrant[1] != 0:
        while placed < quadrant[1]:
            placed += 1
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            
            if sector[y][x] == '.':
                sector[y][x] = 'B'
            else:
                placed -= 1

    placed = 0
    tries = 0
    if quadrant[2] != 0:
        while placed < quadrant[2]:
            placed += 1
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            
            if sector[y][x] == '.':
                sector[y][x] = "+"
            else:
                placed -= 1
                tries += 1
                if tries > 100:
                    print("**ERROR**: Unable to place star in quadrant.")
    
    panic = ""
    if quadrant[0] == 0 and energy > 500:
        panic = "Green"
    elif energy <= 500:
        panic = "Yellow"
    else:
        panic = "RED"

    return (sector, local_klingons_list, panic)
    