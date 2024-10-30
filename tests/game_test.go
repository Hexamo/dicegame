package tests

import (
	"testing"

	"github.com/githubnext/workspace-blank/internal"
)

func TestNewGame(t *testing.T) {
	players := []string{"Alice", "Bob"}
	game := internal.NewGame(players)

	if len(game.Players) != len(players) {
		t.Errorf("expected %d players, got %d", len(players), len(game.Players))
	}

	for i, player := range game.Players {
		if player.Name != players[i] {
			t.Errorf("expected player name %s, got %s", players[i], player.Name)
		}
		if player.Score != 0 {
			t.Errorf("expected player score 0, got %d", player.Score)
		}
	}

	if game.CurrentPlayer != 0 {
		t.Errorf("expected current player 0, got %d", game.CurrentPlayer)
	}

	if len(game.Dice) != 6 {
		t.Errorf("expected 6 dice, got %d", len(game.Dice))
	}
}

func TestRollDice(t *testing.T) {
	players := []string{"Alice", "Bob"}
	game := internal.NewGame(players)
	game.RollDice()

	if len(game.Dice) != 6 {
		t.Errorf("expected 6 dice, got %d", len(game.Dice))
	}

	for _, die := range game.Dice {
		if die < 1 || die > 6 {
			t.Errorf("expected die value between 1 and 6, got %d", die)
		}
	}
}

func TestCalculateScore(t *testing.T) {
	players := []string{"Alice", "Bob"}
	game := internal.NewGame(players)

	tests := []struct {
		dice     []int
		expected int
	}{
		{[]int{1, 1, 1, 2, 3, 4}, 1000},
		{[]int{2, 2, 2, 3, 4, 5}, 250},
		{[]int{1, 5, 2, 3, 4, 6}, 150},
		{[]int{1, 1, 1, 5, 5, 5}, 1500},
		{[]int{2, 3, 4, 6, 6, 6}, 600},
	}

	for _, test := range tests {
		score := game.CalculateScore(test.dice)
		if score != test.expected {
			t.Errorf("expected score %d, got %d", test.expected, score)
		}
	}
}

func TestIsFarkle(t *testing.T) {
	players := []string{"Alice", "Bob"}
	game := internal.NewGame(players)

	tests := []struct {
		dice     []int
		expected bool
	}{
		{[]int{1, 1, 1, 2, 3, 4}, false},
		{[]int{2, 2, 2, 3, 4, 5}, false},
		{[]int{2, 3, 4, 6, 6, 6}, false},
		{[]int{2, 3, 4, 6, 2, 3}, true},
	}

	for _, test := range tests {
		isFarkle := game.IsFarkle(test.dice)
		if isFarkle != test.expected {
			t.Errorf("expected farkle %v, got %v", test.expected, isFarkle)
		}
	}
}

func TestEndTurn(t *testing.T) {
	players := []string{"Alice", "Bob"}
	game := internal.NewGame(players)

	game.EndTurn()
	if game.CurrentPlayer != 1 {
		t.Errorf("expected current player 1, got %d", game.CurrentPlayer)
	}

	game.EndTurn()
	if game.CurrentPlayer != 0 {
		t.Errorf("expected current player 0, got %d", game.CurrentPlayer)
	}
}
