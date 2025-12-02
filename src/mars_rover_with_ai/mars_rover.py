from typing import List, ClassVar, Dict, Set
from mars_rover_with_ai.position import Position, Direction
import regex


class MarsRover:
    _DIRECTION_MARKERS: ClassVar[Dict[str, Direction]] = {
        '➡️': Direction.E,
        '⬅️': Direction.W,
        '⬆️': Direction.N,
        '⬇️': Direction.S,
    }
    _ALLOWED_TILES: ClassVar[Set[str]] = {'🟩', '🌳', '🟫', '🪨'} | set(_DIRECTION_MARKERS.keys())

    def __init__(self, grid_map: List[str]):
        self._validate_map(grid_map)
        self._grid_map: List[str] = grid_map
        self._position: Position = self._extract_position_from_map(grid_map)

    @staticmethod
    def _graphemes(row: str) -> List[str]:
        return regex.findall(r"\X", row)

    @staticmethod
    def _validate_map(grid_map: List[str]):
        grapheme_rows = [MarsRover._graphemes(row) for row in grid_map]
        lengths = {len(r) for r in grapheme_rows}
        if len(lengths) != 1:
            raise InvalidMap("invalid size")
        for r in grapheme_rows:
            unknown = set(r) - MarsRover._ALLOWED_TILES
            if unknown:
                bad = next(iter(unknown))
                raise InvalidMap(f"unrecognized land char: {bad}")

    @staticmethod
    def _extract_position_from_map(grid_map: List[str]) -> Position:
        for y, row in enumerate(grid_map):
            graphemes = MarsRover._graphemes(row)
            try:
                x, g = next((idx, g) for idx, g in enumerate(graphemes) if g in MarsRover._DIRECTION_MARKERS)
                return Position(x, y, MarsRover._DIRECTION_MARKERS[g])
            except StopIteration:
                continue
        raise InvalidMap("invalid map: initial position marker not found")

    @property
    def position(self):
        return self._position

    @property
    def grid_map(self):
        return self._grid_map


class InvalidMap(Exception):
    pass
