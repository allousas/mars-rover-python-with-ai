from typing import List
from mars_rover_with_ai.position import Position


class MarsRover:
    def __init__(self, position: Position, grid_map: List[str]):
        self._position: Position = position
        self._grid_map: List[str] = grid_map

    @property
    def position(self):
        return self._position

    @property
    def grid_map(self):
        return self._grid_map

