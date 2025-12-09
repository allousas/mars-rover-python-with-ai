from typing import List, ClassVar, Dict, Set
import regex
from mars_rover_with_ai.position import Position, Direction


class Map:
    _DIRECTION_MARKERS: ClassVar[Dict[str, Direction]] = {
        '➡️': Direction.E,
        '⬅️': Direction.W,
        '⬆️': Direction.N,
        '⬇️': Direction.S,
    }
    _ALLOWED_TILES: ClassVar[Set[str]] = {'🟩', '🌳', '🟫', '🪨'} | set(_DIRECTION_MARKERS.keys())
    _GRAPHEME_RE: ClassVar = regex.compile(r"\X")

    def __init__(self, grid_map: List[str]):
        self._grid_map: List[str] = grid_map
        self._validate()

    @property
    def grid_map(self) -> List[str]:
        return self._grid_map

    def _graphemes(self, row: str) -> List[str]:
        return Map._GRAPHEME_RE.findall(row)

    def _validate(self) -> None:
        grapheme_rows = [self._graphemes(row) for row in self._grid_map]
        lengths = {len(r) for r in grapheme_rows}
        if len(lengths) != 1:
            raise InvalidMap("invalid size")
        marker_found = False
        for r in grapheme_rows:
            unknown = set(r) - Map._ALLOWED_TILES
            if unknown:
                bad = next(iter(unknown))
                raise InvalidMap(f"unrecognized land char: {bad}")
            if not marker_found and any(g in Map._DIRECTION_MARKERS for g in r):
                marker_found = True
        if not marker_found:
            raise InvalidMap("invalid map: initial position marker not found")

    def find_initial_position(self) -> Position:
        for y, row in enumerate(self._grid_map):
            graphemes = self._graphemes(row)
            for x, g in enumerate(graphemes):
                if g in Map._DIRECTION_MARKERS:
                    return Position(x, y, Map._DIRECTION_MARKERS[g])
        raise InvalidMap("invalid map: initial position marker not found")


class InvalidMap(Exception):
    pass
