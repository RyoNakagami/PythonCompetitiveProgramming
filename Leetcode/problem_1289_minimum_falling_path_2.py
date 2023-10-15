from typing import List
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        res = grid[0]
        length = len(grid)

        if length == 1:
            return res[0]
        
        for i in range(1, length):
            tmp = [0] * length
            tmp[-1] = grid[i][-1] + min(res[:-1])
            tmp[0] = grid[i][-1] + min(res[1:])
            for j in range(0, length-1):
                tmp[j] = grid[i][j] + min(res[:j] + res[j+1:])
            res = tmp
        return min(res)