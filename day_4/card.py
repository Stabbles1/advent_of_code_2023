from dataclasses import dataclass


@dataclass
class Card:
    winning_numbers: list[int]
    our_numbers: list[int]
    score: int = 0

    def double_score(self) -> None:
        if self.score == 0:
            self.score = 1
        else:
            self.score = self.score * 2

    def calculate_score(self) -> int:
        for number in self.our_numbers:
            if number in self.winning_numbers:
                self.double_score()
        return self.score
