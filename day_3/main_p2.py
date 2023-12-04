import itertools


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


DIGITS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

# all_gear_numbers key is the coordinates of the first digit of the whole number
# the value is the whole number
all_gear_numbers = {}


def is_number(char):
    return char in DIGITS


def backtrack(line, x, y) -> dict:
    left_offset = 0
    right_offset = 0
    for right in range(x, 99999, 1):  # Counting forwards
        try:
            if is_number(line[right]):
                right_offset += 1
            else:
                break
        except IndexError:
            break
    for left in range(x - 1, -99999, -1):  # Counting backwards
        try:
            if is_number(line[left]):
                left_offset -= 1
            else:
                break
        except IndexError:
            break
    
    t = {}
    t[f"{y}:{x+left_offset}"] = int(line[x + left_offset : x + right_offset])
    return t

def count_surrounding_numbers(lines, y: int, x: int) -> int:
    numbers = {}
    for cur_y, cur_x in itertools.product([y - 1, y, y + 1], [x - 1, x, x + 1]):
        try:
            if is_number(lines[cur_y][cur_x]):
                numbers = numbers | (backtrack(lines[cur_y], cur_x, cur_y))
        except IndexError:
            continue
    return len(numbers)

def gear_ratio(lines, y: int, x: int) -> int:
    numbers = {}
    for cur_y, cur_x in itertools.product([y - 1, y, y + 1], [x - 1, x, x + 1]):
        try:
            if is_number(lines[cur_y][cur_x]):
                numbers = numbers | (backtrack(lines[cur_y], cur_x, cur_y))
        except IndexError:
            continue
    numbers = list(numbers.values())
    assert len(numbers) == 2
    return numbers[0] * numbers[1]


def solve(lines):
    total = 0
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == '*' and count_surrounding_numbers(lines, y, x) == 2:
                print(f"found a gear at {y} {x}")
                total += gear_ratio(lines, y, x)
    return total


if __name__ == "__main__":
    lines = read_input("day_3/input.txt")
    print(solve(lines))
