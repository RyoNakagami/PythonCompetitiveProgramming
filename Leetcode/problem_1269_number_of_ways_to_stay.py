from typing import List

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        # reduce the arrLen size
        arrLen = min(steps // 2 + 1, arrLen)
        
        # If arrLen is 1, there's only one way to be at the starting position
        if arrLen == 1:
            return 1
        
        # Initialize an array to track the number of ways to reach each position
        res = [0] * arrLen
        res[0] = 1

        for d in range(steps):
            a = res
            # Create a new array to track the number of ways in the next step
            b = [0] * arrLen

            # Update the number of ways to reach the current position
            b[0] += a[0]
            b[1] += a[0]
            max_idx = min(arrLen, steps+1-d)
            for i in range(1, max_idx - 1):
                b[i-1] += a[i]
                b[i] += a[i]
                b[i+1] += a[i]
            b[max_idx-1] += a[max_idx-1]
            b[max_idx-2] += a[max_idx-1]

            # Update the current step's array
            res = b

        return res[0] % 1000_000_007