import copy
import itertools
import json
import re
import time
from functools import cache


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

@cache
def is_valid(combo:str, candidate: str, broken:str, num_of_unknown_locations:int) -> bool:
    broken=json.loads(broken)
    final_spring = ""
    unknowns_encountered = 0
    loop_counter = 0
    while loop_counter < len(candidate):
        if candidate[loop_counter] == "?":
            if combo[unknowns_encountered] == "1":
                final_spring += "#"
            else:
                final_spring += "."
            unknowns_encountered += 1
        else:
            final_spring += candidate[loop_counter]
        loop_counter += 1

    
    try:
        result = re.findall(r'(?:^|\.)*(#+)(?:\.|$)', final_spring)
        assert len(result) == len(broken)
        for i in range(0, len(result)):
            assert len(result[i]) == broken[i]
    except AssertionError:
        return False
    return final_spring

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
    broken_str = json.dumps(broken)
    num_of_unknown_locations = len(unknown_locations)
    formatter = '0' + str(num_of_unknown_locations) + 'b'
    for binint in range(0, 2**num_of_unknown_locations):
        result = is_valid(format(binint, formatter), layout, broken_str, num_of_unknown_locations)
        if result != False:
            valid_combinations.add(result)
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
        print(f"Number of ?: {simplified.count('?')}")
        start = time.time()
        total += num_of_valid_combinations(simplified, broken)
        print(f"Took {time.time() - start}")
    return total
    

if __name__ == "__main__":
    lines = read_input("day_12/input.txt")
    print(solve(lines))
