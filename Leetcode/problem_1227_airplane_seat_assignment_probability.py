class Solution:
    """
    Problem
        https://leetcode.com/problems/airplane-seat-assignment-probability/
    """
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        return 1/2
        