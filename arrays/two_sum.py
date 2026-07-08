"""
Two Sum

Given an array of integers and a target, return indices of the two
numbers that add up to the target.

Approach: Use a hashmap to store seen values and their indices.
Time: O(n), Space: O(n)
"""

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    print("All tests passed.")
