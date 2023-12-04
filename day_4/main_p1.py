import re

from card import Card


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def str_to_int_list(side: str) -> list[int]:
    print(side)
    return [int(n) for n in side.strip().split(" ") if n != ""]


def solve(lines):
    total = 0
    for line in lines:
        regex_result = re.search(r":(.*?)\|(.*)", line)
        winning_side = regex_result.group(1)
        our_side = regex_result.group(2)
        card = Card(
            winning_numbers=str_to_int_list(winning_side),
            our_numbers=str_to_int_list(our_side),
        )
        total += card.calculate_score()
    return total


if __name__ == "__main__":
    lines = read_input("day_4/input.txt")
    print(solve(lines))
