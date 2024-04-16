from game import Game
from dealer import Dealer
from player import Player

if __name__ == "__main__":

    new_game = Game()
    new_dealer = Dealer()
    new_player = Player()

    user_selection = input("[Y/N] Start game?\n")

    player_hand = new_dealer.deal_to_player()
    dealer_hand = new_dealer.deal_to_dealer()
    player_hand += new_dealer.deal_to_player()
    dealer_hand += new_dealer.deal_to_dealer()

    print(f"Player: {player_hand}")
    print(f"Dealer: {dealer_hand}")


