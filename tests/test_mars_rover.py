from mars_rover_with_ai.mars_rover import MarsRover, Position


def test_should_initialize_at_default_position():
    rover = MarsRover()
    position = rover.position

    assert position == Position(0, 0, 'N')


def test_should_move_forward():
    rover = MarsRover()
    rover.execute(command='f')

    assert rover.position == Position(0, 1, 'N')
