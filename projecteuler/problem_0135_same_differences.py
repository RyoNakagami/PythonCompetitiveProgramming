
class Solution:
    """
    Problem 
        https://projecteuler.net/problem=135
        
    Usage
        Solver = Solution(1000000)
        Solver.solve(10)
    """
    def __init__(self, max_n):
        self.max_n = max_n

    def count_solution(self):
        self.res = [0] * (self.max_n + 1)
        for y in range(1, self.max_n + 1):
            for d in range(int((y)/4) + 1, y):
                n_idx =  y * (4*d - y)
                if n_idx > self.max_n:
                    break
                self.res[n_idx] += 1
    
    def solve(self, sol_number):
        self.count_solution()
        return self.res.count(sol_number)
