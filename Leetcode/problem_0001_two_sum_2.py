#%%
from typing import List

class Solution:
    """
    Problem
        https://leetcode.com/problems/two-sum/

        Given an array of integers nums and an integer target, return indices 
        of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, 
        and you may not use the same element twice.

    Note:
        the time complexity is O(N^2) 
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for left_idx in range(0, len(nums)):
            for right_idx in range(left_idx+1, len(nums)):
                if nums[left_idx] + nums[right_idx] == target:
                    return [left_idx, right_idx]