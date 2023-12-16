import json
import time
from copy import copy, deepcopy
from functools import cache


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def populate_dish(lines) -> list[list[str]]:
    dish = []
    for line in lines:
        row = []
        for char in line:
            row.append(char)
        dish.append(row)
    return dish

def roll_delta(dish, y, x, y_delta, x_delta):
    while True:
        if y+y_delta < 0 or y + y_delta >= len(dish) or x+x_delta < 0 or x + x_delta >= len(dish[0]):
            return
        if dish[y+y_delta][x+x_delta] == ".":
            dish[y][x] = "."
            dish[y+y_delta][x+x_delta] = "O"
            y += y_delta
            x += x_delta
        else:
            return


def roll_everything(dish, y_delta, x_delta) -> None:
    if y_delta == -1:
        for y in range(len(dish)):
            for x in range(len(dish[0])):
                if dish[y][x] == "O":
                    roll_delta(dish, y, x, y_delta, x_delta)

    if y_delta == 1:
        for y in range(len(dish) -1, -1, -1):
            for x in range(len(dish[0])):
                if dish[y][x] == "O":
                    roll_delta(dish, y, x, y_delta, x_delta)

    if x_delta == -1:
        for x in range(len(dish[0])):
            for y in range(len(dish)):
                if dish[y][x] == "O":
                    roll_delta(dish, y, x, y_delta, x_delta)

    if x_delta == 1:
        for x in range(len(dish[0]) -1, -1, -1):
            for y in range(len(dish)):
                if dish[y][x] == "O":
                    roll_delta(dish, y, x, y_delta, x_delta)

    


def calculate_load(dish) -> int:
    total = 0
    multiplier = len(dish) 
    for row in dish:
        for location in row:
            if location == "O":
                total += multiplier
        multiplier -= 1
    return total

def print_dish(dish):
    for row in dish:
        print(row)
    print()

@cache
def spin(dish: str):
    dish = json.loads(dish)
    for y_delta, x_delta in [(-1, 0), (0, -1), (+1, 0), (0, +1)]:
        roll_everything(dish, y_delta, x_delta)
    return json.dumps(dish)

def solve(lines):
    dish = populate_dish(lines)
    print_dish(dish)
    dishstr = json.dumps(dish)
    for i in range(1000000000): # Let it cook
        dishstr = spin(dishstr)

    
    return calculate_load(json.loads(dishstr))


if __name__ == "__main__":
    lines = read_input("day_14/input.txt")
    print(solve(lines))
