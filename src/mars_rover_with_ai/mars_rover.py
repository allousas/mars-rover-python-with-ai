from dataclasses import dataclass


class MarsRover:
    def __init__(self):
        self._position = Position(0, 0, 'N')

    @property
    def position(self):
        return self._position

    def execute(self, command: str):
        if command == 'f':
            self._position = self._position.move_forward()


@dataclass
class Position:
    x: int
    y: int
    direction: str

    def move_forward(self):
        if self.direction == 'N':
            return Position(self.x, self.y + 1, self.direction)
        return self

