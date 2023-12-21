from copy import deepcopy

from block import Block, Coordinates


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def get_box_coordinates(size: int) -> list[Coordinates]:
    all_coordinates = []
    # Populate the y's
    for y in range(size):
        all_coordinates.append(Coordinates(y=y, x=size))

    # Populate the x's
    for x in range(size):
        all_coordinates.append(Coordinates(y=size, x=x))
    all_coordinates.append(Coordinates(y=size, x=size))
    return all_coordinates


def best_between_2_points(
    grid, valid_paths, current_path, start_y: int, start_x: int, end_y: int, end_x: int
):
    path = deepcopy(path)
    for symbol, y, x in [("U", -1, 0), ("D", 1, 0), ("L", 0, -1), ("R", 0, 1)]:
        if start_y + y == end_y and start_x + x == end_x:
            # We've arrived
            valid_paths.append(grid)


def best_path(grid: list[list[Block]], end_y: int, end_x: int):
    # Gather all the optimised values from around this tile
    window_size = 5
    nearby_optimised = []
    for y in range(max(0, end_y - window_size), min(len(grid), end_y + window_size)):
        for x in range(
            max(0, end_x - window_size), min(len(grid), end_x + window_size)
        ):
            if grid[y][x].is_optimised:
                nearby_optimised.append(grid[y][x])

    print(f"{nearby_optimised=}")
    for nearby in nearby_optimised:
        valid_paths = []
        for each_best_path in nearby.best_paths:
            result = best_between_2_points(
                grid,
                valid_paths,
                each_best_path,
                nearby.coordinates.y,
                nearby.coordinates.x,
                end_y,
                end_x,
            )


def solve(lines):
    grid = []
    for y, line in enumerate(lines):
        grid.append(
            [
                Block(heat_loss=int(heat_loss), coordinates=Coordinates(x=x, y=y))
                for x, heat_loss in enumerate(line)
            ]
        )
    grid[0][0].best_value = 0
    grid[0][0].best_path = ["U"]
    for box_size in range(1, len(grid)):
        print(f"{box_size=}")
        box_coordinates = get_box_coordinates(box_size)
        for coordinates in box_coordinates:
            best_path(grid, coordinates.y, coordinates.x)

    return grid[-1][-1].best_value


if __name__ == "__main__":
    lines = read_input("day_17/input.txt")
    print(solve(lines))
