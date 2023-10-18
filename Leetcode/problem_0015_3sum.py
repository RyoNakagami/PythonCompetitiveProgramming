from typing import List


class Solution:
    """
    Problem
        https://leetcode.com/problems/3sum/

        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        Notice that the solution set must not contain duplicate triplets.
    
    Related
        https://leetcode.com/problems/two-sum/
    
    Note
        this time, required to retund list of values, not index
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        max_idx = len(nums)-1
        prev = None
        for first_idx in range(max_idx):
            # reduce the search area
            if nums[first_idx] > 0:
                return res
            if nums[first_idx] == prev:
                continue
            
            # Main Part
            target = 0 - nums[first_idx]
            second_idx = first_idx + 1
            third_idx = max_idx
            while second_idx < third_idx and third_idx <= max_idx:
                tmp = nums[second_idx] + nums[third_idx]
                if tmp > target:
                    third_idx -= 1
                elif tmp < target:
                    second_idx += 1
                else:
                    res.append([nums[first_idx], nums[second_idx], nums[third_idx]])
                    second_idx += 1
                    while nums[second_idx] == nums[second_idx - 1] and second_idx < third_idx:
                        second_idx += 1
            prev = nums[first_idx]
        
        return res