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

faces = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

@dataclass
class Hand:
    cards: str
    bid: int
    
    def calc_score(self):
        # Put all the cards in a dict, to help identify counts of each card
        score = 0
        cards = {}
        for card in self.cards:
            if card not in cards:
                cards[card] = 1
            else:
                cards[card] += 1

        if len(cards) == 1:
            # Five of a kind
            score = 6_00_00_00_00_00
        elif len(cards) == 2:
            # Four of a kind or full house
            if max(cards.values()) == 4:
                score = 5_00_00_00_00_00
            else:
                score = 4_00_00_00_00_00
        elif len(cards) == 3:
            # Three of a kind or two pair
            if max(cards.values()) == 3:
                score = 3_00_00_00_00_00
            else: 
                score = 2_00_00_00_00_00
        elif len(cards) == 4:
            # One pair
            score = 1_00_00_00_00_00
        elif len(cards) == 4:
            # High card
            score = 0
        
        # Secondary scores based on card faces
        
        for i, card in enumerate(self.cards[::-1]):
            score += faces.index(card) * ((10 * 10) ** (i))
        return score