import re
from game import Game


def read_input(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


if __name__ == "__main__":
    lines = read_input("day_2/input.txt")
    games = []
    valid_game_sum = 0
    for line in lines:
        game_id = re.search(r"Game (\d+)", line).group(1)
        current_game = Game(int(game_id))
        turns = line.split(";")
        for turn in turns:
            current_game.add_turn(turn)
        if current_game.is_valid_game(max_red=12, max_green=13, max_blue=14):
            valid_game_sum += current_game.id

    print(valid_game_sum)
