import pytest
from mars_rover_with_ai.mars_rover import MarsRover, InvalidMap
from mars_rover_with_ai.position import Position, Direction

N, E, S, W = Direction.N, Direction.E, Direction.S, Direction.W


@pytest.mark.parametrize("grid_map, expected_position", [
    ([
        '🟩🟩🌳🟩🟩',
        '🟩🟩🟩🟩🟩',
        '🟩🟩🟩🌳🟩',
        '➡️🟩🟩🟩🟩'
    ], Position(0, 3, E)),
    ([
        '🟫🟫🪨🟫🟫',
        '🟫🟫🟫🟫🟫',
        '🟫🟫🟫🟫🟫',
        '⬆️🟫🟫🟫🟫'
    ], Position(0, 3, N))
])
def test_should_initialise_with_an_initial_position_and_a_map(grid_map, expected_position):
    rover = MarsRover(grid_map=grid_map)

    assert rover.position == expected_position
    assert rover.grid_map == grid_map


def test_should_fail_with_invalid_map_size():
    bad_grid_map = [
        '🟩🟩🌳',
        '🟩🟩🟩🟩',
    ]
    try:
        MarsRover(grid_map=bad_grid_map)
        assert False, "Expected InvalidMap due to invalid map size, but none was raised."
    except InvalidMap as e:
        assert "invalid size" in str(e)
