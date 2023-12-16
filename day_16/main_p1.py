import sys
import time

from tile import Tile

sys.setrecursionlimit(10000)

def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def travel(grid: list[list[Tile]], y: int, x: int, y_delta: int, x_delta: int):
    # for line in grid:
    #     print(line)
    # print()
    # Check if out of bounds
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0]):
        return
    
    # y_delta  1 Down
    # y_delta -1 Up
    # x_delta -1 Left
    # x_delta  1 Right
    

    # Test for splitters first because we need to prevent infinite loops
    if grid[y][x].symbol == "|" and not grid[y][x].energised:
        grid[y][x].energise()
        if y_delta != 0: # Keep travelling in this direction
            travel(grid, y + y_delta, x + x_delta, y_delta, x_delta)
        else:
            # Split up and down
            travel(grid, y + 1, x,  1, 0)
            travel(grid, y - 1, x, -1, 0)

    elif grid[y][x].symbol == "-" and not grid[y][x].energised:
        grid[y][x].energise()
        if x_delta != 0: # Keep travelling in this direction
            travel(grid, y + y_delta, x + x_delta, y_delta, x_delta)
        else:
            # Split left and right
            travel(grid, y, x - 1, 0, -1)
            travel(grid, y, x + 1, 0, 1)
            

    grid[y][x].energise()
    if grid[y][x].symbol == ".":
        # Keep travelling in this direction
        travel(grid, y + y_delta, x + x_delta, y_delta, x_delta)
    


    elif grid[y][x].symbol == "\\":
        if y_delta == 1: # Deflect right
            travel(grid, y, x+1, 0, 1)
        elif y_delta == -1: # Delect left
            travel(grid, y, x-1, 0, -1)
        elif x_delta == 1: # Delect down
            travel(grid, y+1, x, 1, 0)
        elif x_delta == -1: # Delect up
            travel(grid, y-1, x, -1, 0)

    elif grid[y][x].symbol == "/":
        if y_delta == 1: # Delect left
            travel(grid, y, x-1, 0, -1)
        elif y_delta == -1: # Deflect right
            travel(grid, y, x+1, 0, 1)
        elif x_delta == 1: # Delect up
            travel(grid, y-1, x, -1, 0)
        elif x_delta == -1: # Delect down
            travel(grid, y+1, x, 1, 0)




def solve(lines):
    grid = []
    for line in lines:
        grid.append([Tile(symbol=char) for char in line])
    travel(grid, 0, 0, 0, 1)

    total_energised = 0
    for line in grid:
        for tile in line:
            if tile.energised:
                total_energised += 1
    return total_energised

if __name__ == "__main__":
    lines = read_input("day_16/input.txt")
    print(solve(lines))
