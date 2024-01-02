from main_p1 import solve as p1_solve

# from main_p2 import solve as p2_solve

lines = [
    "...........",
    ".....###.#.",
    ".###.##..#.",
    "..#.#...#..",
    "....#.#....",
    ".##..S####.",
    ".##..#...#.",
    ".......##..",
    ".##.#.####.",
    ".##..##.##.",
    "...........",
]


def test_p1():
    assert p1_solve(lines, steps=6) == 16


# def test_p2():
#     assert p2_solve(lines) == 952408144115
