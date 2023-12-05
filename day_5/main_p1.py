import input_parse
from map import MapRange

map_order = ["seed-to-soil",
             "soil-to-fertilizer","fertilizer-to-water","water-to-light","light-to-temperature","temperature-to-humidity","humidity-to-location",]

def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def translate(num, map:list[MapRange]) -> int:
    for map_range in map:
        if map_range.in_range(num):
            print(f"{num} was in {map}!")
            return num + map_range.offset
    # It wasn't in any mapping, so the same number comes out
    return num



def location_from_seed(seed, maps):
    current_num = seed
    for map_name in map_order:
        current_num = translate(current_num, maps[map_name])
    return current_num




def solve(lines: list[str]) -> int:
    seeds = (input_parse.read_seeds(lines[0]))
    print(seeds)
    maps = (input_parse.read_maps(lines[1:]))
    print(maps)
    locations = []
    for seed in seeds:
        locations.append(location_from_seed(seed, maps))
    return min(locations)

if __name__ == "__main__":
    lines = read_input("day_5/input.txt")
    print(solve(lines))
