from mars_rover_with_ai.mars_rover import MarsRover
from mars_rover_with_ai.position import Position, Direction

N, E, S, W = Direction.N, Direction.E, Direction.S, Direction.W


def test_should_initialise_with_an_initial_position_and_a_map():
    grid_map = [
        '🟩🟩🌳🟩🟩',
        '🟩🟩🟩🟩🟩',
        '🟩🟩🟩🌳🟩',
        '🟩🌳🟩🟩🟩',
        '🟩🟩🟩🟩🟩'
    ]
    initial_position = Position(0, 4, E)
    rover = MarsRover(position=initial_position, grid_map=grid_map)

    assert rover.position == initial_position
    assert rover.grid_map == grid_map
