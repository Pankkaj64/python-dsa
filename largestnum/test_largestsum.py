import pytest

from largestnum import largesnum


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], 10),              # all positive -> whole array
    ([-1, 3, 4, 5], 12),            # leading negative is dropped
    ([5], 5),                        # single element
    ([-5], -5),                      # single negative element
    ([-3, -1, -2], -1),             # all negative -> largest single element
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),  # classic max subarray ([4, -1, 2, 1])
    ([0, 0, 0], 0),                  # all zeros
    ([2, -1, 2, -1, 2], 4),         # dips recover
])
def test_largesnum(nums, expected):
    assert largesnum(nums) == expected
