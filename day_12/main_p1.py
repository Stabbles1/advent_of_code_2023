import copy
import itertools
import json
import re
from functools import cache


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()
    
@cache
def is_valid(combo:str, candidate: str, broken:str) -> bool:
    candidate=json.loads(candidate)
    combo=json.loads(combo)
    broken=json.loads(broken)
    for n in combo:
        candidate[n] = "#"
    # Reconstruct the string
    sping_string = ""
    for spring in candidate:
        if spring == "?":
            sping_string += "."
        else: 
            sping_string += spring
    try:
        result = re.findall(r'(?:^|\.)*(#+)(?:\.|$)', sping_string)
        assert len(result) == len(broken)
        for i in range(0, len(result)):
            assert len(result[i]) == broken[i]
    except AssertionError:
        return False
    return sping_string

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

    valid_combinations = set()
    for combo in itertools.product(unknown_locations, repeat=number_of_brokens_to_place):
        # Make sure there are no dupes in the combo
        if len(set(combo)) != len(combo):
            continue
        combo = sorted(list(combo))
        if is_valid(json.dumps(combo), json.dumps(layout_list), json.dumps(broken)) != False:
            valid_combinations.add(is_valid(json.dumps(combo), json.dumps(layout_list), json.dumps(broken)))
    return len(valid_combinations)

def parse_line(line) -> tuple[str, list[int]]:
    layout, p2 = line.split(" ")
    broken = [int(n) for n in p2.split(",")]
    return layout, broken

def simplify(layout: str, broken:list[int]):
    # If there is a broken pipe at the start or end, we can extrapolate
    layout_list = [c for c in layout]
    # Pad out the left
    for index in range(len(layout_list)):
        if layout_list[index] == ".":
            continue
        if layout_list[index] == "?":
            break # The dream is dead
        if layout_list[index] == "#":
            for broke in range(index+1, broken[0]+index):
                layout_list[broke] = "#"
            break
    # Pad out the right
    for index in range(-1, len(layout_list) * -1, -1):
        if layout_list[index] == ".":
            continue
        if layout_list[index] == "?":
            break # The dream is dead
        if layout_list[index] == "#":
            for broke in range(index-1, (broken[-1] * -1) +index, -1):
                layout_list[broke] = "#"
            break



    simplified = ""
    for c in layout_list:
        simplified += c
    print(f"{simplified=}")
    return simplified, broken

def solve(lines) -> int:
    total = 0
    for line in lines:
        simplified, broken = simplify(*parse_line(line))
        total += num_of_valid_combinations(simplified, broken)
    return total
    

if __name__ == "__main__":
    lines = read_input("day_12/input.txt")
    print(solve(lines))
