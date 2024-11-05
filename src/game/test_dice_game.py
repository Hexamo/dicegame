import unittest
from unittest.mock import MagicMock, patch
from game.dice_game import DiceGame
from game.rules import Rules
from game.user_interaction import UserInteraction
from game.dice import roll_dice

class TestDiceGame(unittest.TestCase):
    def setUp(self):
        self.console = MagicMock()
        self.game = DiceGame(self.console)
        self.game.ui = MagicMock(spec=UserInteraction)
        self.game.rules = MagicMock(spec=Rules)

    def test_display_score(self):
        self.game.score = 100
        self.game.display_score()
        self.game.ui.display_panel.assert_called_with("Current Score", "[bold green]100[/bold green]")

    def test_display_dice(self):
        roll_results = [1, 2, 3, 4, 5, 6]
        self.game.display_dice(roll_results)
        self.game.ui.display_panel.assert_called_with("Dice Roll", "[bold green]1[/bold green] [bold yellow]2[/bold yellow] [bold yellow]3[/bold yellow] [bold yellow]4[/bold yellow] [bold green]5[/bold green] [bold yellow]6[/bold yellow]")

    def test_get_keep_dice(self):
        self.game.ui.prompt_keep_dice.return_value = '15'
        roll_results = [1, 2, 3, 4, 5, 6]
        result = self.game.get_keep_dice(roll_results)
        self.assertEqual(result, [1, 5])

    def test_check_special_rolls(self):
        self.game.rules.check_special_rolls.return_value = "three_pairs"
        roll_results = [1, 1, 2, 2, 3, 3]
        result = self.game.check_special_rolls(roll_results)
        self.assertFalse(result)
        self.game.ui.display_message.assert_called_with("[bold green]You rolled three pairs![/bold green]")

    def test_handle_no_scoring_dice(self):
        self.game.rules.handle_no_scoring_dice.return_value = True
        roll_results = [2, 3, 4, 6, 6, 6]
        result = self.game.handle_no_scoring_dice(roll_results)
        self.assertTrue(result)
        self.game.ui.display_message.assert_called_with("[bold red]No scoring dice! Round over, no points scored.[/bold red]")

    def test_handle_pair_roll(self):
        self.game.rules.handle_pair_roll.return_value = True
        roll_results = [2, 2, 3, 4, 5, 6]
        result = self.game.handle_pair_roll(roll_results)
        self.assertTrue(result)
        self.game.ui.display_message.assert_called_with("[bold red]You rolled a pair! Round over, no points scored.[/bold red]")

    @patch('game.dice_game.DiceGame.roll_dice', return_value=[1, 2, 3, 4, 5, 6])
    def test_play_round(self, mock_roll_dice):
        self.game.ui.prompt_keep_dice.return_value = '15'
        self.game.ui.prompt_continue_rolling.return_value = False
        self.game.rules.is_valid_move.return_value = True
        self.game.rules.handle_pair_roll.return_value = False
        self.game.rules.handle_no_scoring_dice.return_value = False
        self.game.rules.calculate_score.return_value = 150
        self.game.play_round()
        self.assertEqual(self.game.round_score, 150)
        self.assertEqual(self.game.score, 150)

    @patch('game.dice_game.DiceGame.play_round')
    def test_start_game(self, mock_play_round):
        self.game.ui.prompt_continue_rolling.return_value = False
        self.game.is_game_over = True
        self.game.start_game()
        self.game.ui.display_message.assert_called_with("[bold red]Exiting the game. Thanks for playing![/bold red]")

if __name__ == '__main__':
    unittest.main()