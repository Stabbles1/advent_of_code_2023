import re

from card import Card


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def str_to_int_list(side: str) -> list[int]:
    return [int(n) for n in side.strip().split(" ") if n != ""]


def solve(lines):
    card_counts = {}
    # Start with 1 of each card
    for i in range(0,len(lines)):
        card_counts[i] = 1

    for card_number, line in enumerate(lines):
        regex_result = re.search(r":(.*?)\|(.*)", line)
        winning_side = regex_result.group(1)
        our_side = regex_result.group(2)
        card = Card(
            winning_numbers=str_to_int_list(winning_side),
            our_numbers=str_to_int_list(our_side),
        )
        score = card.calculate_score_p2()
        for i in range(card_number+1, card_number + score + 1):
            try:
                print(f"Adding {card_counts[card_number]} to {i}")
                card_counts[i] += card_counts[card_number]
            except KeyError:
                continue
    return sum(card_counts.values())




if __name__ == "__main__":
    lines = read_input("day_4/input.txt")
    print(solve(lines))
