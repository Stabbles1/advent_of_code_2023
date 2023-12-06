import input_parse
from map import MapRange

map_order = ["seed-to-soil",
             "soil-to-fertilizer","fertilizer-to-water","water-to-light","light-to-temperature","temperature-to-humidity","humidity-to-location",]

def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def translate(num, map:list[MapRange]) -> tuple[int, int]:
    min_closest_encounter = 99999999999
    for map_range in map:
        if map_range.in_range(num):
            translation = num + map_range.offset
            min_closest_encounter = min(min_closest_encounter, map_range.closest_encounter(num))
            return translation, min_closest_encounter
    # It wasn't in any mapping, so the same number comes out
    return num, min_closest_encounter

def location_from_seed(seed, maps) -> tuple[int, int]:
    current_num = seed
    min_closest_encounter = 9999999999
    for map_name in map_order:
        current_num, closest_encounter = translate(current_num, maps[map_name])
        min_closest_encounter = min(min_closest_encounter, closest_encounter)
    return current_num, min_closest_encounter

def solve(lines: list[str]) -> int:
    seed_ranges = input_parse.read_seeds(lines[0])
    maps = (input_parse.read_maps(lines[1:]))
    min_location = 9999999999
    for seed_range in seed_ranges:
        seed = seed_range[0]
        while seed < seed_range[0] + seed_range[1]:
            print(f"I'm going to stop at {seed_range[0] + seed_range[1]}")
            
            location, step = location_from_seed(seed, maps)
            print(f"{seed=} {location=}")
            min_location = min(min_location, location)
            step = max(step - 2, 1)
            seed += step

    return min_location

if __name__ == "__main__":
    lines = read_input("day_5/input.txt")
    print(solve(lines))
