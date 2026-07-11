import pytest

from armstrong import is_armstrong


@pytest.mark.parametrize("n, expected", [
    (0, True),
    (1, True),
    (153, True),
    (370, True),
    (371, True),
    (407, True),
    (1634, True),
    (2, True),
    (10, False),
    (100, False),
])
def test_is_armstrong(n, expected):
    assert is_armstrong(n) is expected


def test_is_armstrong_non_integer_raises():
    with pytest.raises(TypeError):
        is_armstrong(3.5)


def test_is_armstrong_bool_raises():
    with pytest.raises(TypeError):
        is_armstrong(True)
