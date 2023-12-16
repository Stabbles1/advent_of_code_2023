from dataclasses import dataclass


@dataclass
class Tile:
    symbol: str
    energised: bool = False

    def energise(self):
        self.energised = True

    def __repr__(self):
        if self.energised and self.symbol == ".":
            return "#"
        return self.symbol