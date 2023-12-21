from dataclasses import dataclass, field


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class Block:
    heat_loss: int
    coordinates: Coordinates
    best_value_so_far: int = 99999999999
    best_paths_so_far: list = field(default_factory=list)
    best_value: int = 99999999999
    best_paths: list = field(default_factory=list)

    @property
    def is_optimised(self):
        return self.best_value != 99999999999
