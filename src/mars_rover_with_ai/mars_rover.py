from typing import List
from mars_rover_with_ai.position import Position
from mars_rover_with_ai.map import Map, InvalidMap
import regex


class MarsRover:
    def __init__(self, grid_map: List[str]):
        self._map = Map(grid_map)
        self._position: Position = self._map.find_initial_position()

    def execute(self, commands: str) -> None:
        graphemes = regex.findall(r"\X", commands)
        for cmd in graphemes:
            if cmd == '➡️':
                self._position = self._position.turn_right()
            elif cmd == '⬆️':
                next_position = self._position.move_forward()
                if not self._map.is_obstacle_at(next_position):
                    self._position = next_position
            elif cmd == '⬅️':
                self._position = self._position.turn_left()

    @property
    def position(self):
        return self._position

