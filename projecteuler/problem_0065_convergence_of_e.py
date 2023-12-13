#%%
class Solution:
    """
    Problem
        https://projecteuler.net/problem=65

    How to Run
        solver = Solution()
        solver.find_solution(100)
    """
    def get_k(self, x):
        if x == 1:
            return 2
        if x % 3 == 0:
            return 2 * (x // 3)
        else:
            return 1

    def compute_denominator_nominator(self, index):
        n, d = 0, 1
        while index > 0:
            a = self.get_k(index)
            n, d = d, n + d * a
            index -= 1
        return d, n
    
    def find_solution(self, index):
        n = self.compute_denominator_nominator(index)[0]
        res = 0
        while n > 0: 
            n, r = divmod(n, 10)
            res += r
        return res