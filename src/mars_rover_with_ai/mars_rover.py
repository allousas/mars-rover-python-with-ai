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
        elif command == 'l':
            self._position = self._position.turn_left()


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

    _FORWARD_MOVEMENTS = {
        N: (0, 1),
        E: (1, 0),
        S: (0, -1),
        W: (-1, 0)
    }

    _RIGHT_TURNS = {N: E, E: S, S: W, W: N}
    _LEFT_TURNS = {N: W, W: S, S: E, E: N}

    def move_forward(self):
        dx, dy = self._FORWARD_MOVEMENTS[self.direction]
        return Position(self.x + dx, self.y + dy, self.direction)

    def turn_right(self):
        return Position(self.x, self.y, self._RIGHT_TURNS[self.direction])

    def turn_left(self):
        return Position(self.x, self.y, self._LEFT_TURNS[self.direction])

