from dataclasses import dataclass, field


@dataclass
class RGB:
    rgb: str
    # red: int
    # green: int
    # blue: int


# @dataclass
# class Location:
#     x: int
#     y: int

#     def __hash__(self):
#         return hash(f"{self.x} {self.y}")


@dataclass
class Graph:
    tiles: dict[tuple, RGB]
    right_counter: int = 0
    left_counter: int = 0
    current_location: tuple = (0, 0, "D")  # x, y
    previous_direction: str = "D"
    route: list[tuple] = field(default_factory=list)

    def add_tiles(self, direction: str, length: str, rgb: str):
        for _ in range(int(length)):
            if direction == "R":
                if self.previous_direction == "U":
                    self.right_counter += 1
                elif self.previous_direction == "D":
                    self.left_counter += 1
                new_location = (
                    self.current_location[0] + 1,
                    self.current_location[1],
                    "R",
                )

            elif direction == "D":
                if self.previous_direction == "R":
                    self.right_counter += 1
                elif self.previous_direction == "L":
                    self.left_counter += 1
                new_location = (
                    self.current_location[0],
                    self.current_location[1] - 1,
                    "D",
                )

            elif direction == "L":
                if self.previous_direction == "D":
                    self.right_counter += 1
                elif self.previous_direction == "U":
                    self.left_counter += 1
                new_location = (
                    self.current_location[0] - 1,
                    self.current_location[1],
                    "L",
                )

            elif direction == "U":
                if self.previous_direction == "L":
                    self.right_counter += 1
                elif self.previous_direction == "R":
                    self.left_counter += 1
                new_location = (
                    self.current_location[0],
                    self.current_location[1] + 1,
                    "U",
                )

            else:
                raise Exception("Invalid direction")
            self.previous_direction = direction
            self.route.append(new_location)
            self.tiles[new_location[0:2]] = RGB(rgb)
            self.current_location = new_location

    def fill_surroundings(self, x, y):
        if (x, y) not in self.tiles:
            self.tiles[(x, y)] = RGB("Lava")
            self.fill_surroundings(x + 1, y)
            self.fill_surroundings(x - 1, y)
            self.fill_surroundings(x, y + 1)
            self.fill_surroundings(x, y - 1)

    def __str__(self):
        s = ""
        for y in range(200, -200, -1):
            for x in range(-100, 100):
                if (x, y) in self.tiles:
                    s += "#"
                else:
                    s += "."
            s += "\n"
        return s

    def fill(self):
        # This only works for right hand loops. Test and actual are both right
        print(self.left_counter)
        print(self.right_counter)
        for step in self.route:
            try:
                if step[2] == "R":
                    self.fill_surroundings(step[0], step[1] - 1)
                elif step[2] == "D":
                    self.fill_surroundings(step[0] - 1, step[1])
                elif step[2] == "L":
                    self.fill_surroundings(step[0], step[1] + 1)
                elif step[2] == "U":
                    self.fill_surroundings(step[0] + 1, step[1])
            except RecursionError:
                pass  # Give it a break
