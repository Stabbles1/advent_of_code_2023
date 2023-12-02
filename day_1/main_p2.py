def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def spelled_check(line: str) -> None | str:
    spelled_numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for spelled_number in spelled_numbers.keys():
        if line[0 : len(spelled_number)] == spelled_number:
            return spelled_numbers[spelled_number]


def get_first_and_last_numbers(line: str) -> int:
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    first = None
    last = None

    for index, char in enumerate(line):
        if char not in numbers:
            spelled_result = spelled_check(line[index:])
            if spelled_result is None:
                continue
            else:
                char = spelled_result

        if first is None:
            first = char
        last = char

    return int(f"{first}{last}")


if __name__ == "__main__":
    lines = read_input("day_1/input.txt")
    result = sum([get_first_and_last_numbers(line) for line in lines])
    print(result)
