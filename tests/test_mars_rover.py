import unittest
from mars_rover_with_ai.mars_rover import MarsRover

class TestMarsRover(unittest.TestCase):
    def test_initial_position(self):
        rover = MarsRover()
        position = rover.get_position()

        self.assertEqual(position, (0, 0, 'N'))


if __name__ == '__main__':
    unittest.main()
