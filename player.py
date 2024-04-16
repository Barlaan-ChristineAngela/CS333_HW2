from deck import Deck
from dealer import Dealer

class Player:

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()

    def stand(self):
        return self.deck.deck

    def hit(self):
        self.dealer.deal_to_player()

    def count_hand(self, hand):

        total_value = 0
        for card in hand:
            if card == "ace":
                total_value += 11
            elif card in ["king", "queen", "jack"]:
                total_value += 10
            else:
                total_value += card
        
        return total_value
    
    def bust(self, hand):
        if self.count_hand(hand) > 21:
            print("Bust!")
        
