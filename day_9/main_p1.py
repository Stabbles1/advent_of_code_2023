from history import History


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def solve(lines):
    total = 0
    for line in lines:
        current_history = History(tiers=[[int(n) for n in line.split(" ")]])
        current_history.populate()
        total += current_history.extrapolate()
    return total
    

if __name__ == "__main__":
    lines = read_input("day_9/input.txt")
    print(solve(lines))
