from deck import Deck
import random

class Dealer:

    def __init__(self):
        self.deck = Deck()

    def deal_to_player(self):

        selected_card = random.choice(self.deck.deck)
        self.deck.deck.remove(selected_card)
        player_hand = [selected_card]

        return player_hand
        
    def deal_to_dealer(self):

        selected_card = random.choice(self.deck.deck)
        self.deck.deck.remove(selected_card)
        dealer_hand = [selected_card]

        return dealer_hand
    
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
    
    def check_for_17_or_more(self, hand):

        while self.count_hand(hand) <= 16:
            hand += self.deal_to_dealer()
        return hand

