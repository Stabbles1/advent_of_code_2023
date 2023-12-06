from main_p1 import solve as p1_solve
from main_p2 import solve as p2_solve

lines = [
"Time:        42     89     91     89",
"Distance:   308   1170   1291   1467"
]

def test_p1():
    assert p1_solve(times=[7, 15, 30], distances=[9,40,200]) == 288



def test_p2():
    assert p2_solve(times=[71530], distances=[940200]) == 71503