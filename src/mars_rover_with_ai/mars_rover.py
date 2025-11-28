from dataclasses import dataclass
from enum import Enum


class MarsRover:
    def __init__(self, position=None):
        self._position = position if position is not None else Position(0, 0, N)

    @property
    def position(self):
        return self._position

    def execute(self, command: str):
        if command == 'f':
            self._position = self._position.move_forward()
        elif command == 'r':
            self._position = self._position.turn_right()


class Direction(Enum):
    N = 'N'
    S = 'S'
    E = 'E'
    W = 'W'


N, E, S, W = Direction.N, Direction.E, Direction.S, Direction.W


@dataclass
class Position:
    x: int
    y: int
    direction: Direction

    def move_forward(self):
        if self.direction == N:
            return Position(self.x, self.y + 1, self.direction)
        elif self.direction == E:
            return Position(self.x + 1, self.y, self.direction)
        elif self.direction == S:
            return Position(self.x, self.y - 1, self.direction)
        return self

    def turn_right(self):
        if self.direction == N:
            return Position(self.x, self.y, E)
        return self

