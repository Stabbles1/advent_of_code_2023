from dataclasses import dataclass, field
import re


@dataclass
class Turn:
    red: int
    green: int
    blue: int


@dataclass
class Game:
    id: int
    turns: list[Turn] = field(default_factory=list)

    def add_turn(self, turn_info: str) -> None:
        # turn_info example:
        # 9 blue, 10 green, 4 red
        colour_counts = {}
        for colour in ["red", "green", "blue"]:
            regex_result = re.search(f"(\d+) {colour}", turn_info)
            if not regex_result:
                colour_counts[colour] = 0
            else:
                colour_counts[colour] = int(regex_result.group(1))
        self.turns.append(Turn(**colour_counts))

    def is_valid_game(self, max_red: int, max_green: int, max_blue: int) -> bool:
        for turn in self.turns:
            if turn.red > max_red or turn.green > max_green or turn.blue > max_blue:
                return False
        return True
