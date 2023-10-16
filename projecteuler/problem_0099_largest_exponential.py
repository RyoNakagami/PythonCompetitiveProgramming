from math import log10
from functools import reduce

class Solution:
    """
    Solution
        solver = Solution()
        solver.get_idx()
    """
    def __init__(self, path="projecteuler/data/0099_base_exp.txt"):
        with open(path) as f:
            data = f.read()
        self.data = [[int(num) for num in line.split(",")] for line in data.split("\n")]

    def get_idx(self):
        log_data = list(map(lambda x: reduce(lambda a, b: b*log10(a), x), self.data))
        return log_data.index(max(log_data)) + 1
