import unittest
from game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_player_bust(self):
        self.assertFalse(self.game.player_bust([10, 'queen', 'king']))

    def test_dealer_bust(self):
        self.assertFalse(self.game.dealer_bust(['ace', 'queen', 'king']))

    def test_player_win(self):
        self.assertFalse(self.game.player_win(['ace', 10]))

    def test_dealer_win(self):
        self.assertFalse(self.game.dealer_win(['ace', 'queen', 'king'])) 

    def test_tie(self):
        self.assertFalse(self.game.tie(['ace', 10], ['ace', 'queen', 'king']))

if __name__ == '__main__':
    unittest.main()