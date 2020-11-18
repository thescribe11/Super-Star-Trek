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


class Upcoming:
    """
    Buffer for upcoming events
    """

    def __init__(self, *args, **kwargs):
        self.upcoming_input = []

    def get(self) -> str or None:
        """
        Return the top element in the event stack
        """
        try:
            return self.upcoming_input.pop()
        except IndexError:
            return None

    def add(self, incoming):
        """
        Add an element to the stack
        """
        assert isinstance(incoming, str)
        self.upcoming_input.append(incoming)
