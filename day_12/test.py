from main_p1 import is_valid, parse_line, simplify
from main_p1 import solve as p1_solve
from main_p2 import solve as p2_solve

lines = [
    "???.### 1,1,3",
    ".??..??...?##. 1,1,3",
    "?#?#?#?#?#?#?#? 1,3,1,6",
    "????.#...#... 4,1,1",
    "????.######..#####. 1,6,5",
    "?###???????? 3,2,1",
    ]

# def test_is_valid():
#     solved_lines = [
#         "#.#.### 1,1,3",
#         ".#...#....###. 1,1,3",
#         ".#.###.#.###### 1,3,1,6",
#         "####.#...#... 4,1,1",
#         "#....######..#####. 1,6,5",
#         ".###.##....# 3,2,1",
#     ]
#     for line in solved_lines:
#         assert is_valid(*parse_line(line))

#     assert is_valid(*parse_line("###.### 1,1,3")) == False
#     assert is_valid(*parse_line("##..### 1,1,3")) == False
#     assert is_valid(*parse_line("....... 1,1,3")) == False
#     assert is_valid(*parse_line("####### 1,1,3")) == False
#     assert is_valid(*parse_line("#.#.###.# 1,1,3")) == False

def test_simplify():
    assert simplify(*parse_line("##???#??#?????????# 11,6")) == ("###########??######", [11,6])

def test_simplify_2():
    assert simplify(*parse_line(".#???#??#?????????#. 11,6")) == (".###########?######.", [11,6])

def test_p1():
    assert p1_solve([lines[0]]) == 1

def test_p1_full():
    assert p1_solve(lines) == 21

def test_p2():
    assert p2_solve([lines[0]]) == 1

def test_p2_2():
    assert p2_solve([lines[1]]) == 16384

# def test_p2_full():
#     assert p2_solve(lines) == 525152
