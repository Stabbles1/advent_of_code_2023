import sys

from graph import Graph

sys.setrecursionlimit(10000)


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


def solve(lines):
    graph = Graph(tiles={})
    for line in lines:
        direction, length, rgb = line.split(" ")
        graph.add_tiles(direction, length, rgb)
    print(graph)
    graph.fill()
    print(graph)
    return len(graph.tiles)


if __name__ == "__main__":
    lines = read_input("day_18/input.txt")
    print(solve(lines))
