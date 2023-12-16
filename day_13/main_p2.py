import time

from pattern import Pattern


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def get_patterns(lines) -> list[Pattern]:
    patterns = []
    current_pattern = Pattern(grid=[])
    for line in lines:
        if line != "":
            current_pattern.grid.append(line)
        else:
            patterns.append(current_pattern)
            current_pattern = Pattern(grid=[])
    patterns.append(current_pattern)
    return patterns

def solve(lines):
    start = time.time()
    patterns = get_patterns(lines)
    total_value = 0
    for pattern in patterns:
        result = pattern.smudgeless_value()
        if result is None:
            result = 0
        total_value += result
        print(total_value)
    print(f"Time taken: {time.time() - start}")
    return total_value
    

if __name__ == "__main__":
    lines = read_input("day_13/input.txt")
    print(solve(lines))
