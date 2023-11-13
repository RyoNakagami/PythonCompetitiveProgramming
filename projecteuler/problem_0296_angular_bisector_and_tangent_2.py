#%%
import math
from multiprocessing import Pool
    
class Solution:
    """
    Note
        faster version using the multiprocessing module
    
    Problem
        https://projecteuler.net/problem=296
    
    Solution
        Using the similarity between the triangle ACD and BCE
        and BE = BD
    
    Usage
        Solver = Solution()
        Solver.find_solution()
        >>> 1137208419
    """
    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def compute(self, BC):
        count = 0
        for AC in range(BC, (self.perimeter - BC)//2 + 1):
            k = self.gcd(AC, BC)
            step = AC//k + BC//k
            min_AB = math.ceil(AC / step) * step
            max_AB = min(AC + BC, self.perimeter - AC - BC + 1)
            count += math.ceil((max_AB - min_AB) / step)
        return count
    
    def find_solution(self, cpu, perimeter:int=100000):
        self.perimeter = perimeter
        with Pool(processes=cpu) as pool:
            return sum(pool.map(Solver.compute, range(1, perimeter//3 + 1)))

Solver = Solution()
Solver.find_solution(cpu=30, perimeter=100000)
