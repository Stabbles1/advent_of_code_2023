import gate


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def push_button():
    print("-----Pushing------")
    gate.action_list.append(
        gate.Instruction(signal=0, sender="button", receiver="broadcaster")
    )
    while gate.action_list:
        gate.action_list[0].execute()
        gate.action_list.pop(0)


def solve(lines):
    for line in lines:
        gate.add_gate_to_circuit(line)
    for line in lines:
        gate.add_outputs_to_gate(line)
    for _ in range(1000):
        push_button()
    return gate.lows * gate.highs


if __name__ == "__main__":
    lines = read_input("day_20/input.txt")
    print(solve(lines))
