from functools import reduce
from operator import xor
from typing import List

class Solution:
    """
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

    Example:
        Input: nums = [4,1,2,1,2]
        Output: 4

    Constraints:

        1 <= nums.length <= 3 * 104
        -3 * 104 <= nums[i] <= 3 * 104
        Each element in the array appears twice except for one element which appears only once.
    """
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)