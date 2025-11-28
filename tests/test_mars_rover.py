import pytest
from mars_rover_with_ai.mars_rover import MarsRover, Position, Direction

N, E, S, W = Direction.N, Direction.E, Direction.S, Direction.W


def test_should_initialize_at_default_position():
    rover = MarsRover()
    position = rover.position

    assert position == Position(0, 0, N)


@pytest.mark.parametrize("initial_position, expected_position", [
    (Position(0, 0, N), Position(0, 1, N)),
    (Position(0, 0, E), Position(1, 0, E)),
    (Position(0, 0, S), Position(0, -1, S)),
])
def test_should_move_forward(initial_position, expected_position):
    rover = MarsRover(position=initial_position)
    rover.execute(command='f')

    assert rover.position == expected_position


def test_should_turn_right():
    rover = MarsRover()
    rover.execute(command='r')

    assert rover.position == Position(0, 0, E)



