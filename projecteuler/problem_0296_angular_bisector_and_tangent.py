import math
    
class Solution:
    """ 
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
    
    #def check_length(self, AB, AC, BC):
    #    return BC <= AC & AC <= AB

    def find_solution(self, perimeter:int=100000):
        count = 0
        for BC in range(1, perimeter//3 + 1):
            for AC in range(BC, (perimeter - BC)//2 + 1):
                k = self.gcd(AC, BC)
                step =  AC//k + BC//k
                min_AB = math.ceil(AC / step) * step
                max_AB = min(AC + BC, perimeter - AC - BC + 1)
                count += math.ceil((max_AB - min_AB) / step)

        return count