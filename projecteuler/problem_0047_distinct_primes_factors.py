import itertools

class Solution:
    """import itertools
    Problem
        https://projecteuler.net/problem=47

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
    
    
    How to Run
        Solver = Solution()
        Solver.find_solution(6, 4, 4)
    """

    def prime_factorize(self, n):
        a = []
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return set(a)
    
    def check_consecutive(self, arr):
        consecutive_array = [list(g) for _, g in itertools.groupby(arr, 
                                key=lambda n, c=itertools.count(): n - next(c))]
        return consecutive_array

    def find_solution(self, digits, unique_prime, consecutive):
        candidate = []
        for num in range(10**(digits - 1), 10**digits):
            if len(self.prime_factorize(num)) == unique_prime:
                candidate.append(num)
        candidate = self.check_consecutive(candidate)
        for res in candidate:
            if len(res) == consecutive:
                return res
