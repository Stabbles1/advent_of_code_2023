import copy

from maze import PIPE_TYPES, Maze


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def solve(lines):
    #Populate the maze
    maze = Maze()
    for line in lines:
        maze.schematic.append([copy.deepcopy(PIPE_TYPES[c]) for c in line])
    maze.find_loop_size()
    print(maze)
    return maze.mark_enclosed()
    
    

if __name__ == "__main__":
    lines = read_input("day_10/input.txt")
    print(solve(lines))
