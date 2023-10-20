class Solution:
    """  
    Problem
        https://projecteuler.net/problem=49

    Usage
        Solver = Solution()
        Solver.find_arithmetic_prime()
    """
    def prime_generator(self):
        START, END = 1000, 10000
        nums = list(range(2, END))
        num = 2
        while num < END**0.5 and num is not None:
            nums = list(filter(lambda x: x % num > 0 or x <= num, nums))
            num_idx = nums.index(num)
            if num_idx == len(nums) - 1:
                break
            num = nums[num_idx+1]
        return list(filter(lambda x: x >= START, nums))
    def is_same_str(self, p1, p2, p3):
        return sorted(str(p1)) == sorted(str(p2)) == sorted(str(p3))
    def find_arithmetic_prime(self):
        prime_list = self.prime_generator()
        res = []
        for i in range(0, len(prime_list)):
            p1 = prime_list[i]
            for j in range(i+1, len(prime_list)):
                p3 = prime_list[j]
                p2 = (p1 + p3) // 2
                if p2 not in prime_list:
                    continue
                if self.is_same_str(p1, p2, p3):
                    res.append([p1, p2, p3])
        return res
