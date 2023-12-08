from main_p1 import solve as p1_solve

#from main_p2 import solve as p2_solve

lines = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]

def test_p1():
    assert p1_solve(lines) == 6



# def test_p2():
#     assert p2_solve(lines) == 5905