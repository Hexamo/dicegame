from rich.console import Console
from game.dice_game import DiceGame

def main():
    console = Console()
    game = DiceGame(console)
    game.start_game()

if __name__ == "__main__":
    main()