import random

class Torpedo(object):
    def __init__(self):
        return None

class MakeUniverse(object):
    klingons = random.randint(50, 80)
    starbases = random.randint(3, 5)

    universe = [[0 for _ in range(10)] for _ in range(10)]

    def __init__(self):
        self.make_stars()
        self.make_klingons()
        self.make_starbases()
    
    def make_stars(self):
        pass
    
    def make_klingons(self):
        pass

    def make_starbases(self):
        pass

class Damage(object):
    life_support = None
    damage_control = None
    sick_bay = None
    torps = None
    warp = None
    impulse = None
    phasers = None
    computer = None
    sr_sensors = None
    lr_sensors = None
    shields = None
    plasma_conduits = None

    def __init__(self):
        return None
    
    def add_damage(self, severity: int):
        if severity == 0: # Shields are up
            amount = random.randint(0, 10)
            if amount == 10:
                which_ones = random.randint(1, 12)
                self._do_add([which_ones])
        
        elif severity == 1: # Shields are down
            amount = random.randint(0, 5)
            if (amount == 4) or (amount == 5):
                which_ones = []
                for i in range(random.randint(0, 3)):
                    which_ones.append(random.randint(0, 12))
                self._do_add(which_ones)

        elif severity == 2:  # Collision
            amount = random.randint(3, 8) # A collision is guaranteed to generate damage, so no "zero damage" event is possible.
            which_ones = []
            for i in range(amount):
                which_ones.append(random.randint(0, 12))
            self._do_add(which_ones)
    
    def _do_add(self, to_do: list):
        print("*ALERT! ALERT! DAMAGE INCURRED!*")
        for damage in to_do:
            if damage == 1:
                self.life_support = self.days()
                self.alert("Life support")
            elif damage == 2:
                self.damage_control == self.days()
                self.alert("Damage")
            elif damage == 3:
                self.sick_bay = self.days()
                self.alert("Sick Bay")
            elif damage == 4:
                self.torps = self.days()
                self.alert("Torpedo tubes")
            elif damage == 5:
                self.warp = self.days()
                self.alert("Warp Drive")
            elif damage == 6:
                self.impulse = self.days()
                self.alert("Impulse Drive")
            elif damage == 7:
                self.phasers = self.days()
                self.alert("Phasers")
            elif damage == 8:
                self.computer = self.days()
                self.alert("Main Computer")
            elif damage == 9:
                self.sr_sensors = self.days()
                self.alert("Short-Range Sensors")
            elif damage == 10:
                lr_sensors = self.days()
                self.alert("Long-Range Sensors")
            elif damage == 11:
                shields = self.days()
                self.alert("Shield Generators")
            elif damage == 12:
                plasma_conduits = self.days()
                self.alert("Plasma Conduits")

    def alert(self, name):
        print(f"\t- {name}")
        return

class Enterprise(object):
    energy = 3000
    torps = 5
    deutronium = 0
    damage = Damage()

    def __init__ (self, location: list):
        return None
