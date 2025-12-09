from typing import List, Set
from mars_rover_with_ai.position import Position
from mars_rover_with_ai.map import Map, InvalidMap
import regex


class MarsRover:
    OBSTACLES: Set[str] = {'🌳', '🪨'}

    def __init__(self, grid_map: List[str]):
        self._map = Map(grid_map)
        self._position: Position = self._map.find_initial_position()

    def _is_obstacle_at(self, position: Position) -> bool:
        if position.y < 0 or position.y >= len(self._map.grid_map):
            return True
        row = self._map.grid_map[position.y]
        graphemes = regex.findall(r"\X", row)
        if position.x < 0 or position.x >= len(graphemes):
            return True
        tile = graphemes[position.x]
        return tile in self.OBSTACLES

    def execute(self, commands: str) -> None:
        graphemes = regex.findall(r"\X", commands)
        for cmd in graphemes:
            if cmd == '➡️':
                self._position = self._position.turn_right()
            elif cmd == '⬆️':
                next_position = self._position.move_forward()
                if not self._is_obstacle_at(next_position):
                    self._position = next_position
            elif cmd == '⬅️':
                self._position = self._position.turn_left()

    @property
    def position(self):
        return self._position

    @property
    def grid_map(self):
        return self._map.grid_map
