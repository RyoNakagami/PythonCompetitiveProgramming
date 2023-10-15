class Solution:
    """
    If a box contains twenty-one coloured discs, composed of fifteen blue discs 
    and six red discs, and two discs were taken at random, it can be seen that 
    the probability of taking two blue discs,

        P(BB) = 1/2

    The next such arrangement, for which there is exactly 50% chance of taking 
    two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

    By finding the first arrangement to contain over 10^12
    discs in total, determine the number of blue discs that the box would contain.


    Solution
        Target = 10 ** 12
        generator = Solution.solution_generator()
        print(next(x[1] for x in filter(lambda x: x[0] > Target, generator)))
    """
    def solution_generator():
        """
        Using Pell's equation such that

            (x^2-ny^2)(z^2-nt^2) = (xz + nty)^2-n(xt + yz)^2
            where n = 2, z = 3, t = 2
        """
        x, y = 1, 1
        while True:
            x, y = 3 * x + 4 * y, 2 * x + 3 * y
            if (x % 2 == 1) and (y % 2 == 1):
                total, blue = (x + 1) // 2, (y + 1) // 2
                yield total, blue