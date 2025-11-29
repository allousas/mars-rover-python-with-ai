from mars_rover_with_ai.mars_rover import MarsRover
from mars_rover_with_ai.position import Position, Direction

N, E, S, W = Direction.N, Direction.E, Direction.S, Direction.W


def test_should_initialize_at_default_position():
    rover = MarsRover()
    position = rover.position

    assert position == Position(0, 0, N)
