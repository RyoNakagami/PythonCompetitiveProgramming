import pytest
from projecteuler.problem_0041_pandigital_prime import Solution

@pytest.mark.parametrize(
    "input,expected", 
    [({"nums": 9}, 7652413),
     ({"nums": 8}, 7652413), 
     ({"nums": 7}, 7652413), 
     ({"nums": 6}, 4231),
     ({"nums": 5}, 4231),
     ({"nums": 4}, 4231),
     ({"nums": 3}, 1),
     ({"nums": 2}, 1),
     ({"nums": 1}, 1)
     ]
)

def test_with_example_0136(input, expected):
    Solver = Solution()
    assert Solver.search(input['nums']) == expected