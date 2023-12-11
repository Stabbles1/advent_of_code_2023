from star import Star


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def get_y_wormholes(lines: list[str]):
    wormholes = []
    for i, row in enumerate(lines):
        empty = True
        for char in row:
            if char == "#":
                empty = False
        if empty:
            wormholes.append(i)
    return wormholes

def get_x_wormholes(lines: list[str]):
    wormholes = []
    for x in range(0, len(lines[0])):
        empty = True
        for y in range(0, len(lines)):
            if lines[y][x] == "#":
                empty = False
        if empty:
            wormholes.append(x)
    return wormholes
    
def get_stars(lines, 
              expansion_rate: int, 
              x_wormholes:list[int], 
              y_wormholes:list[int]) -> list[Star]:
    expansion_rate -= 1
    all_stars = []
    id = 1
    for y in range(0, len(lines)):
        for x in range(0, len(lines[0])):
            if lines[y][x] == "#":
                wormholed_x = len([hole for hole in x_wormholes if x > hole])
                wormholed_y = len([hole for hole in y_wormholes if y > hole])
                all_stars.append(Star(id=id, x=x+(wormholed_x*expansion_rate), y=y+(wormholed_y*expansion_rate)))
                id += 1
    return all_stars


def solve(lines, expansion_rate: int):
    x_wormholes = get_x_wormholes(lines)
    y_wormholes = get_y_wormholes(lines)
    all_stars = get_stars(lines, expansion_rate, x_wormholes, y_wormholes)
    for i in range(0, len(all_stars)):
        all_stars[i].set_total_length(all_stars[i:])
    return sum([star.total_length for star in all_stars])
    

if __name__ == "__main__":
    lines = read_input("day_11/input.txt")
    print(solve(lines, expansion_rate=1000000))
