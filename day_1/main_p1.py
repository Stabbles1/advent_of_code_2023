def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def get_first_and_last_numbers(line: str) -> int:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first = None
    last = None
    for char in line:
        if char not in numbers:
            continue
        if first is None:
            first = char
        last = char

    return int(f"{first}{last}")


if __name__ == "__main__":
    lines = read_input("day_1/input.txt")
    result = sum([get_first_and_last_numbers(line) for line in lines])
    print(result)
