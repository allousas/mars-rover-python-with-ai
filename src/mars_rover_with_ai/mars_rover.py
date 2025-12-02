from typing import List
from mars_rover_with_ai.position import Position


class MarsRover:
    def __init__(self, position: Position, grid_map: List[str]):
        self._validate_map(grid_map)
        self._position: Position = position
        self._grid_map: List[str] = grid_map

    @staticmethod
    def _validate_map(grid_map: List[str]):
        if not grid_map or len(set(len(row) for row in grid_map)) != 1:
            raise InvalidMap("invalid size")

    @property
    def position(self):
        return self._position

    @property
    def grid_map(self):
        return self._grid_map


class InvalidMap(Exception):
    pass
