class Solution:
    """
    Problem
        https://projecteuler.net/problem=37

    The number 3797 has an interesting property. Being prime itself, 
    it is possible to continuously remove digits from left to right, 
    and remain prime at each stage: 3797, 797, 97, 7. 
    Similarly we can work from right to left: 3, 37, 379, and 3797.

    Find the sum of the first eleven primes that are both truncatable 
    from left to right and right to left.

    NOTE: 2, 3, 7 are not considered to be truncatable primes.
    
    How to Run
        Solver = Solution()
        sum(Solver.find_solution(target_length=11))
    """

    def is_prime(self, num:int):
        if num <= 1:
            return False
        
        if num in [2, 3]:
            return True
                    
        if (num % 2 == 0) or (num % 3 == 0):
            return False
        base_list = [i for i in range(2, num // 2) if (i % 2 != 0) or (i % 3 != 0)]
        for base in base_list:
            if num % base == 0:
                return False
        return True
    
    def is_tractable(self, num:int):
        if num < 10:
            return False
        digit = 1
        while True:
            q, r = divmod(num, 10**digit)
            if q == 0:
                break
            if (self.is_prime(q)) and self.is_prime(r):
                digit += 1
            else:
                return False
            
        return True
    
    def find_solution(self, target_length:int=11):
        res = []
        num = 11
        while len(res) < target_length:
            if self.is_tractable(num) and self.is_prime(num):
                res.append(num)
                print(res)
            num += 2
        return res
            