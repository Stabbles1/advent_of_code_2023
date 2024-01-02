from main_p1 import solve as p1_solve

# from main_p2 import solve as p2_solve

lines = [
    "broadcaster -> a",
    "%a -> inv, con",
    "&inv -> b",
    "%b -> con",
    "&con -> output",
]


def test_p1():
    assert p1_solve(lines) == 11687500


# def test_p2():
#     assert p2_solve(lines) == 952408144115
