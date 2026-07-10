import pytest
from sumofdigits import sum_of_digits


def test_sum_of_digits_single_digit():
    assert sum_of_digits(5) == 5
    assert sum_of_digits(0) == 0
    assert sum_of_digits(9) == 9


def test_sum_of_digits_multiple_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(9876) == 30
    assert sum_of_digits(505) == 10
    assert sum_of_digits(999) == 27


def test_sum_of_digits_negative():
    assert sum_of_digits(-123) == 6
    assert sum_of_digits(-9876) == 30
    assert sum_of_digits(-505) == 10


def test_sum_of_digits_zeros():
    assert sum_of_digits(0) == 0
    assert sum_of_digits(1000) == 1
    assert sum_of_digits(1001) == 2


def test_sum_of_digits_large_numbers():
    assert sum_of_digits(123456789) == 45
    assert sum_of_digits(111111) == 6


def test_sum_of_digits_type_error():
    with pytest.raises(TypeError):
        sum_of_digits("123")
    
    with pytest.raises(TypeError):
        sum_of_digits(12.34)
    
    with pytest.raises(TypeError):
        sum_of_digits(True)
    
    with pytest.raises(TypeError):
        sum_of_digits(None)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
