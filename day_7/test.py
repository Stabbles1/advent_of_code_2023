from main_p1 import solve as p1_solve
from main_p2 import solve as p2_solve

lines = [
"32T3K 765",
"T55J5 684",
"KK677 28",
"KTJJT 220",
"QQQJA 483",
]

def test_p1():
    assert p1_solve(lines) == 6440



def test_p2():
    assert p2_solve(lines) == 5905