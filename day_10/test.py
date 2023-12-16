from main_p1 import solve as p1_solve
from main_p2 import solve as p2_solve

# lines = [
#     "7-F7-",
#     ".FJ|7",
#     "SJLL7",
#     "|F--J",
#     "LJ.LJ",
#     ]

# def test_p1():
#     assert p1_solve(lines) == 8

lines_p2 = [
    "FF7FSF7F7F7F7F7F---7",
    "L|LJ||||||||||||F--J",
    "FL-7LJLJ||||||LJL-77",
    "F--JF--7||LJLJ7F7FJ-",
    "L---JF-JLJ.||-FJLJJ7",
    "|F|F-JF---7F7-L7L|7|",
    "|FFJF7L7F-JF7|JL---7",
    "7-L-JL7||F7|L7F-7F7|",
    "L.L7LFJ|||||FJL7||LJ",
    "L7JLJL-JLJLJL--JLJ.L",
]

def test_p2():
    assert p2_solve(lines_p2) == 10

def test_p2_simple():
    lines_p2_simple = [
        "...........",
        ".S-------7.",
        ".|F-----7|.",
        ".||.....||.",
        ".||.....||.",
        ".|L-7.F-J|.",
        ".|..|.|..|.",
        ".L--J.L--J.",
        "...........",
    ]
    assert p2_solve(lines_p2_simple) == 4

test_p2()