import pytest

from isprime import is_prime


@pytest.mark.parametrize("n, expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (100, False),
    (97, True),
    (-7, False),
])
def test_is_prime(n, expected):
    assert is_prime(n) == expected


def test_is_prime_non_integer_raises():
    with pytest.raises(TypeError):
        is_prime(3.5)
