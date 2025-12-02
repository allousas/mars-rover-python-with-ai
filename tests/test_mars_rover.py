import pytest
from mars_rover_with_ai.mars_rover import MarsRover, InvalidMap
from mars_rover_with_ai.position import Position, Direction

N, E, S, W = Direction.N, Direction.E, Direction.S, Direction.W


@pytest.mark.parametrize("initial_position,grid_map", [
    (Position(0, 4, E), [
        '🟩🟩🌳🟩🟩',
        '🟩🟩🟩🟩🟩',
        '🟩🟩🟩🌳🟩',
        '➡️🟩🟩🟩🟩'
    ]),
    (Position(0, 4, N), [
        '🟫🟫🪨🟫🟫',
        '🟫🟫🟫🟫🟫',
        '🟫🟫🟫🟫🟫',
        '⬆️🟫🟫🟫🟫'
    ])
])
def test_should_initialise_with_an_initial_position_and_a_map(initial_position, grid_map):
    rover = MarsRover(position=initial_position, grid_map=grid_map)

    assert rover.position == initial_position
    assert rover.grid_map == grid_map


def test_should_fail_with_invalid_map_size():
    bad_grid_map = [
        '🟩🟩🌳',
        '🟩🟩🟩🟩',
    ]
    initial_position = Position(0, 0, N)
    try:
        MarsRover(position=initial_position, grid_map=bad_grid_map)
        assert False, "Expected InvalidMap due to invalid map size, but none was raised."
    except InvalidMap as e:
        assert "invalid size" in str(e)
