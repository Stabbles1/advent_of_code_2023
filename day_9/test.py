from main_p1 import solve as p1_solve
from main_p2 import solve as p2_solve

lines = [
    "0 3 6 9 12 15",
    "1 3 6 10 15 21",
    "10 13 16 21 30 45",
    ]

def test_p1():
    assert p1_solve(lines) == 114

def test_p2():
    assert p2_solve(lines) == 2
