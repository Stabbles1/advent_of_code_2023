from main_p1 import solve as solve_p1
from main_p2 import solve as solve_p2

lines = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

def test_p1():
    assert solve_p1(lines) == 4361

def test_p2():
    assert solve_p2(lines) == 467835