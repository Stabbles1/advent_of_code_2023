from main_p1 import solve as p1_solve
from main_p2 import solve as p2_solve

lines = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]

def test_p1():
    assert p1_solve(lines) == 136

def test_p2():
    assert p2_solve(lines) == 64

test_p2()