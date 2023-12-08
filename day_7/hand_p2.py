from dataclasses import dataclass, field
from enum import Enum, auto


class PrimaryScore(str, Enum):
    FIVE_Of_A_KIND = auto()
    FOUR_Of_A_KIND = auto()
    FULL_HOUSE = auto()
    THREE_OF_A_KIND = auto()
    TWO_PAIR = auto()
    ONE_PAIR = auto()
    HIGH_CARD = auto()

faces = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

@dataclass
class Hand:
    cards: str
    bid: int

    @staticmethod
    def most_common_card(card_counts):
        max_count = 0
        most_common_card = None
        for card, count in card_counts.items():
            if count > max_count:
                most_common_card=card
                max_count = count
        return most_common_card


    
    def calc_score(self):
        # Put all the cards in a dict, to help identify counts of each card
        score = 0
        card_counts = {}
        for card in self.cards:
            if card == "J":
                continue
            if card not in card_counts:
                card_counts[card] = 1
            else:
                card_counts[card] += 1

        joker_count = self.cards.count("J")
        if joker_count == 5:
            card_counts["J"] = 5
        elif joker_count > 0:
            card_counts[self.most_common_card(card_counts)] += joker_count
            

        if len(card_counts) == 1:
            # Five of a kind
            score = 6_00_00_00_00_00
        elif len(card_counts) == 2:
            # Four of a kind or full house
            if max(card_counts.values()) == 4:
                score = 5_00_00_00_00_00
            else:
                score = 4_00_00_00_00_00
        elif len(card_counts) == 3:
            # Three of a kind or two pair
            if max(card_counts.values()) == 3:
                score = 3_00_00_00_00_00
            else: 
                score = 2_00_00_00_00_00
        elif len(card_counts) == 4:
            # One pair
            score = 1_00_00_00_00_00
        elif len(card_counts) == 4:
            # High card
            score = 0

        # Secondary scores based on card faces
        
        for i, card in enumerate(self.cards[::-1]):
            score += faces.index(card) * ((10 * 10) ** (i))
        return score