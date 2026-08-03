from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, current: List[int], remaining: int):
            if remaining == 0:
                result.append(current[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # Reuse the same element, so pass i instead of i + 1
                backtrack(i, current, remaining - candidates[i])

                current.pop()

        backtrack(0, [], target)
        return result