import copy


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def toggle_surroundings(current_grid, next_grid, y, x) -> None:
    if y > 0 and current_grid[y - 1][x] == ".":  # Up
        next_grid[y - 1][x] = "O"
    if current_grid[y + 1][x] == ".":  # Down
        next_grid[y + 1][x] = "O"
    if current_grid[y][x + 1] == ".":  # Right
        next_grid[y][x + 1] = "O"
    if x > 0 and current_grid[y][x - 1] == ".":  # Left
        next_grid[y][x - 1] = "O"


def print_grid(grid):
    s = ""
    for line in grid:
        for char in line:
            s += char
        s += "\n"
    print(s)


def reset_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == "O" or grid[y][x] == "S":
                grid[y][x] = "."


def take_first_step(current_grid) -> list[list[str]]:
    # Get a fresh copy of the grid
    next_grid = copy.deepcopy(current_grid)
    reset_grid(next_grid)

    for y in range(len(current_grid)):
        for x in range(len(current_grid[0])):
            if current_grid[y][x] == "S" or current_grid[y][x] == "O":
                toggle_surroundings(current_grid, next_grid, y, x)
    return next_grid


def count_plots(grid: list[list[str]]):
    total = 0
    for line in grid:
        total += line.count("O")
    return total


def solve(lines, steps: int):
    grid = []
    for line in lines:
        grid.append(list(line))
    for _ in range(steps):
        grid = take_first_step(copy.deepcopy(grid))
    return count_plots(grid)


if __name__ == "__main__":
    lines = read_input("day_21/input.txt")
    print(solve(lines, steps=64))
