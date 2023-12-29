import re
from dataclasses import dataclass


@dataclass
class Scrap:
    x: int
    m: int
    a: int
    s: int

    @property
    def value(self):
        return self.x + self.m + self.a + self.s


def from_string(s: str) -> Scrap:
    matches = re.search(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)", s)
    return Scrap(
        x=int(matches.group(1)),
        m=int(matches.group(2)),
        a=int(matches.group(3)),
        s=int(matches.group(4)),
    )
