import pytest

from gcd import gcd


@pytest.mark.parametrize("a, b, expected", [
    (12, 18, 6),
    (48, 36, 12),
    (17, 5, 1),          # coprime
    (0, 9, 9),           # gcd with zero
    (0, 0, 0),
    (100, 25, 25),
    (-12, 18, 6),        # negatives use magnitude
])
def test_gcd(a, b, expected):
    assert gcd(a, b) == expected


def test_gcd_non_integer_raises():
    with pytest.raises(TypeError):
        gcd(12.0, 8)
