import math

import circuit as circuit


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def push_button(x: int) -> bool:
    circuit.action_list.append(
        circuit.Instruction(signal=0, sender="button", receiver="broadcaster")
    )
    while circuit.action_list:
        if (
            circuit.action_list[0].receiver == "rx"
            and circuit.action_list[0].signal == 0
        ):
            return True
        elif (
            circuit.action_list[0].sender in ["pq", "fg", "dk", "fm"]
            and circuit.action_list[0].signal == 1
        ):
            print(f"{x=} {circuit.action_list[0].sender=}")

        circuit.action_list[0].execute()
        circuit.action_list.pop(0)
    return False


def solve(lines):
    return math.lcm(3793, 3929, 4001, 4007)
    for line in lines:
        circuit.add_gate_to_circuit(line)
    for line in lines:
        circuit.add_outputs_to_gate(line)
    x = 0
    while True:
        x += 1
        if push_button(x):
            return x


if __name__ == "__main__":
    lines = read_input("day_20/input.txt")
    print(solve(lines))
