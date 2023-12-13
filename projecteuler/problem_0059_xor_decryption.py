from operator import xor
import string

class Solution:
    """
    Problem
        https://projecteuler.net/problem=59
    
    Note
        if you use a wrong cipher, it could return an ascii code which is not 
        within list(string.ascii_letters + string.digits + " .,:;+?!/[]()'\"")
        
    Solution
        Solver = Solution()
        Solver.find_solution()
    """
    def __init__(self, path="projecteuler/data/0059_cipher.txt"):
        with open(path) as f:
            data = f.read()
        self.data = []
        for line in data.split("\n"):
            for num in line.split(","):
                self.data.append(int(num)) 
        
        english = list(string.ascii_letters + string.digits + " .,:;+?!/[]()'\"")
        self.english = tuple(map(lambda x: ord(x), english))


    def split_three_group(self):
        self.data_1 = [self.data[i] for i in range(0, len(self.data), 3)]
        self.data_2 = [self.data[i] for i in range(1, len(self.data), 3)]
        self.data_3 = [self.data[i] for i in range(2, len(self.data), 3)]

    def decript(self, text_group):
        res = []
        for i in range(ord('a'), ord('z')+1):
            decripted = list(map(lambda x: xor(i, x), text_group))
            candidate = list(filter(lambda x: True if x in self.english else False, decripted))
            if len(candidate) == len(text_group):
                return sum(candidate)
        return res
    
    def find_solution(self):
        Solver.split_three_group()
        res = 0
        res += self.decript(self.data_1)
        res += self.decript(self.data_2)
        res += self.decript(self.data_3)
        return res