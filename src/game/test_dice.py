import unittest
from game.dice import roll_dice

class TestDice(unittest.TestCase):
    def test_roll(self):
        for _ in range(10):
            result = roll_dice()
            self.assertIn(result, range(1, 7))

if __name__ == '__main__':
    unittest.main()