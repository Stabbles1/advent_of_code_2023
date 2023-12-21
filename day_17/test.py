import main_p1
from main_p1 import solve as p1_solve

# from main_p2 import solve as p2_solve

lines = [
    "2413432311323",
    "3215453535623",
    "3255245654254",
    "3446585845452",
    "4546657867536",
    "1438598798454",
    "4457876987766",
    "3637877979653",
    "4654967986887",
    "4564679986453",
    "1224686865563",
    "2546548887735",
    "4322674655533",
]

tiny = [
    "241",
    "311",
    "325",
]


def test_tiny():
    assert p1_solve(tiny) == 10


# def test_p1():
#     assert p1_solve(lines) == 102


# def test_p2():
#    assert p2_solve(read_input("day_16/test_input.txt")) == 51
