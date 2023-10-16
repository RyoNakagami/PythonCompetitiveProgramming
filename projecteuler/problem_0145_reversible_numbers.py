#%%
class Solution:
    """
    Problem 
        https://projecteuler.net/problem=145

    Solution
        solver = Solution()
        solver.count_reversible(9)
    """
    def count_reversible(self, digits_number):
        count = 0
        for i in range(1, digits_number+1):
            if i % 2 == 0:
                count += 20 * (30 ** (i // 2 - 1))
            elif i % 4 == 3:
                odd_count = 5
                for k in range(i//2):
                    if k % 2 == 0: 
                        odd_count *= 20
                    else:
                        odd_count *= 25
                count += odd_count
        return count