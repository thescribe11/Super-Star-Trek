from dataclasses import dataclass
import enum


class Klingon(object):
    def __init__(self, x, y, health):
        """
        Behold! A Klingon() is born!
        """
        self.x = x
        self.y = y
        self.health = health

    def __str__(self, *args):
        return f"Vert: {self.y}, Horiz: {self.x}, Health: {self.health}"

    def is_at(self, vert, horiz):
        if self.y == vert and self.x == horiz:
            return True
        else:
            return False


class CommandKind(enum.Enum):
    Error = -1
    Shield = 1
    Srscan = 2
    Lrscan = 3
    Torpedo = 4
    Phaser = 5
    Move = 6
    SelfDestruct = 7
    Rest = 8
    Damage = 9
    Score = 10
    ImprobGun = 11
    Chart = 12
    Number = 13


class Reason(enum.Enum):
    NegativeSpaceWedgie = -1  # Warning: Usage of the Improbability Cannon may result insanity-causing Alien Geometries
    Kaboom = 0  # The Enterprise has been blown up
    Tribble = 1  # The Enterprise is filled with Tribbles
    Stranded = 2  # You have been stranded on a planet.
    TimeUp = 3  # The Enterprise is out of time
    NoAir = 4  # The life support reserves have run out
    NoGas = 5  # The Enterprise has run out of fuel
    Transformation = 6  # The Enterprise's crew, excepting Mr. Spock, have been transformed into brutish abominations.
    Borg = 7  # We are the Borg. You will be assimilated. Resistance is futile.
    Dalek = 8  # EXTERMINATE!!!!
    EventHorizon = 9  # The Enterprise is crushed in a black hole
    SelfDestruct = 10  # The self destruct has finished its countdown
    SpecialSelfDestruct = 11  # Goodbye, cruel world!
    TooManyLeaveAttempts = 12  # You can't leave now!


class Mode(enum.Enum):
    Manual = 1
    Auto = 2


@dataclass()
class Shields:
    subtype: str or None = None
    amount: float or None = None
    new_status: bool or None = None


@dataclass()
class Torpedo:
    number: int or None = None
    directions: list or None = None


@dataclass()
class Movement:
    mode: Mode or None = None
    disp1: int or None = None
    disp2: int or None = None


@dataclass()
class SrScan:
    pass


@dataclass()
class LrScan:
    pass


@dataclass()
class Phasers:
    mode: Mode or None = None
    power: int or None = None
    targets: list or None = None


class KlingonsRespond:
    def __init__(self):
        pass


@dataclass()
class Decision:
    which: str = 'n'


@dataclass()
class Die:
    reason: Reason


class Upcoming:
    """
    Buffer for upcoming events
    """

    def __init__(self, *args, **kwargs):
        self._upcoming_input = []

    def get(self) -> str or None:
        """
        Return the top element in the event stack
        """
        try:
            return self._upcoming_input.pop(0)
        except IndexError:
            return None

    def scan(self) -> str or None:
        """
        Return the top element in the event stack, without removing it
        """
        try:
            return self._upcoming_input[0]
        except IndexError:
            return None

    def add(self, incoming):
        """
        Add an element to the stack
        """
        self._upcoming_input.append(incoming)

    def clear(self):
        """
        Remove all (or most, depending on whether or not I implement commanders) of the elements in self.upcoming_input
        """
        self._upcoming_input.clear()
