import pytest
from Leetcode.problem_0268_missing_number import Solution

@pytest.mark.parametrize(
    "input,expected", 
    [({"nums": [3,0,1]}, 2),
     ({"nums": [0,1]}, 2),
     ({"nums": [9,6,4,2,3,5,7,0,1]}, 8)
    ]
)

def test_with_example_0268(input, expected):
    Solver = Solution()
    assert Solver.missingNumber(input['nums']) == expected
