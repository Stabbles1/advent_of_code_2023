from main_p1 import solve as p1_solve
from main_p2 import solve as p2_solve

lines = [
    "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7",
]

def test_p1():
    assert p1_solve(lines) == 1320

def test_p2():
    assert p2_solve(lines) == 145