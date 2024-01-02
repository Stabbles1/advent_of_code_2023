import re
from abc import abstractmethod
from dataclasses import dataclass, field

lows = 0
highs = 0


@dataclass
class Instruction:
    signal: int
    sender: str
    receiver: str

    def execute(self):
        print(self)
        global lows, highs
        if self.signal == 0:
            circuit[self.receiver].receive_low_input()
            lows += 1
        else:
            circuit[self.receiver].receive_high_input()
            highs += 1

    def __str__(self):
        hl = "low" if self.signal == 0 else "high"
        return f"{self.sender} -{hl}-> {self.receiver}"


action_list: list[Instruction] = []


@dataclass
class Gate:
    name: str
    state: int = 0
    inputs: list[object] = field(default_factory=list)
    outputs: list[object] = field(default_factory=list)

    @abstractmethod
    def receive_low_input(self):
        ...

    @abstractmethod
    def receive_high_input(self):
        ...


@dataclass
class FlipFlop(Gate):  # %
    def receive_high_input(self):
        return  # Nothing happens on high pulses

    def receive_low_input(self):
        if self.state == 0:
            for output in self.outputs:
                action_list.append(
                    Instruction(signal=1, sender=self.name, receiver=output.name)
                )
                self.state = 1
        else:
            for output in self.outputs:
                action_list.append(
                    Instruction(signal=0, sender=self.name, receiver=output.name)
                )
                self.state = 0


@dataclass
class Conjunction(Gate):
    def receive_input(self):
        if any([input.state == 0 for input in self.inputs]):
            for output in self.outputs:
                action_list.append(
                    Instruction(signal=1, sender=self.name, receiver=output.name)
                )
                self.state = 1
            return
        # All inputs were high, so send low
        for output in self.outputs:
            action_list.append(
                Instruction(signal=0, sender=self.name, receiver=output.name)
            )
            self.state = 0

    def receive_low_input(self):
        self.receive_input()

    def receive_high_input(self):
        self.receive_input()


@dataclass
class Broadcaster(Gate):
    def receive_high_input(self):
        for output in self.outputs:
            action_list.append(
                Instruction(signal=1, sender=self.name, receiver=output.name)
            )
            self.state = 1

    def receive_low_input(self):
        for output in self.outputs:
            action_list.append(
                Instruction(signal=0, sender=self.name, receiver=output.name)
            )
            self.state = 0


circuit: dict[str, Gate] = {}


def add_gate_to_circuit(line: str) -> None:
    matches = re.search(r"(\w+) \-\> (.*)", line)
    name = matches.group(1)
    outputs = matches.group(2)

    if line[0] == "&":
        circuit[name] = Conjunction(name=name)
    elif line[0] == "%":
        circuit[name] = FlipFlop(name=name)
    elif line[0] == "b":
        circuit[name] = Broadcaster(name=name)
    else:
        raise NotImplementedError()


def add_outputs_to_gate(line: str) -> None:
    matches = re.search(r"(\w+) \-\> (.*)", line)
    name = matches.group(1)
    outputs = matches.group(2)
    for output_name in outputs.split(", "):
        if output_name not in circuit:
            circuit[output_name] = Gate(name=output_name)
        circuit[output_name].inputs.append(circuit[name])
        circuit[name].outputs.append(circuit[output_name])
    return
