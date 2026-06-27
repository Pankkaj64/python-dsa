import pytest

from countvowels import countvowels


# Note: "text, expected" is ONE string (the two column names),
# then a comma, then the list of (input, expected) rows.
@pytest.mark.parametrize("text, expected", [
    ("hello", 2),        # h-e-l-l-o  -> e, o        = 2
    ("", 0),             # empty string             = 0
    ("racecar", 3),      # r-a-c-e-c-a-r -> a, e, a  = 3
    ("abcd", 1),         # a                         = 1
    ("AEIOU", 5),        # uppercase counts too      = 5
])
def test_countvowels(text, expected):
    assert countvowels(text) == expected
