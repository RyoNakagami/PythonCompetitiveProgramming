class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        ## reduce the arrLen size
        arrLen = min(steps // 2 + 1, arrLen)
        
        if arrLen == 1:
            return 1
        
        res = [0] * arrLen
        res[0] = 1

        for d in range(steps):
            a = res
            b = [0] * arrLen

            b[0] += a[0]
            b[1] += a[0]
            max_idx = min(arrLen, steps+1-d)
            for i in range(1, max_idx - 1):
                b[i-1] += a[i]
                b[i] += a[i]
                b[i+1] += a[i]
            b[max_idx-1] += a[max_idx-1]
            b[max_idx-2] += a[max_idx-1]
            res = b

        return res[0] % 1000_000_007