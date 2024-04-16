import unittest
from dealer import Dealer

class TestDealer(unittest.TestCase):

    def setUp(self):
        self.dealer = Dealer()

    def test_deal_to_player(self):
        player_hand = self.dealer.deal_to_player()
        self.assertIsInstance(player_hand, list)
        self.assertEqual(len(player_hand), 1)

    def test_deal_to_dealer(self):
        dealer_hand = self.dealer.deal_to_dealer()
        self.assertIsInstance(dealer_hand, list)
        self.assertEqual(len(dealer_hand), 1)

    def test_count_hand(self):
        hand = ["ace", 5, "king"]
        total_value = self.dealer.count_hand(hand)
        self.assertEqual(total_value, 26)

    def test_check_for_17_or_more(self):
        hand_below_17 = [2, 4]
        hand = self.dealer.check_for_17_or_more(hand_below_17)
        self.assertGreaterEqual(self.dealer.count_hand(hand), 17)

if __name__ == '__main__':
    unittest.main()