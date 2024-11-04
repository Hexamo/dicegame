from game.dice import roll_dice
from game.rules import Rules
from game.user_interaction import UserInteraction

class DiceGame:
    def __init__(self, console):
        self.console = console
        self.rules = Rules()
        self.ui = UserInteraction(console)
        self.score = 0
        self.round_score = 0
        self.is_game_over = False

    def display_score(self):
        self.ui.display_panel("Current Score", f"[bold green]{self.score}[/bold green]")

    def roll_dice(self, num_dice):
        return [roll_dice() for _ in range(num_dice)]

    def display_dice(self, roll_results):
        dice_str = ""
        counts = {i: roll_results.count(i) for i in range(1, 7)}
        for d in roll_results:
            if d == 1 or d == 5:
                dice_str += f"[bold green]{d}[/bold green] "
            elif counts[d] >= 3:
                dice_str += f"[dodger_blue1]{d}[/dodger_blue1] "
            else:
                dice_str += f"[bold yellow]{d}[/bold yellow] "
        self.ui.display_panel("Dice Roll", dice_str.strip())

    def get_keep_dice(self, roll_results):
        while True:
            keep_dice = self.ui.prompt_keep_dice()
            if keep_dice.lower() == 'q':
                self.is_game_over = True
                return None
            try:
                keep_dice = [int(d) for d in keep_dice]
                if all(d in roll_results for d in keep_dice):
                    if all(d in [1, 5] or roll_results.count(d) >= 3 for d in keep_dice):
                        return keep_dice
                    else:
                        self.ui.display_message("[bold red]Invalid selection! Only dice that can score points can be kept.[/bold red]")
                else:
                    self.ui.display_message("[bold red]Invalid selection! Some dice are not in the roll results.[/bold red]")
            except ValueError:
                self.ui.display_message("[bold red]Invalid input! Please enter valid dice values.[/bold red]")

    def check_special_rolls(self, roll_results):
        special_roll = self.rules.check_special_rolls(roll_results)
        if special_roll == "three_pairs":
            self.ui.display_message("[bold green]You rolled three pairs![/bold green]")
            self.round_score += 1000
            self.ui.display_panel("Round Score", f"[bold blue]{self.round_score}[/bold blue]")
            self.display_score()
            return False  # Continue the current round
        elif special_roll == "straight":
            self.ui.display_message("[bold green]You rolled a straight![/bold green]")
            self.round_score += 1500
            self.ui.display_panel("Round Score", f"[bold blue]{self.round_score}[/bold blue]")
            self.display_score()
            self.score += self.round_score
            return False  # End the current round
        return False

    def handle_no_scoring_dice(self, roll_results):
        if self.rules.handle_no_scoring_dice(roll_results):
            self.ui.display_message("[bold red]No scoring dice! Round over, no points scored.[/bold red]")
            self.round_score = 0
            return True
        return False

    def handle_pair_roll(self, roll_results):
        if self.rules.handle_pair_roll(roll_results):
            self.ui.display_message("[bold red]You rolled a pair! Round over, no points scored.[/bold red]")
            self.round_score = 0
            return True
        return False

    def play_round(self):
        self.round_score = 0
        kept_dice = []  # List to store dice that are kept for scoring
        while True:
            self.ui.display_message("\nRolling the dice...")
            roll_results = self.roll_dice(6 - len(kept_dice))  # Roll remaining dice
            self.display_dice(roll_results)

            if self.handle_pair_roll(roll_results):
                break

            if self.handle_no_scoring_dice(roll_results):
                break

            if self.check_special_rolls(roll_results):
                break

            keep_dice = self.get_keep_dice(roll_results)
            if keep_dice is None:
                break

            kept_dice.extend(keep_dice)  # Add chosen dice to kept_dice

            if self.rules.is_valid_move(kept_dice):
                self.round_score += self.rules.calculate_score(keep_dice)
                self.ui.display_panel("Round Score", f"[bold blue]{self.round_score}[/bold blue]")
                self.display_score()

                if self.score + self.round_score >= 10000:
                    self.score += self.round_score
                    self.ui.display_message("[bold red]You reached 10,000! You win![/bold red]")
                    self.display_score()
                    self.is_game_over = True
                    break

                if len(kept_dice) == 6:
                    self.ui.display_message("[bold green]All dice used! Rolling a fresh set of 6 dice.[/bold green]")
                    kept_dice = []

                if not self.ui.prompt_continue_rolling():
                    self.score += self.round_score
                    break
            else:
                self.ui.display_message("[bold red]Invalid roll![/bold red]")
                break

    def start_game(self):
        self.ui.display_message("[bold magenta]Welcome to the Dice Game: 10,000![/bold magenta]")
        while not self.is_game_over:
            self.play_round()
        self.ui.display_panel("Final Score", f"[bold green]{self.score}[/bold green]")
        self.ui.display_message("[bold red]Exiting the game. Thanks for playing![/bold red]")
