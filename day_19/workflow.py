import re
from dataclasses import dataclass

from scrap import Scrap


@dataclass
class Condition:
    label: str
    operator: str
    value: int
    destination: str

    def process_scrap_step(self, scrap: Scrap) -> str:
        if self.operator == ">":
            if scrap.__getattribute__(self.label) > self.value:
                return self.destination
        elif self.operator == "<":
            if scrap.__getattribute__(self.label) < self.value:
                return self.destination
        return ""


def condition_from_string(s: str) -> Condition:
    matches = re.search(r"(\w)(.)(\d+)\:(\w+)", s)
    return Condition(
        label=matches.group(1),
        operator=matches.group(2),
        value=int(matches.group(3)),
        destination=matches.group(4),
    )


@dataclass
class Workflow:
    name: str
    conditions: list[Condition]
    default: str


def wf_from_string(s: str) -> Workflow:
    matches = re.search(r"(\w+)\{(.*)\}", s)
    name = matches.group(1)
    conditions = []
    rules = matches.group(2)
    for rule in rules.split(","):
        if ":" in rule:
            conditions.append(condition_from_string(rule))
        else:
            default = rule

    return Workflow(
        name=name,
        conditions=conditions,
        default=default,
    )
