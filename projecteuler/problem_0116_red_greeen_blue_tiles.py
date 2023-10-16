from functools import lru_cache
class solution:
    """
    Problem
        https://projecteuler.net/problem=116

    Solution
        solver = solution()
        solver.compute_replacement(50)
    """
    @lru_cache(maxsize=None)
    def red_dp(self, n):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        else:
            return self.red_dp(n-1) + self.red_dp(n-2) + 1

    @lru_cache(maxsize=None)
    def green_dp(self, n):
        if n <= 2:
            return 0
        if n == 3:
            return 1
        if n == 4:
            return 2
        else:
            return self.green_dp(n-1) + self.green_dp(n-3) + 1
    
    @lru_cache(maxsize=None)
    def blue_dp(self, n):
        if n <= 3:
            return 0
        if n == 4:
            return 1
        if n == 5:
            return 2
        else:
            return self.blue_dp(n-1) + self.blue_dp(n-4) + 1

    def compute_replacement(self, n):
        return self.red_dp(n) + self.green_dp(n) + self.blue_dp(n)
