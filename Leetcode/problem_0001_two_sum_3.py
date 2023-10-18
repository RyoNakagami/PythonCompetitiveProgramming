from typing import List

class Solution:
    """
    Problem
        https://leetcode.com/problems/two-sum/

        Given an array of integers nums and an integer target, return indices 
        of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, 
        and you may not use the same element twice.
    
    Time Complexity: O(N)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_num = sorted(nums)
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx < right_idx and right_idx < len(nums):
            left_val, right_val = sorted_num[left_idx], sorted_num[right_idx]
            tmp = left_val + right_val
            if tmp < target:
                left_idx += 1
            elif tmp > target:
                right_idx -= 1
            else:
                first_idx = nums.index(left_val)
                second_idx = len(nums) - 1 - nums[::-1].index(right_val)
                return [first_idx, second_idx]
