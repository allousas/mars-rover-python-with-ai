from dataclasses import dataclass
from enum import Enum


class MarsRover:
    def __init__(self):
        self._position = Position(0, 0, Direction.N)

    @property
    def position(self):
        return self._position

    def execute(self, command: str):
        if command == 'f':
            self._position = self._position.move_forward()


class Direction(Enum):
    N = 'N'
    S = 'S'
    E = 'E'
    W = 'W'


@dataclass
class Position:
    x: int
    y: int
    direction: Direction

    def move_forward(self):
        if self.direction == Direction.N:
            return Position(self.x, self.y + 1, self.direction)
        return self

