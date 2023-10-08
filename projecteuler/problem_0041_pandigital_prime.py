from itertools import permutations
from functools import reduce

class Solution:
    """
    We shall say that an n-digit number is pandigital if it makes use of all 
    the digits 1 to n exactly once. 
    
    For example, 2143 is a 4-digit pandigital and is also prime.

    What is the largest n-digit pandigital prime that exists?
    """

    def is_prime(self, num: int):
        if (num % 2 == 0) or (num % 3 == 0):
            return False
        base_list = [i for i in range(2, num // 2) if (i % 2 != 0) or (i % 3 != 0)]
        for base in base_list:
            if num % base == 0:
                return False
        return True
    
    def search(self, digits: int):
        num_list = permutations([i for i in range(1, digits + 1)[::-1]], digits)
        for num in num_list:
            num = reduce(lambda b, a : 10 * b + a, num)
            res_prime = self.is_prime(num)
            if res_prime:
                return num
        return self.search(digits -1)