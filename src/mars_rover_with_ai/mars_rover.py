from typing import List
from mars_rover_with_ai.position import Position
from mars_rover_with_ai.map import Map, InvalidMap


class MarsRover:
    def __init__(self, grid_map: List[str]):
        self._map = Map(grid_map)
        self._position: Position = self._map.find_initial_position()

    @property
    def position(self):
        return self._position

    @property
    def grid_map(self):
        return self._map.grid_map
