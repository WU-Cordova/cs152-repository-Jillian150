from projects.project1.MultiDeck import MultiDeck
from projects.project1.Card import Card

class Game:
    def __init__(self):
        self.deck = MultiDeck()
        self.player_hand = []
        self.dealer_hand = []

    def deal_initial_hands(self):
        self.player_hand = [self.deck.draw_card(), self.deck.draw_card()]
        self.dealer_hand = [self.deck.draw_card(), self.deck.draw_card()]

    def calculate_hand_value(self, hand):
        value = sum(card.value for card in hand)
        ace_count = sum(1 for card in hand if card.card_face == CardFace.ACE)
        while value > 21 and ace_count:
            value -= 10
            ace_count -= 1
        return value

    def display_hands(self, reveal_dealer=False):
        print(f"Player's hand: {[str(card) for card in self.player_hand]}")
        if reveal_dealer:
            print(f"Dealer's hand: {[str(card) for card in self.dealer_hand]}")
        else:
            print(f"Dealer's hand: [{self.dealer_hand[0]}, ?]")

    def player_turn(self):
        while True:
            self.display_hands()
            choice = input("Do you want to 'hit' or 'stay'? ").lower()
            if choice == 'hit':
                self.player_hand.append(self.deck.draw_card())
                if self.calculate_hand_value(self.player_hand) > 21:
                    print("You bust!")
                    return False
            elif choice == 'stay':
                return True

    def dealer_turn(self):
        while self.calculate_hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(self.deck.draw_card())

    def determine_winner(self):
        player_value = self.calculate_hand_value(self.player_hand)
        dealer_value = self.calculate_hand_value(self.dealer_hand)
        if dealer_value > 21 or player_value > dealer_value:
            print("You win!")
        elif player_value == dealer_value:
            print("It's a tie!")
        else:
            print("Dealer wins!")

    def play_round(self):
        self.deal_initial_hands()
        if self.player_turn():
            self.dealer_turn()
            self.display_hands(reveal_dealer=True)
            self.determine_winner()
        print("\nWould you like to play again? (yes/no)")
        if input().lower() != 'yes':
            return False
        return True

    def start_game(self):
        while self.play_round():
            self.deck = MultiDeck()

if __name__ == "__main__":
    game = Game()
    game.start_game()
