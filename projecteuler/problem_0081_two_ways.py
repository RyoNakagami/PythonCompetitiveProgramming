class Solution:
    """
    Problem
        https://projecteuler.net/problem=81

    Note
        the data contains the empty line at the last
        Remove it by using ".rstrip('\n')".

    Solution
        Solver = Solution()
        Solver.compute_minimum()
    """

    def __init__(self, path="projecteuler/data/0081_matrix.txt"):
        with open(path) as f:
            data = f.read()
        self.data = [[int(num) for num in line.split(",")] for line in data.rstrip('\n').split("\n")]

    def compute_minimum(self):
        self.max_idx = len(self.data) - 1
        for row in range(-self.max_idx, 1):
            row = -row
            for col in range(-self.max_idx, 1):
                col = -col
                tmp = []
                if col + 1 <= self.max_idx:
                    tmp.append(self.data[row][col+1])
                if row + 1 <= self.max_idx:
                    tmp.append(self.data[row+1][col])
                if len(tmp) == 0:
                    continue
                self.data[row][col] += min(tmp)
        
        return self.data[0][0]
