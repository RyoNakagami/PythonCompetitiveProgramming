class Solution:
    """
    Problem
        https://projecteuler.net/problem=39

    If is the perimeter of a right angle triangle with integral length sides, {a, b, c}, 
    there are exactly three solutions for p = 120,

        {20, 48, 52}, {24, 45, 51}, {30, 40, 50}

    For which value of p <= 1000, is the number of solutions maximised?
    
    
    How to Run
        solver = Solution()
        solver.find_solution(1000)
    """

    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def find_solution(self, sum_limit) :
        res = [0] * (sum_limit + 1)
        for m in range(1, int((sum_limit//2)**0.5)+1):
            for n in range(-m+1, 0, 2) :
                n = abs(n)
                if self.gcd(m, n) == 1:                
                    a = m * m - n * n
                    b = 2 * m * n
                    c = m * m + n * n

                    sum_of_length = a + b + c
                    if sum_of_length <= sum_limit:
                        for s in range(sum_of_length, sum_limit+1, sum_of_length):
                            res[s] += 1
        return res.index(max(res))