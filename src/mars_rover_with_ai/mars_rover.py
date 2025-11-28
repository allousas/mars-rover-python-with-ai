from dataclasses import dataclass


class MarsRover:
    @property
    def position(self):
        return Position(0, 0, 'N')

    def execute(self, command: str):
        raise NotImplementedError()


@dataclass
class Position:
    x: int
    y: int
    direction: str

