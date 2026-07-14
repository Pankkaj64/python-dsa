import pytest

from prime_factors import prime_factors


@pytest.mark.parametrize("n, expected", [
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (6, [2, 3]),
    (12, [2, 2, 3]),
    (100, [2, 2, 5, 5]),
    (13195, [5, 7, 13, 29]),
])
def test_prime_factors(n, expected):
    assert prime_factors(n) == expected


def test_prime_factors_non_integer_raises():
    with pytest.raises(TypeError):
        prime_factors(3.5)


def test_prime_factors_bool_raises():
    with pytest.raises(TypeError):
        prime_factors(True)
