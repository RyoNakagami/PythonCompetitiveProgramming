class Solution:
    """
    Problem
        https://projecteuler.net/problem=47

    Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
    
    
    How to Run
        Solver = Solution()
        Solver.find_solution(4, 4)
    """

    def prime_factorize(self, n):
        a = set()
        while n % 2 == 0:
            a.add(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.add(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.add(n)
        return set(a)
    
    def find_solution(self, unique_prime:int, consecutive:int, threshold:int=1000000):
        num = 1
        candidate = []
        while num < threshold:
            if len(self.prime_factorize(num)) == unique_prime:
                candidate.append(num)
            if len(candidate) > 1 and candidate[-1] - candidate[-2] > 1:
                candidate = [num]
            if len(candidate) == consecutive:
                return candidate
            num += 1
