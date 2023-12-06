
def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()

def winning_moves(time:int, record:int) -> int:
    winning_moves_counter = 0
    for hold_time in range(0, time):
        distance = hold_time * (time-hold_time)
        if distance > record:
            winning_moves_counter += 1
        
    return winning_moves_counter

def solve(times: list[int], distances: list[int]) -> int:
    product = 1
    for race_number in range(len(times)):
        time = times[race_number]
        record = distances[race_number]
        product *= winning_moves(time, record)
    return product

if __name__ == "__main__":
    lines = read_input("day_6/input.txt")
    print(solve(times=[42899189], distances=[308117012911467]))
