import pytest
from Leetcode.problem_0136_single_number import Solution

@pytest.mark.parametrize(
    "input,expected", 
    [({"nums": [2,2,1]}, 1),
     ({"nums": [4,1,2,1,2]}, 4), 
     ({"nums": [1]}, 1)]
)

def test_with_example_0136(input, expected):
    Solver = Solution()
    assert Solver.singleNumber(input['nums']) == expected