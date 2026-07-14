import pytest

from perfect_number import is_perfect_number


@pytest.mark.parametrize("n, expected", [
    (6, True),       # 1 + 2 + 3 = 6
    (28, True),      # 1 + 2 + 4 + 7 + 14 = 28
    (496, True),     # perfect number
    (8128, True),    # perfect number
    (12, False),     # abundant number
    (1, False),
    (2, False),
    (10, False),
    (100, False),
    (0, False),
    (-6, False),
])
def test_is_perfect_number(n, expected):
    assert is_perfect_number(n) is expected


def test_is_perfect_number_non_integer_raises():
    with pytest.raises(TypeError):
        is_perfect_number(6.5)


def test_is_perfect_number_bool_raises():
    with pytest.raises(TypeError):
        is_perfect_number(True)
