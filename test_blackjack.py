import unittest
from game import Game
from player import Player
from dealer import Dealer

class TestBlackjackIntegration(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_player_and_dealer_interaction(self):
        player = Player()
        dealer = Dealer()

        initial_player_hand = player.count_hand()
        initial_dealer_hand = dealer.check_for_17_or_more(dealer.count_hand())

        player_hand = self.game.player_bust(dealer.deal_to_player())
        dealer_hand = self.game.dealer_bust(dealer.deal_to_dealer())

        self.assertNotEqual(initial_player_hand, player_hand)
        self.assertNotEqual(initial_dealer_hand, dealer_hand)

if __name__ == '__main__':
    unittest.main()