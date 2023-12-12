import copy
import itertools
import re


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()
    
def is_valid(candidate: str, broken:list[int]) -> bool:
    try:
        result = re.findall(r'(?:^|\.)*(#+)(?:\.|$)', candidate)
        assert len(result) == len(broken)
        for i in range(0, len(result)):
            assert len(result[i]) == broken[i]
    except AssertionError:
        print(f"{candidate} is invalid")
        return False
    print(f"{candidate} VALID")
    return True


def num_of_valid_combinations(layout: str, broken:list[int]) -> int:
    broken_total = sum(broken)
    already_broken_total = len([spring for spring in layout if spring=='#'])
    number_of_brokens_to_place = broken_total - already_broken_total
    layout_list = [c for c in layout]
    unknown_locations = []
    for i, spring in enumerate(layout_list):
        if spring == "?":
            unknown_locations.append(i)

    all_combinations = []
    for i in range(0,number_of_brokens_to_place):
        all_combinations.append(unknown_locations)
    print(f"{already_broken_total=} {broken_total=}")
    print(all_combinations)

    valid_combinations = set()
    for combo in itertools.product(unknown_locations, repeat=number_of_brokens_to_place):
        # Make sure there are no dupes in the combo
        if len(set(combo)) != len(combo):
            continue
        current_layout = copy.copy(layout_list)
        for n in combo:
            current_layout[n] = "#"
        # Reconstruct the string
        sping_string = ""
        for spring in current_layout:
            if spring == "?":
                sping_string += "."
            else: 
                sping_string += spring
        if is_valid(sping_string, broken):
            valid_combinations.add(sping_string)
    return len(valid_combinations)

def parse_line(line) -> tuple[str, list[int]]:
    layout, p2 = line.split(" ")
    broken = [int(n) for n in p2.split(",")]
    return layout, broken


def solve(lines) -> int:
    total = 0
    for line in lines:
        total += num_of_valid_combinations(*parse_line(line))
    return total
    

if __name__ == "__main__":
    lines = read_input("day_12/input.txt")
    print(solve(lines))
