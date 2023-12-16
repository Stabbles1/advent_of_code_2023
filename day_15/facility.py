from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from hashing_algo import hash


@dataclass
class Operation(str, Enum):
    EQALS = "="
    DASH = "-"

@dataclass
class Lens:
    label: str
    operation: Operation
    focal_length: Optional[int] = -1

    @staticmethod
    def fromstr(string: str):
        if "=" in string:
            return Lens(label=string.split("=")[0],
                        operation=Operation.EQALS,
                        focal_length=int(string.split("=")[1]))
        else:
            return Lens(label=string.split("-")[0],
                        operation=Operation.DASH)
        
    @property
    def hashvalue(self):
        return hash(self.label)
    
    def __repr__(self):
        return f"[{self.label} {self.focal_length}]"
            



class Facility:
    def __init__(self):
        self.boxes: list[Box] = [Box() for _ in range(256)]

    def focusing_power(self):
        total = 0
        for i, box in enumerate(self.boxes):
            total += (i+1) * box.focusing_power()
        return total
    
    def execute_dash_lens(self, lens: Lens):
        self.boxes[lens.hashvalue].remove_lens(lens)
        
    def execute_eq_lens(self, lens: Lens):
        self.boxes[lens.hashvalue].replace_lens(lens)

    def execute_lens(self, lens: Lens)-> None:
        if lens.operation == "=":
            self.execute_eq_lens(lens)
        else:
            self.execute_dash_lens(lens)
            

    def __repr__(self):
        string = ""
        for i, box in enumerate(self.boxes):
            if len(box.lenses) > 0:
                string += f"Box {i}: {box}\n"
        return string

@dataclass
class Box:
    lenses: list[Lens] = field(default_factory=list)

    def remove_lens(self, new_lens: Lens):
        for i, lens in enumerate(self.lenses):
            if lens.label == new_lens.label:
                self.lenses.pop(i)
                return

    def replace_lens(self, new_lens: Lens):
        for i, lens in enumerate(self.lenses):
            if lens.label == new_lens.label:
                self.lenses[i] = new_lens
                return
            
        # The lens wasn't in the box
        self.lenses.append(new_lens)

    def focusing_power(self):
        total = 0
        for i, lens in enumerate(self.lenses):
            total += (i+1) * lens.focal_length
        return total


    def __repr__(self):
        string = ""
        for lens in self.lenses:
            string += f"[{lens}]"
        return string
            