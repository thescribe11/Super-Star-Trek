class Klingon(object):
    def __init__(self, **kwds):
        self.__dict__.update(kwds)
    def __str__(self, *args):
        return f"Vert: {self.y}, Horiz: {self.x}, Health: {self.health}"