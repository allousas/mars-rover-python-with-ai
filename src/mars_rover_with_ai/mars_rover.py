class Position:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def __eq__(self, other):
        if not isinstance(other, Position):
            return False
        return self.x == other.x and self.y == other.y and self.direction == other.direction


class MarsRover:
    @property
    def position(self):
        return Position(1, 1, 'S')  # Wrong values to make test fail
