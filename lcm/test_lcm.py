import pytest

from lcm import lcm


@pytest.mark.parametrize("a, b, expected", [
    (4, 6, 12),
    (12, 18, 36),
    (7, 5, 35),          # coprime -> product
    (21, 6, 42),
    (0, 9, 0),           # lcm with zero
    (0, 0, 0),
    (-4, 6, 12),         # negatives use magnitude
])
def test_lcm(a, b, expected):
    assert lcm(a, b) == expected


def test_lcm_non_integer_raises():
    with pytest.raises(TypeError):
        lcm(4.0, 6)
