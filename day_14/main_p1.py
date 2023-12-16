import time


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

def roll_up(dish, y, x):
    while True:
        if y>0 and dish[y-1][x] == ".":
            dish[y][x] = "."
            dish[y-1][x] = "O"
            y -= 1
        else:
            return

def roll_everything(dish) -> None:
    for y in range(len(dish)):
        for x in range(len(dish[0])):
            if dish[y][x] == "O":
                roll_up(dish, y, x)

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

def solve(lines):
    dish = populate_dish(lines)
    print_dish(dish)
    print()
    roll_everything(dish)
    print_dish(dish)
    return calculate_load(dish)


if __name__ == "__main__":
    lines = read_input("day_14/input.txt")
    print(solve(lines))
