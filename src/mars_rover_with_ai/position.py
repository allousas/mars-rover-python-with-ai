from dataclasses import dataclass
from enum import Enum
from typing import ClassVar, Dict, Tuple


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

    _FORWARD_MOVEMENTS: ClassVar[Dict[Direction, Tuple[int, int]]] = {
        Direction.N: (0, -1),
        Direction.E: (1, 0),
        Direction.S: (0, 1),
        Direction.W: (-1, 0)
    }

    _RIGHT_TURNS: ClassVar[Dict[Direction, Direction]] = {
        Direction.N: Direction.E,
        Direction.E: Direction.S,
        Direction.S: Direction.W,
        Direction.W: Direction.N
    }
    _LEFT_TURNS: ClassVar[Dict[Direction, Direction]] = {
        Direction.N: Direction.W,
        Direction.W: Direction.S,
        Direction.S: Direction.E,
        Direction.E: Direction.N
    }

    def move_forward(self):
        dx, dy = self._FORWARD_MOVEMENTS[self.direction]
        return Position(self.x + dx, self.y + dy, self.direction)

    def turn_right(self):
        return Position(self.x, self.y, self._RIGHT_TURNS[self.direction])

    def turn_left(self):
        return Position(self.x, self.y, self._LEFT_TURNS[self.direction])

