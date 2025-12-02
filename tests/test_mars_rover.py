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
        '🟩🧱🟩🟩🟩',  # Unrecognized land character 🧱
        '🟩🟩🟩🌳🟩',
        '➡️🟩🟩🟩🟩'
    ], "unrecognized land char")
])
def test_should_fail_when_map_is_invalid(grid_map, expected_message_fragment):
    with pytest.raises(InvalidMap) as exc:
        MarsRover(grid_map=grid_map)
    assert expected_message_fragment in str(exc.value)
