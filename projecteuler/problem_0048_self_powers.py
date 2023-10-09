class Solution:
    """
    Problem
        Find the last ten digits of the series , \sum_{i=1}^1000 i^i

    Usage
        solver = Solution()
        solver.solve(1000, 10 ** 10)
    """
    def solve(self, max_int: int, modulas: int):
        return sum([pow(i, i, modulas) for i in range(1, max_int)]) % modulas