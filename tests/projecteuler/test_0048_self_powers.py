from typing import Any, Literal
import pytest
from projecteuler.problem_0048_self_powers import Solution

@pytest.mark.parametrize(
    "input,expected", 
    [({"nums": 10,'digits': 10**1}, 7),
     ({"nums": 10,'digits': 10**3}, 317),
     ({"nums": 10,'digits': 10**9}, 405071317),
     ({"nums": 1000,'digits': 10**10}, 9110846700)
     ]
)

def test_with_example_0048(input, expected):
    solver = Solution()
    assert solver.solve(input['nums'], input['digits']) == expected