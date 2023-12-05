import re

from map import MapRange


def read_seeds(line:str) -> list[int]:
    regex_result = re.search(r':\s+(.*)', line).group(1)
    return [int(seed) for seed in regex_result.split(" ")]

def read_maps(lines:list[str]) -> dict[list[map]]:
    all_maps = {}
    current_map_name = ""
    current_map_ranges = []
    for line in lines:
        print(f"Current line:{line}")
        if "map" in line:
            map_name = re.search(r'(.*?)\s', line).group(1)
            current_map_name = map_name
            current_map_ranges = []
        elif line == "" and current_map_name != "":
            all_maps[current_map_name] = current_map_ranges
        elif line != "" and current_map_name != "": #There are numbers
            nums = [int(n) for n in line.split(" ")]
            current_map_ranges.append(MapRange(**{"dest_range_start": nums[0],
            "src_range_start": nums[1],
            "range_len": nums[2]}))
            

    return all_maps