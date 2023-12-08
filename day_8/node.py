from dataclasses import dataclass, field


@dataclass
class Node:
    starting_label: str
    label: str
    pattern: list[int] = field(default_factory=list)
    
    def is_complete(self, steps_taken):
        if self.label[-1] == "Z":
            try:
                self.pattern.append(steps_taken - self.pattern[-1])
            except:
                self.pattern.append(steps_taken)
            return True
        return False
    
    def __repr__(self):
        return f"{self.starting_label} - {self.pattern}"