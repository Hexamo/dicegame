from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich.console import Console

class UserInteraction:
    def __init__(self, console):
        self.console = console

    def display_message(self, message):
        self.console.print(message)

    def display_panel(self, title, message):
        panel = Panel(message, title=title, expand=False)
        self.console.print(panel)

    def display_table(self, title, columns, rows):
        table = Table(title=title)
        for column in columns:
            table.add_column(column)
        for row in rows:
            table.add_row(*row)
        self.console.print(table)

    def prompt_keep_dice(self):
        return Prompt.ask("Enter the dice to keep (space-separated) or 'q' to quit")

    def prompt_continue_rolling(self):
        return Prompt.ask("Do you want to continue rolling? (y/n)", default="y").lower() == 'y'
