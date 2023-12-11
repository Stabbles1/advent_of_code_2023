from dataclasses import dataclass


@dataclass
class Star:
    id: int
    x: int
    y: int
    total_length: int = 0

    def diff(self, star):
        return abs(star.x - self.x) + abs(star.y - self.y)

    def set_total_length(self, stars: list):
        for star in stars:
            self.total_length += self.diff(star)