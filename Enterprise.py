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

def Slope(x1: int, y1: int, x2: int, y2: int) -> float:
    try:
        return (float)(y2 - y1) / (x2 - x1)
    except ZeroDivisionError:
        return None  

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

    location = {               # Represents the Enterprise's current location
        'sx': random.randint(0, 9),  # Sector x
        'sy': random.randint(0, 9),  # Sector y
        'qx': random.randint(0, 7),  # Quadrant x
        'qy': random.randint(0, 7)   # Quadrant y
    }
    
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
        self.galaxy[self.location['qy']][self.location['qx']].SetObject('E', self.location['sx'], self.location['sy'])

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
        print("┌─────────────────────────┐")
        print("│    1 2 3 4 5 6 7 8 9 10 │")
        for i in range(10):  # Iterate through the quadrant.
            print("│ ", end="")
            print(i + 1, end="")
            if i < 9:
                print("  ", end="")
            else:
                print(" ", end="")

            self.galaxy[self.location['qy']][self.location['qx']].SrPrintout(i)

            # And this is when I wish that Python had switch-case statements...
            if i == 0:
                print(" │ >                Status                <")
            elif i == 1:
                print(" │ ----------------------------------------")
            elif i == 2:
                print(f" │ Energy:    {self.energy}")
            elif i == 3:
                print(f" │ Torpedoes: {self.torpedoes}")
            elif i == 4:
                print(f" │ Shields:   {('Down' if self.shield_status == False else 'Up')}, {self.shield_energy} energy remaining.")
            elif i == 6:  # Not a typo
                print(f" │ Location: Sector ({self.location['sx']+1},{int(self.location['sy']+1)}) of quadrant ({self.location['qx']+1},{self.location['qy']+1})")
            else:
                print(" │ ")
        print("└─────────────────────────┘")

    def LrScan(self):
        pass  # Complete this sometime else.
    
    def Move(self):
        movement_type = cin("Impulse [0] or Warp [1]?", "int")
        if movement_type >= 2:
            print("I'm sorry sir, but the Enterprise is not equipped for intergalactic travel.")
        elif movement_type < 0:
            print("Sir, you aren't making any sense.")
        
        raw_displacement = cin("Please enter x and y displacement.", "str").split(' ')
        semiprocessed_displacement = [i for i in raw_displacement if i != " "]
        x_disp = int(semiprocessed_displacement[0])
        y_disp = int(semiprocessed_displacement[1])
        x2 = self.location['sx'] + x_disp
        y2 = self.location['sy'] + y_disp

        slope = Slope(self.location['sx'], self.location['sy'], x2, y2)
        if slope is None:
            slope = y_disp
        if movement_type == 0:
            self.Manuever(x_disp, slope)
        else:
            self.InterQuadrantTravel()

    def Manuever(self, xdisp: int, slope: float):
        '''
        In-quadrant moevement.
        '''

        if xdisp != 0: # To avoid wonkiness
            for i in range(0, xdisp, (1 if xdisp > 1 else - 1)):
                new_x = self.location['sx'] + (1 if xdisp > 1 else - 1)          # New x pos
                new_y = self.location['sy'] + (slope if xdisp > 1 else (-slope))  # New y pos
                
                if (new_y < 0) or (new_x < 0):
                    print("I'm sorry sir, but we can't leave the quadrant on impulse drive.")
                    break

                if (emptiness := self.galaxy[self.location['qy']][self.location['qx']].CheckIsEmpty(new_x, new_y)) == True: # Check to see if sector is uninhabited
                    self.galaxy[self.location['qy']][self.location['qx']].SetObject('E', new_x, new_y)  # Update the quadrant
                    self.galaxy[self.location['qy']][self.location['qx']].SetObject('.', self.location['sx'], self.location['sy'])
                    self.location['sx'] = new_x; self.location['sy'] = new_y  # Change the Enterprise's location

                    self.energy -= (1 + abs(slope)) * (random.randint(5, 8))
                elif emptiness == False:
                    self.EmergencyStop()
                    break
                else:
                    print("I'm sorry sir, but we can't leave the quadrant on impulse drive.")
                    break
        else:
            for i in  range(0, int(slope), (1 if int(slope) > 1 else - 1)):
                new_y = self.location['sy'] + (1 if int(slope) > 1 else - 1)
                if self.galaxy[self.location['qy']][self.location['qx']].CheckIsEmpty(self.location['sx'], new_y) == True:
                    self.galaxy[self.location['qy']][self.location['qx']].SetObject('E', self.location['sx'], new_y)
                    self.galaxy[self.location['qy']][self.location['qx']].SetObject('.', self.location['sx'], self.location['sy'])
                    self.location['sy'] = new_y
                else:
                    self.EmergencyStop()
                    break
        return
    
    def EmergencyStop(self):
        cost = random.randint(200, 350)
        if self.energy > cost:
            print(f"""**ALERT OBJECT DETECTED**\n**EMERGENCY STOP**\n\nEmergency stop costs {cost} energy.""")
        else:
            self.is_alive = False
            self.GameOver()

    def GameOver(self):
        pass

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
    test.SrScan()
    print()
