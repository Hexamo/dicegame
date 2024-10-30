# Dice 10000 Game

This is a simple implementation of the Dice 10000 game using the Bubbletea TUI framework in Go.

## Description

Dice 10000, also known as Farkle, is a dice game where players take turns rolling six dice to accumulate points. The game continues until a player reaches a target score, typically 10,000 points. Players can choose to bank their points or continue rolling to accumulate more points, but if they roll and get no scoring dice (a "farkle"), they lose all points accumulated during that turn.

## Running the Game

To run the game, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/githubnext/workspace-blank.git
   cd workspace-blank
   ```

2. Build and run the game:
   ```
   go build -o dicegame cmd/main.go
   ./dicegame
   ```

## Running the Unit Tests

To run the unit tests, use the following command:
```
go test ./tests/...
```
