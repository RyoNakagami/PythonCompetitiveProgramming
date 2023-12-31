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
        thresh = target - min(nums)
        d = {j:i for i, j in enumerate(nums) if j <= thresh}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d and d[diff] != i:
                return [i, d[diff]]
      