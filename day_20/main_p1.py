import circuit as circuit


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def push_button():
    print("-----Pushing------")
    circuit.action_list.append(
        circuit.Instruction(signal=0, sender="button", receiver="broadcaster")
    )
    while circuit.action_list:
        circuit.action_list[0].execute()
        circuit.action_list.pop(0)


def solve(lines):
    for line in lines:
        circuit.add_gate_to_circuit(line)
    for line in lines:
        circuit.add_outputs_to_gate(line)
    for _ in range(1000):
        push_button()
    return circuit.lows * circuit.highs


if __name__ == "__main__":
    lines = read_input("day_20/input.txt")
    print(solve(lines))
