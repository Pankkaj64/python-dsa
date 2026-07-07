import pytest

from factorial import factorial


@pytest.mark.parametrize("n, expected", [
    (0, 1),          # base case
    (1, 1),          # base case
    (2, 2),
    (3, 6),
    (5, 120),
    (10, 3628800),
])
def test_factorial(n, expected):
    assert factorial(n) == expected


def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_non_integer_raises():
    with pytest.raises(TypeError):
        factorial(3.5)
