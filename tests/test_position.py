import pytest
from mars_rover_with_ai.position import Position, Direction

N, E, S, W = Direction.N, Direction.E, Direction.S, Direction.W


@pytest.mark.parametrize("start, expected", [
    (Position(0, 0, N), Position(0, 1, N)),
    (Position(0, 0, E), Position(1, 0, E)),
    (Position(0, 0, S), Position(0, -1, S)),
    (Position(0, 0, W), Position(-1, 0, W)),
])
def test_should_move_forward(start, expected):
    assert start.move_forward() == expected


@pytest.mark.parametrize("start, expected", [
    (Position(0, 0, N), Position(0, 0, E)),
    (Position(0, 0, E), Position(0, 0, S)),
    (Position(0, 0, S), Position(0, 0, W)),
    (Position(0, 0, W), Position(0, 0, N)),
])
def test_should_turn_right(start, expected):
    assert start.turn_right() == expected


@pytest.mark.parametrize("start, expected", [
    (Position(0, 0, N), Position(0, 0, W)),
    (Position(0, 0, W), Position(0, 0, S)),
    (Position(0, 0, S), Position(0, 0, E)),
    (Position(0, 0, E), Position(0, 0, N)),
])
def test_should_turn_left(start, expected):
    assert start.turn_left() == expected
