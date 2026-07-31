from typing import List


def search_insert(nums: List[int], target: int) -> int:
    """
    Returns the index if the target is found.
    Otherwise, returns the index where it should be inserted.
    """

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left