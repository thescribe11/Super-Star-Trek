class Klingon(object):
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    def __str__(self, *args):
        return f"Vert: {self.y}, Horiz: {self.x}, Health: {self.health}"

    def is_at(self, vert, horiz):
        if self.y == vert and self.x == horiz:
            return True
        else:
            return False

        raise NotImplementedError("This should not be called!")
