#%%
import pytest
from Leetcode.problem_0118_pascals_triangle import Solution

@pytest.mark.parametrize(
    "input,expected", 
    [({"numRows": 5}, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
     ({"numRows": 1}, [[1]])
    ]
)

def test_with_example_0118(input, expected):
    Solver = Solution()
    assert Solver.generate(input['numRows']) == expected