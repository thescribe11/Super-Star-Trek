import random

class Quadrant(object):
    '''
    Defines a Quadrant in the Galaxy.

    Public variables:
    - klingons
    - starbases
    - stars

    Public functions:
    - LrPrintout(), pretty-prints public variables for use in the <lrscan> command.
    - SrPrintout(), pretty-prints quadrant for use in the <srs> command.
    - GetContents(which_one), returns the number of <which_one>s in the quadrant.
    - SetStarbase(), sets $starbases to True.
    '''

    def __init__(self):
        super().__init__()

        testing = False  # Disable for production code; this is a testing feature.

        self.klingons = random.randint(0, 6)
        self.starbase = (1 if ((random.randint(0,10) == 10) or testing == True) else 0)
        self.stars = random.randint(0, 10)
        
        self._black_holes = random.randint(0, 3)  # Number of black holes in quadrant. Private variable, should never be used by another class.

        self.is_known = False
        self.contents = [   # A "map" of the Quadrant.
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

        i = 0
        while i < self.klingons: # Make the Klingons.
            i += 1
            if self.contents[(x := random.randint(0, 9))][(y := random.randint(0, 9))] == '.':  #Oh, how I love the new Walrus Operator!
                self.contents[x][y] = 'K'
            else:
                i -= 1

        i = 0
        while i < self.starbase:  # Place starbase (if applicable)
            if self.contents[(x := random.randint(0, 9))][(y := random.randint(0, 9))] == '.':
                self.contents[x][y] = 'S'
                break

        i = 0
        while i < self.stars:  # Produce some stars...
            i += 1
            if self.contents[(x := random.randint(0, 9))][(y := random.randint(0, 9))] == '.':
                self.contents[x][y] = '*'
            else:
                i -= 1

    def EnterEnterprise(self, is_present: bool):
        '''
        Put the Enterprise in a quadrant.
        '''
        placed = False
        while placed != True:
            if self.contents[(x := random.randint(0, 9))][(y := random.randint(0, 9))] == '.':
                self.contents[x][y] = 'E'
                break
        return None
        
    def GetContents(self, which: str):
        self.LrPrintout()

        return {
            "klingons": self.klingons,
            "starbase": self.starbase,
            "stars": self.stars
        }[which]

    def LrPrintout(self):
        print(f"{self.klingons}{self.starbase}{self.stars}")

    def SrPrintout(self, row):
            for thing in self.contents[row]:
                print(thing + " ", end="")

    def CheckIsEmpty(self, x, y):
        if self.contents[int(y)][x] == '.':
            return True
        else:
            return False

    def SetObject(self, objecter, x, y):
        self.contents[int(y)][x] = objecter
        

if __name__ == "__main__":
    test = Quadrant()
    test.GetContents("klingons")
    test.SrPrintout(0)
    test.SrPrintout(1)
    test.SrPrintout(2)
    test.SrPrintout(3)
    test.SrPrintout(4)
    test.SrPrintout(5)
    test.SrPrintout(6)
    test.SrPrintout(7)
    test.SrPrintout(8)
    test.SrPrintout(9)
