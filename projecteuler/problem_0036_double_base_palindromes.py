class Solution:
    """ 
    Problem
        https://projecteuler.net/problem=36
    
    Solution
        brute-force check whether int is base-10 and base-2 palindrome
    
    Usage
        Solver = Solution()
        Solver.find_solution()
    """
    def is_palindrome(self, binary_string: str):
        left_idx = 0
        right_idx = len(binary_string) - 1
        while left_idx < right_idx:
            if binary_string[left_idx] != binary_string[right_idx]:
                return False
            left_idx += 1
            right_idx -= 1
        return True
    
    def find_solution(self, begin=1, end=1000000):
        total = 0
        for integer in range(begin, end):
            if self.is_palindrome(str(integer)) and self.is_palindrome(bin(integer)[2:]):
                total += integer
        return total