import unittest
from unittest.mock import MagicMock
from game.user_interaction import UserInteraction
from rich.console import Console

class TestUserInteraction(unittest.TestCase):
    def setUp(self):
        self.console = MagicMock(spec=Console)
        self.ui = UserInteraction(self.console)

    def test_display_message(self):
        message = "Hello, World!"
        self.ui.display_message(message)
        self.console.print.assert_called_once_with(message)

    def test_display_panel(self):
        title = "Test Panel"
        message = "This is a test panel."
        self.ui.display_panel(title, message)
        self.console.print.assert_called_once()

    def test_display_table(self):
        title = "Test Table"
        columns = ["Column 1", "Column 2"]
        rows = [["Row 1 Col 1", "Row 1 Col 2"], ["Row 2 Col 1", "Row 2 Col 2"]]
        self.ui.display_table(title, columns, rows)
        self.console.print.assert_called_once()

    def test_prompt_keep_dice(self):
        with unittest.mock.patch('rich.prompt.Prompt.ask', return_value='1 22 3'):
            result = self.ui.prompt_keep_dice()
            self.assertEqual(result, '1 22 3')

    def test_prompt_continue_rolling(self):
        with unittest.mock.patch('rich.prompt.Prompt.ask', return_value='y'):
            result = self.ui.prompt_continue_rolling()
            self.assertTrue(result)
        with unittest.mock.patch('rich.prompt.Prompt.ask', return_value='n'):
            result = self.ui.prompt_continue_rolling()
            self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()