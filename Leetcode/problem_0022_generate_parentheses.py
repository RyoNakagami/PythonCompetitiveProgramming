from typing import List

class Solution:
    """
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    Example 1:

        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]
    
    Example 2:

        Input: n = 1
        Output: ["()"]
    

    Constraints:
        1 <= n <= 8

    Solution
        solver = Solution()
        solver.generateParenthesis()
    """
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.recursive_search(n, n, '')
        return self.res

    def recursive_search(self, left, right, string):
        if right < left:
            return None
        if right == 0 and left == 0:
            return self.res.append(string)
        if right == 1 and left == 1:
            return self.res.append(string+"()")
        if left > 0:
            self.recursive_search(left-1, right, string+"(")
        if right > 0:
            self.recursive_search(left, right-1, string+")")