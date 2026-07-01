import pytest

from palindrome import is_palindrome


@pytest.mark.parametrize("text, expected", [
    ("racecar", True),    # classic palindrome (odd length)
    ("abba", True),       # even length palindrome
    ("hello", False),     # not a palindrome
    ("a", True),          # single char is always a palindrome
    ("", True),           # empty string counts as a palindrome
    ("ab", False),        # smallest non-palindrome
    ("madam", True),      # odd length palindrome
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected
