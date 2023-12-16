def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def hash_char(char: str, initialisation: int) -> int:
    asc_value = list(bytes(char, "ascii"))[0]
    current_value = asc_value + initialisation
    current_value *= 17
    return current_value % 256

def hash(input: str) -> int:
    current_value = 0
    for char in input:
        current_value = hash_char(char, current_value)
    return current_value

def solve(lines):
    total = 0
    for substr in lines[0].split(","):
        total += hash(substr)
    return total

if __name__ == "__main__":
    lines = read_input("day_15/input.txt")
    print(solve(lines))
