import re


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def solve(lines):
    lr_sequence = lines[0]

    mapping = {}
    for line in lines[2:]:
        left = re.search(r'\((\w+)', line).group(1)
        right = re.search(r'(\w+)\)', line).group(1)
        mapping[line.split(" ")[0]] = [left, right]
    lr_count = 0
    steps_taken = 0
    current_location = "AAA"
    while True:
        if lr_count == len(lr_sequence):
            lr_count = 0
        if lr_sequence[lr_count] == "L":
            current_location = mapping[current_location][0]
        else :
            current_location = mapping[current_location][1]
        steps_taken += 1
        lr_count += 1
        if current_location == "ZZZ":
            return steps_taken 
    

if __name__ == "__main__":
    lines = read_input("day_8/input.txt")
    print(solve(lines))
