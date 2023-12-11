import copy

from main_p1 import expand
from main_p1 import solve as p1_solve

#from main_p2 import solve as p2_solve

lines = [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
    ]

expanded_lines = [
    "....#........",
    ".........#...",
    "#............",
    ".............",
    ".............",
    "........#....",
    ".#...........",
    "............#",
    ".............",
    ".............",
    ".........#...",
    "#....#.......",
]

def test_p1():
    result = expand(copy.deepcopy(lines))
    for i in range(0, len(expanded_lines)):
        print(result[i])
        assert expanded_lines[i] == result[i]
    assert p1_solve(lines) == 374

#def test_p2():
#    assert p2_solve(lines) == 2
