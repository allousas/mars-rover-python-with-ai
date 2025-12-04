import pytest
from mars_rover_with_ai.map import Map, InvalidMap
from mars_rover_with_ai.position import Position, Direction

N, E, S, W = Direction.N, Direction.E, Direction.S, Direction.W


def test_map_should_find_initial_position_north():
    grid_map = [
        '🟫🟫🪨🟫🟫',
        '🟫🟫🟫🟫🟫',
        '🟫🟫🟫🟫🟫',
        '⬆️🟫🟫🟫🟫'
    ]
    m = Map(grid_map)
    assert m.find_initial_position() == Position(0, 3, N)


@pytest.mark.parametrize("grid_map, expected_message_fragment", [
    ([
        '🟩🟩🌳',
        '🟩🟩🟩🟩',
    ], "invalid size"),
    ([
        '🟩🟩🌳🟩🟩',
        '🟩🟩🟩🟩🟩',
        '🟩🟩🟩🌳🟩',
        '🟩🌳🟩🟩🟩'
    ], "initial position marker not found"),
    ([
        '🟩🟩🌳🟩🟩',
        '🟩🧱🟩🟩🟩',
        '🟩🟩🟩🌳🟩',
        '➡️🟩🟩🟩🟩'
    ], "unrecognized land char")
])
def test_map_should_fail_when_invalid(grid_map, expected_message_fragment):
    with pytest.raises(InvalidMap) as exc:
        Map(grid_map)
    assert expected_message_fragment in str(exc.value)

