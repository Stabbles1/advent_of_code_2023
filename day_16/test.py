from main_p1 import read_input
from main_p1 import solve as p1_solve

# from main_p2 import solve as p2_solve


def test_p1():
    assert p1_solve(read_input("day_16/test_input.txt")) == 46
test_p1()
# def test_p2():
#     assert p2_solve(lines) == 145