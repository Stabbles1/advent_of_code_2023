import re
from math import lcm

from node import Node


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()
    
def all_nodes_complete(nodes, steps_taken) -> bool:
    for node in nodes:
        node.is_complete(steps_taken)
    return all([len(node.pattern)>0 for node in nodes])

def solve(lines):
    lr_sequence = lines[0]

    mapping = {}
    for line in lines[2:]:
        left = re.search(r'\((\w+)', line).group(1)
        right = re.search(r'(\w+)\)', line).group(1)
        mapping[line.split(" ")[0]] = [left, right]
    lr_count = 0
    steps_taken = 0
    active_nodes = []
    for node_label in mapping.keys():
        if node_label[-1] == "A":
        #if node_label == "DQA":
            active_nodes.append(Node(starting_label=node_label, label=node_label))
    while all_nodes_complete(active_nodes, steps_taken) == False:
        for active_node in active_nodes:
            if lr_count == len(lr_sequence):
                lr_count = 0
            if lr_sequence[lr_count] == "L":
                active_node.label = mapping[active_node.label][0]
            else :
                active_node.label = mapping[active_node.label][1]
        steps_taken += 1
        lr_count += 1
        
    common_multiple = lcm(*[node.pattern[0] for node in active_nodes])
    return common_multiple
    

if __name__ == "__main__":
    lines = read_input("day_8/input.txt")
    print(solve(lines))
