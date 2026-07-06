import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize("n, expected", [
    (1, "1"),            # plain number
    (2, "2"),            # plain number
    (3, "Fizz"),         # divisible by 3
    (5, "Buzz"),         # divisible by 5
    (9, "Fizz"),         # divisible by 3
    (10, "Buzz"),        # divisible by 5
    (15, "FizzBuzz"),    # divisible by 3 and 5
    (30, "FizzBuzz"),    # divisible by 3 and 5
])
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected


def test_fizzbuzz_non_positive_raises():
    with pytest.raises(ValueError):
        fizzbuzz(0)
