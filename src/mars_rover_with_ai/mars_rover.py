from dataclasses import dataclass


class MarsRover:
    @property
    def position(self):
        return Position(0, 0, 'N')


@dataclass
class Position:
    x: int
    y: int
    direction: str

