import random
import math
import sys

def cin(prompt: str, typer=str, / ):
    '''
    Returns command-line input in type-casted form.
    '''
    if typer == "str":
        return input(prompt + "\n> ")
    elif typer == 'int':
        return int(input(prompt + "\n> "))
    elif typer == 'float':
        return float(input(prompt + "\n> "))


class Enterprise(object):
    '''
This class represents the U.S.S. Enterprise, which the player controls.

Public functions:

~ Movement:
- WarpMove(), moves the Enterprise via Warp Drive.
- ImpulseMove(), moves the Enterprise via the Impulse Drive.

~ Weapons:
- FirePhasers(), which fires the Phasers at enemies.
- FireTorpedoes(), fires the Photon Torpedoes

~ Shields:
- ChangeShieldEnergy(), add/remove energy from shields.
- ChangeShieldStatus(), on/off switch for the shields.

~ Damage control:
- Rest(), skip time spent in repairs.
- GetDamage(), prints out current damage.
- CheckDamage( <partOfShip> ), sees if <partOfShip> is damaged.

~ Sensors:
- LrScan(), prints out map of known space.
- SrScan(), prints out map of current sector.
    '''
    energy = 3000           # Available energy remaining
    shield_energy = 200     # How much energy remains in the shields.
    shield_status = False   # Whether or not the shields are up
    torpedoes = 8           # Remaining photon torpedoes
    is_alive = True         # Determines if the Enterprise still exists.

    location = [               # Represents the Enterprise's current location
        random.randint(0, 9),  # Sector x
        random.randint(0, 9),  # Sector y
        random.randint(0, 7),  # Quadrant x
        random.randint(0, 7)   # Quadrant y
    ]
    
    damage = {                    # Says which (if any) parts of the ship are damaged.
        "shields": False,      # Shield emitters
        "phasers": False,      # Phaser arrays
        "torps": False,        # Photon torpedo launching systems
        "warp": False,         # Warp drive
        "impulse": False,      # Impulse drive
        "environment": False,  # Air-exchangers, etc
        "medical": False,
        "lrsensors": False,   # Long-range sensors
        "srsensors": False,   # Short-range sensors
    }

    repair_times = {
        "shields": 0,      # Shield emitters
        "phasers": 0,      # Phaser arrays
        "torps": 0,        # Photon torpedo launching systems
        "warp": 0,         # Warp drive
        "impulse": 0,      # Impulse drive
        "environment": 0,  # Air-exchangers, etc
        "medical": 0,
        "lrsensors": 0,   # Long-range sensors
        "srsensors": 0,   # Short-range sensors
    }

    def __init__(self, galaxy: list) -> None:
        super().__init__()
        # Put initialization code here if necessary.
        self.galaxy = galaxy
        self.galaxy[self.location[3]][self.location[2]].EnterEnterprise(True)

    def ChangeShieldEnergy(self):
        if self.damage['shields'] == False:  # Check to see if the shields are damaged.
            amount = cin("How much energy would you like to transfer to shields?", float)
            if 0 <= self.shield_energy + amount <= 200:
                self.shield_energy += amount
            else:
                print("I'm sorry, but the shields can't take that amount of energy.")
            print("\n")
        else:
            print("I'm sorry sir, but the shield emitters are fused; I cannot do anything until they are repaired.")
        

    def ChangeShieldStatus(self) -> int:
        if self.damage['shields'] == False:
            which = cin("To turn the shields on, type <1>.\nTo turn them off, type <2>.")
            if which == '0':
                self.shield_status = False
                print("Shields are disabled.\n")
                return 0
            elif which == '1':
                self.shield_status = True
                print("Shields are up.\n")
                return 0
            else:
                print("Sir? I do not understand what you are saying.\n")
                return 1
        else:
            print("I'm sorry sir, but the shield emitters are fused; I cannot do anything until they are repaired.\n")
            return 1

    def GetDamage(self) -> None:
        '''
        Outputs a list of repair times for different parts of the Enterprise.
        '''
        
        output = f"""
Department               Repair time
-------------------------------------
Shields:                     {self.repair_times['shields']}
Phasers:                     {self.repair_times['phasers']}
Torpedoes:                   {self.repair_times['torps']}
Warp Drive:                  {self.repair_times['warp']}
Impulse Drive:               {self.repair_times['impulse']}
Life Support:                {self.repair_times['environment']}
Med-bay:                     {self.repair_times['medical']}
Long-Range Sensors:          {self.repair_times['lrsensors']}
Short-Range Sensors:         {self.repair_times['srsensors']}
        """  # Oh, how I love f-strings!
        print(output)
        return None

    def SrScan(self):
        for i in range(10): # Iterate through the quadrant.
            self.galaxy[self.location[3]][self.location[2]].SrPrintout(i)

            if i == 0:
                print(" >                Status                <")
            elif i == 1:
                print(" ----------------------------------------")
            elif i == 2:
                print(f" | Energy:    {self.energy}")
            elif i == 3:
                print(f" | Torpedoes: {self.torpedoes}")
            elif i == 4:
                print(f" | Shields:   {('Down' if self.shield_status == False else 'Up')}, {self.shield_energy} energy remaining.")
            elif i == 6:  # Not a typo
                print(f" | Location: Sector ({self.location[0]},{self.location[1]}) of quadrant ({self.location[2]},{self.location[3]})")
            else:
                print(" | ")

    def LrScan(self):
        pass  # Complete this sometime else.
    
    def Move(self):
        movement_type = cin("Manuevering [0] or Long-Range [1]?", "int")
        if -1 < movement_type < 2:
            nav_type = cin("Would you like to use the Autopilot [0], or do you want to manually pilot the ship [1]?", 'int')
            if not -1 < nav_type < 2:
                print("Sir, that is not a valid method of navigation.")
                return
        elif movement_type >= 2:
            print("I'm sorry sir, but the Enterprise is not equipped for intergalactic travel.")
        else:
            print("Sir, you aren't making any sense.")
        
        if nav_type == 0:
            unprocessed_destination = cin("Please input the destination coordinates.", 'str')
            semiprocessed_destination = unprocessed_destination.split(' ')
            destination = []
            for i in semiprocessed_destination:
                destination.append(int(i))
            x1 = destination[0]
            y1 = destination[1]
        else:
            x_disp = cin("X-displacement:", 'int')
            y_disp = cin("Y-displacement:", 'int')
            x1 = self.location[0] + x_disp
            y1 = self.location[1] + y_disp
            

if __name__ == "__main__":
    from Quadrant import Quadrant
    quadrants = [[Quadrant() for i in range(10)] for j in range(10)]
    test = Enterprise(quadrants)
    test.damage['shields'] = True
    test.ChangeShieldStatus()
    test.repair_times['shields'] = 3.2
    test.GetDamage()
    test.SrScan()
    test.Move()
    print()
