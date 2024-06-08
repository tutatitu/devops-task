import pytest
from calculator.calculator import add, subtract


@pytest.mark.parametrize(
    ('x', 'y', 'result'), [
        (2, 2, 4),
        (2.5, 3.5, 6),
        (-4, 3, -1),
        ('Hello', ' World', 'Hello World'),
        ([1, 2], [3, 4], [1, 2, 3, 4]),
    ]
)
def test_add(x, y, result):
    assert add(x, y) == result


@pytest.mark.parametrize(
    ('x', 'y', 'result'), [
        (2, 2, 0),
        (2.5, 3.5, -1),
        (5, -3, 8),
    ]
)
def test_subtract(x, y, result):
    assert subtract(x, y) == result
