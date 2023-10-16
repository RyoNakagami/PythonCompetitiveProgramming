from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thresh = target - min(nums)
        d = {j:i for i, j in enumerate(nums) if j <= thresh}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d and d[diff] != i:
                return [i, d[diff]]