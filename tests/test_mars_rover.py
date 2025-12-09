from mars_rover_with_ai.mars_rover import MarsRover
from mars_rover_with_ai.position import Position, Direction

N, E, S, W = Direction.N, Direction.E, Direction.S, Direction.W


def test_should_initialise_with_an_initial_position_and_a_map():
    grid_map = [
        '🟩🟩🌳🟩🟩',
        '🟩🟩🟩🟩🟩',
        '🟩🟩🟩🌳🟩',
        '➡️🟩🟩🟩🟩'
    ]
    expected_position = Position(0, 3, E)

    rover = MarsRover(grid_map=grid_map)

    assert rover.position == expected_position
    assert rover.grid_map == grid_map


def test_should_execute_list_of_commands():
    grid_map = [
        '🟩🟩🟩🟩',
        '🟩🟩🟩🟩',
        '🟩🟩🟩🟩',
        '⬆️🟩🟩🟩'
    ]
    rover = MarsRover(grid_map=grid_map)

    rover.execute('➡️⬆️⬅️') # turn right, move forward, turn left

    assert rover.position == Position(1, 3, N)


def test_should_not_move_when_encountering_obstacle():
    grid_map = [
        '🟩🟩🟩',
        '🟩🌳🟩',
        '⬆️🟩🟩'
    ]
    rover = MarsRover(grid_map=grid_map)

    rover.execute('⬆️➡️⬆️') # move forward, turn right, move forward into obstacle

    assert rover.position == Position(0, 1, E)
