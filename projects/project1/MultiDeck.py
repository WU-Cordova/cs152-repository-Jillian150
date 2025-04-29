from random import shuffle, choice
from projects.project1.Card import Card, CardSuit, CardFace

class MultiDeck:
    def __init__(self):
        self.num_decks = choice([2, 4, 6, 8])
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        deck = [Card(face, suit) for _ in range(self.num_decks) for suit in CardSuit for face in CardFace]
        return deck

    def draw_card(self):
        if not self.cards:
            self.cards = self._generate_deck()
            shuffle(self.cards)
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)
