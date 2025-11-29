from mars_rover_with_ai.position import Position, Direction, N, E, S, W


class MarsRover:
    def __init__(self, position=None):
        self._position = position if position is not None else Position(0, 0, N)

    @property
    def position(self):
        return self._position

    def execute(self, command: str):
        if command == 'f':
            self._position = self._position.move_forward()
        elif command == 'r':
            self._position = self._position.turn_right()
        elif command == 'l':
            self._position = self._position.turn_left()
