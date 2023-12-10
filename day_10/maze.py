import time
from dataclasses import dataclass, field


@dataclass
class Direction:
    delta_y: int = 0
    delta_x: int = 0


@dataclass
class Pipe:
    symbol: str
    connections: list[Direction]

    def __repr__(self):
        return self.symbol

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

    def set_s_location(self):
        for y_index, y in enumerate(self.schematic):
            for x_index, x in enumerate(y):
                if len(self.schematic[y_index][x_index].connections) == 4:
                    self.s_x_location = x_index
                    self.s_y_location = y_index

    def connected(self, x_current:int, y_current:int, direction: Direction) -> bool:
        try:
            future_pipe: Pipe = self.schematic[y_current + direction.delta_y][x_current + direction.delta_x]
            print(f"We're trying to connect to {future_pipe} via {direction}")
            for d in future_pipe.connections:
                if d.delta_x == direction.delta_x * -1 and d.delta_y == direction.delta_y * -1:
                    return True
            return False
        except IndexError:
            return False


    def step(self) -> None:
        print(f"y={self.y_location} x={self.x_location}")
        # Search around the current location
        for direction in self.schematic[self.y_location][self.x_location].connections:
            if (self.y_location + direction.delta_y == self.prev_y_location and 
                self.x_location + direction.delta_x == self.prev_x_location):
                continue # We don't want to backtrack
            # Check if it's a valid connection
            if self.connected(self.x_location, self.y_location, direction):
                print(f"Connected! {self.x_location}, {self.y_location}, {direction}")
                # Yes it's valid, make the step
                self.prev_x_location = self.x_location
                self.prev_y_location = self.y_location
                self.x_location = self.x_location + direction.delta_x
                self.y_location = self.y_location + direction.delta_y
                return
            print(f"Disonnected! {self.x_location}, {self.y_location}, {direction}")
    
    def is_current_location_s(self) -> bool:
        return self.y_location == self.s_y_location and self.x_location == self.s_x_location

    def find_loop_size(self) -> int:
        self.set_s_location()
        print(self.s_x_location, self.s_y_location)
        self.y_location = self.s_y_location
        self.x_location = self.s_x_location

        self.step()
        steps_taken = 1
        while not self.is_current_location_s():
            self.step()
            steps_taken += 1
        return steps_taken







