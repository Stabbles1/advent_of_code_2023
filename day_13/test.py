from main_p1 import solve as p1_solve

#from main_p2 import solve as p2_solve

lines = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
    ]

def test_p1():
    assert p1_solve(lines) == 405

# def test_p2():
#     assert p2_solve(lines) == 2
