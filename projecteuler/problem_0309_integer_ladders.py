class Solution:
    """
    Problem
        https://projecteuler.net/problem=309
    
    Usage
        solver = Solution(1000000)
        solver.solve()
    """
    def __init__(self, y_limit) -> None:
        self.y_limit = y_limit
    
    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    def is_h_int(self, a, b):
        return (a * b) % (a + b) == 0

    def make_pythagorean_triples(self) :
        self.res = [[] for _ in range(self.y_limit + 1)]
        for m in range(1, int(self.y_limit ** 0.5)):
            for n in range(-m+1, 0, 2) :
                n = -n
                if self.gcd(m, n) == 1:                
                    a = m * m - n * n
                    b = 2 * m * n
                    c = m * m + n * n
                    power =  (self.y_limit - 1) // c + 1
                    for s in range(1, power):
                        tmp1 = a * s
                        tmp2 = b * s
                        self.res[tmp1].append(tmp2)
                        self.res[tmp2].append(tmp1)
    
    def solve(self):
        self.make_pythagorean_triples()
        count = 0
        for base_idx in range(0, len(self.res)):
            ref_array = self.res[base_idx]
            inner_len = len(ref_array)
            for ref_a_idx in range(0, inner_len):
                for ref_b_idx in range(ref_a_idx+1, inner_len):
                    if self.is_h_int(ref_array[ref_a_idx], ref_array[ref_b_idx]):
                        count += 1
        
        return count
