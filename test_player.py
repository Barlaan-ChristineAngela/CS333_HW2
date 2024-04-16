import unittest
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player()

    def test_stand(self):
        self.assertTrue(self.player.stand())

    def test_hit(self):
        card = self.player.hit()
        self.assertIsNotNone(card)

    def test_count_hand(self):
        hand1 = ['ace', 10]
        hand2 = [5, 'king']
        hand3 = ['queen', 7]

        self.assertEqual(self.player.count_hand(hand1), 21)
        self.assertEqual(self.player.count_hand(hand2), 15)
        self.assertEqual(self.player.count_hand(hand3), 17)

    def test_bust(self):
        hand1 = ['ace', 10]
        hand2 = [10, 'king', 5]
        hand3 = ['queen', 7, 'ace']

        self.assertFalse(self.player.bust(hand1))
        self.assertTrue(self.player.bust(hand2))
        self.assertFalse(self.player.bust(hand3))

if __name__ == '__main__':
    unittest.main()