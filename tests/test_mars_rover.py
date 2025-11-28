from mars_rover_with_ai.mars_rover import MarsRover, Position, Direction


def test_should_initialize_at_default_position():
    rover = MarsRover()
    position = rover.position

    assert position == Position(0, 0, Direction.N)


def test_should_move_forward():
    rover = MarsRover()
    rover.execute(command='f')

    assert rover.position == Position(0, 1, Direction.N)


def test_should_turn_right():
    rover = MarsRover()
    rover.execute(command='r')

    assert rover.position == Position(0, 0, Direction.E)

