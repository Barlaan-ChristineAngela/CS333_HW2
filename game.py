from player import Player
from dealer import Dealer

class Game:

    def __init__(self):
        self.player = Player()
        self.dealer = Dealer()

    def player_bust(self, hand):
        if self.player.count_hand(hand) > 21:
            print("Player, Bust!")
            return False

    def dealer_bust(self, hand):
        if self.dealer.count_hand(hand) > 21:
            print("Dealer, Bust!")
            return False

    def player_win(self, hand):
        if self.player.count_hand(hand) == 21:
            print("Player wins!")
            return False

    def dealer_win(self, hand):
        if self.dealer.count_hand(hand) == 21:
            print("Dealer wins!")
            return False

    def tie(self, player_hand, dealer_hand):
        if self.player.count_hand(player_hand) == 21 and self.dealer.count_hand(dealer_hand) == 21:
            print("Tie!")
            return False
