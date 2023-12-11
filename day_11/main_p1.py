from star import Star


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def expand_rows(lines: list[str]):
    rows_to_expand = []
    for i, row in enumerate(lines):
        empty = True
        for char in row:
            if char == "#":
                empty = False
        if empty:
            rows_to_expand.append(i)

    expanded_counter = 0
    for i in rows_to_expand:
        lines.insert(i+expanded_counter, '.'*len(lines[0]))
        expanded_counter+=1
    return lines

def expand_columns(lines: list[str]):
    cols_to_expand = []
    for x in range(0, len(lines[0])):
        empty = True
        for y in range(0, len(lines)):
            if lines[y][x] == "#":
                empty = False
        if empty:
            cols_to_expand.append(x)

    for y, line in enumerate(lines):
        chars = ""
        for x, char in enumerate(line):
            if x in cols_to_expand:
                chars += ".."
            else:
                chars += char
        lines[y] = chars

    return lines

def expand(lines):
    return expand_columns(expand_rows(lines))
    
def get_stars(expanded) -> list[Star]:
    all_stars = []
    id = 1
    for y in range(0, len(expanded)):
        for x in range(0, len(expanded[0])):
            if expanded[y][x] == "#":
                all_stars.append(Star(id=id, x=x, y=y))
                id += 1
    return all_stars



def solve(lines):
    expanded = expand(lines)
    all_stars = get_stars(expanded)
    for i in range(0, len(all_stars)):
        all_stars[i].set_total_length(all_stars[i:])
    return sum([star.total_length for star in all_stars])
    

if __name__ == "__main__":
    lines = read_input("day_11/input.txt")
    print(solve(lines))
