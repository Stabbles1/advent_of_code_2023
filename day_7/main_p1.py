from hand import Hand


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()

def solve(lines):
    hands = []
    for line in lines:
        cards, bid = line.split(" ")
        hands.append(Hand(cards=cards, bid=int(bid)))
    
    for hand in hands:
        hand.calc_score()
    sorted_hands = sorted(hands, key=lambda x: x.calc_score())

    total_winnings=0
    for rank, hand in enumerate(sorted_hands):
        total_winnings += (rank + 1) * hand.bid
    return total_winnings
    
    

if __name__ == "__main__":
    lines = read_input("day_7/input.txt")
    print(solve(lines))
