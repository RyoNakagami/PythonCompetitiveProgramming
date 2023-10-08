class Solution:
    """
    It turns out that 12 cm is the smallest length of wire that can be bent to form an 
    integer sided right angle triangle in exactly one way, but there are many more examples.

        12cm: (3,4,5)
        24cm: (6,8,10)
        30cm: (5,12,13)

    Other lengths allow more than one solution to be found; for example, using 120cm
    it is possible to form exactly three different integer sided right angle triangles.

        120cm: (30, 40, 50), (20,48,52), (24,454,51)
    
    Given that L is the length of the wire, for how many values of L <= 1,500,000 
    can exactly one integer sided right angle triangle be formed?
    
    
    How to Run
        solver = Solution()
        solver.singular_pythagorean_count(1500000)
    """

    def gcd(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a

    def singular_pythagorean_count(self, sum_limit) :
        res = [0] * (sum_limit + 1)
        for m in range(1, int((sum_limit//2)**0.5)+1):
            for n in range(-m+1, 0, 2) :
                n = abs(n)
                if self.gcd(m, n) == 1:                
                    a = abs(m * m - n * n)
                    b = 2 * m * n
                    c = m * m + n * n

                    sum_of_length = a + b + c
                    if sum_of_length <= sum_limit:
                        for s in range(sum_of_length, sum_limit+1, sum_of_length):
                            res[s] += 1
        return res.count(1)
