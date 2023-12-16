import time
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional


@dataclass
class Direction:
    delta_y: int = 0
    delta_x: int = 0


class Category(str, Enum):
    UNKNOWN = "."
    LOOP_SEGMENT = "S"
    INSIDE = "I"
    OUTSIDE = "O"

@dataclass
class Pipe:
    symbol: str
    connections: list[Direction]
    category: Category = Category.UNKNOWN
    placement_direction: Optional[Direction] = None

    def __repr__(self):
        if self.category == Category.LOOP_SEGMENT:
            if self.placement_direction.delta_y == 1:
                return "v"
            elif self.placement_direction.delta_y == -1:
                return "^"
            elif self.placement_direction.delta_x == 1:
                return ">"
            elif self.placement_direction.delta_x == -1:
                return "<"
        return self.category.value
    
    def __str__(self):
        if self.category == Category.LOOP_SEGMENT:
            if self.placement_direction.delta_y == 1:
                return "v"
            elif self.placement_direction.delta_y == -1:
                return "^"
            elif self.placement_direction.delta_x == 1:
                return ">"
            elif self.placement_direction.delta_x == -1:
                return "<"
        return self.category.value


PIPE_TYPES = {
    # Going up y decreases
    # Going left x decreases
    "|":Pipe(symbol="|", connections=[Direction(delta_y=1), Direction(delta_y=-1)]),
    "-":Pipe(symbol="-", connections=[Direction(delta_x=1), Direction(delta_x=-1)]),
    "L":Pipe(symbol="L", connections=[Direction(delta_y=-1), Direction(delta_x=1)]),
    "J":Pipe(symbol="J", connections=[Direction(delta_y=-1), Direction(delta_x=-1)]),
    "7":Pipe(symbol="7", connections=[Direction(delta_y=1), Direction(delta_x=-1)]),
    "F":Pipe(symbol="F", connections=[Direction(delta_y=1), Direction(delta_x=1)]),
    ".":Pipe(symbol=".", connections=[]),
    "S":Pipe(symbol="S", connections=[Direction(delta_y=1), Direction(delta_x=1),Direction(delta_y=-1), Direction(delta_x=-1)]),
}

@dataclass
class Maze:
    schematic: list[list[Pipe]] = field(default_factory=list)
    y_location:int = 0
    x_location:int = 0
    prev_y_location: int = 0
    prev_x_location: int = 0

    def __str__(self):
        chars = ""
        for line in self.schematic:
            for c in line:
                chars += str(c)
            chars += "\n"
        return chars

    def set_s_location(self):
        for y_index, y in enumerate(self.schematic):
            for x_index, x in enumerate(y):
                if len(self.schematic[y_index][x_index].connections) == 4:
                    self.s_x_location = x_index
                    self.s_y_location = y_index

    def connected(self, x_current:int, y_current:int, direction: Direction) -> bool:
        try:
            future_pipe: Pipe = self.schematic[y_current + direction.delta_y][x_current + direction.delta_x]
            for d in future_pipe.connections:
                if d.delta_x == direction.delta_x * -1 and d.delta_y == direction.delta_y * -1:
                    self.schematic[self.y_location][self.x_location].category = Category.LOOP_SEGMENT
                    self.schematic[self.y_location][self.x_location].placement_direction = direction # Should this be d?!
                    return True
            return False
        except IndexError:
            return False


    def step(self) -> None:
        # Search around the current location
        for direction in self.schematic[self.y_location][self.x_location].connections:
            if (self.y_location + direction.delta_y == self.prev_y_location and 
                self.x_location + direction.delta_x == self.prev_x_location):
                continue # We don't want to backtrack
            # Check if it's a valid connection
            if self.connected(self.x_location, self.y_location, direction):
                # Yes it's valid, make the step
                self.prev_x_location = self.x_location
                self.prev_y_location = self.y_location
                self.x_location = self.x_location + direction.delta_x
                self.y_location = self.y_location + direction.delta_y
                return
    
    def is_current_location_s(self) -> bool:
        return self.y_location == self.s_y_location and self.x_location == self.s_x_location

    def find_loop_size(self) -> int:
        self.set_s_location()
        self.y_location = self.s_y_location
        self.x_location = self.s_x_location

        self.step()
        steps_taken = 1
        while not self.is_current_location_s():
            self.step()
            steps_taken += 1
        return steps_taken


    def mark_unknowns_to_the_left(self, y, x, direction: Direction) -> int:
        marked_count = 0
        while True:
            if direction.delta_y == 1:
                # Placed down, therefore left is +x
                x += 1
            elif direction.delta_y == -1:
                # Placed up, therefore left is -x
                x -= 1
            elif direction.delta_x == 1:
                # Placed right, therefore left is -y
                y -= 1
            elif direction.delta_x == -1:
                # Placed left, therefore left is +y
                y += 1
            else:
                raise ValueError()
            
            if x < 0 or y < 0 or x >= len(self.schematic[0]) or y >= len(self.schematic):
                return marked_count
            pipe_under_consideration: Pipe = self.schematic[y][x]
            if pipe_under_consideration.category == Category.UNKNOWN:
                pipe_under_consideration.category = Category.INSIDE
                marked_count += 1
            elif pipe_under_consideration.category == Category.LOOP_SEGMENT:
                return marked_count
            
    def mark_unknowns_to_the_right(self, y, x, direction: Direction) -> int:
        marked_count = 0
        while True:
            if direction.delta_y == 1:
                # Placed down, therefore right is -x
                x -= 1
            elif direction.delta_y == -1:
                # Placed up, therefore right is +x
                x += 1
            elif direction.delta_x == 1:
                # Placed right, therefore right is +y
                y += 1
            elif direction.delta_x == -1:
                # Placed left, therefore right is -y
                y -= 1
            else:
                raise ValueError()
            
            if x < 0 or y < 0 or x >= len(self.schematic[0]) or y >= len(self.schematic):
                return marked_count
            pipe_under_consideration: Pipe = self.schematic[y][x]
            if pipe_under_consideration.category == Category.UNKNOWN:
                pipe_under_consideration.category = Category.INSIDE
                marked_count += 1
            elif pipe_under_consideration.category == Category.LOOP_SEGMENT:
                return marked_count

    def fill_neighbours(self, y, x):
        marked_count = 0
        try:
            target_pipes = [
                self.schematic[y][x],
                self.schematic[y-1][x],
                self.schematic[y+1][x],
                self.schematic[y][x-1],
                self.schematic[y][x+1],
            ]
            if any([tp.category == Category.INSIDE for tp in target_pipes]):
                for tp in target_pipes:
                    if tp.category == Category.UNKNOWN:
                        tp.category = Category.INSIDE
                        marked_count += 1
            return marked_count
        except IndexError:
            return marked_count


    def mark_enclosed(self) -> int:
        marked_count = 0
        for y, line in enumerate(self.schematic):
            for x, pipe in enumerate(line):
                if pipe.category != Category.LOOP_SEGMENT:
                    marked_count += self.fill_neighbours(y, x)
                    continue
                marked_count += self.mark_unknowns_to_the_left(y, x, pipe.placement_direction)
                #marked_count += self.mark_unknowns_to_the_right(y, x, pipe.placement_direction)
                #time.sleep(1)
        print(self)
        return marked_count
