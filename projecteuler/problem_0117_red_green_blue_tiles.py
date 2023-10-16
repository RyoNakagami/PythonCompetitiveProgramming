from functools import lru_cache

class Solution:
    """
    Problem
        https://projecteuler.net/problem=117
        
    Solution
        solver = Solution()
        solver.dp(50)    
    """
    @lru_cache(maxsize=None)
    def dp(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        if n == 4:
            return 8
        else:
            return self.dp(n-4) + self.dp(n-3) + self.dp(n-2) + self.dp(n-1)
        