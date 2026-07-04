import pytest

from fibonacci import fibonacci


@pytest.mark.parametrize("n, expected", [
    (0, 0),      # base case
    (1, 1),      # base case
    (2, 1),      # 0 + 1
    (5, 5),      # 0,1,1,2,3,5
    (10, 55),    # classic checkpoint
    (15, 610),   # larger value
])
def test_fibonacci(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_negative_raises():
    with pytest.raises(ValueError):
        fibonacci(-1)
