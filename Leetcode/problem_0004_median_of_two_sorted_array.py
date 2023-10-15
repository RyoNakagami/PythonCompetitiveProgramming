from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        if len(merged) % 2 == 1:
            idx = len(merged) // 2
            return merged[idx] / 1.0
        idx = len(merged) // 2
        return (merged[idx] + merged[idx -1]) / 2