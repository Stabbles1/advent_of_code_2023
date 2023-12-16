from facility import Box, Facility, Lens


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()

def solve(lines):
    facility = Facility()
    for substr in lines[0].split(","):
        lens = Lens.fromstr(substr)
        facility.execute_lens(lens)
    print(facility)
    return facility.focusing_power()

if __name__ == "__main__":
    lines = read_input("day_15/input.txt")
    print(solve(lines))
