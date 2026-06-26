import pytest

from reverse import reverse


# A table of (input, expected) — just like LeetCode's test cases.
@pytest.mark.parametrize("text, expected", [
    ("hello", "olleh"),      # normal
    ("a", "a"),              # single char
    ("", ""),                # empty edge case
    ("ab", "ba"),            # even length
    ("abc", "cba"),          # odd length
    ("aba", "aba"),          # palindrome
    ("12 3", "3 21"),        # spaces + digits
])
def test_reverse_string(text, expected):
    assert reverse(text) == expected


# A nice property-based check: reversing twice returns the original.
@pytest.mark.parametrize("text", ["hello", "", "racecar", "abcd"])
def test_double_reverse_is_identity(text):
    assert reverse(reverse(text)) == text
