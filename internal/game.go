package internal

import (
	"math/rand"
	"time"
)

type GameState struct {
	Players       []Player
	CurrentPlayer int
	Dice          []int
}

type Player struct {
	Name  string
	Score int
}

func NewGame(players []string) *GameState {
	game := &GameState{
		Players:       make([]Player, len(players)),
		CurrentPlayer: 0,
		Dice:          make([]int, 6),
	}

	for i, name := range players {
		game.Players[i] = Player{Name: name, Score: 0}
	}

	return game
}

func (g *GameState) RollDice() {
	rand.Seed(time.Now().UnixNano())
	for i := range g.Dice {
		g.Dice[i] = rand.Intn(6) + 1
	}
}

func (g *GameState) CalculateScore(dice []int) int {
	score := 0
	counts := make(map[int]int)

	for _, die := range dice {
		counts[die]++
	}

	// Scoring rules
	if counts[1] >= 3 {
		score += 1000
		counts[1] -= 3
	}
	for i := 2; i <= 6; i++ {
		if counts[i] >= 3 {
			score += i * 100
			counts[i] -= 3
		}
	}
	score += counts[1] * 100
	score += counts[5] * 50

	return score
}

func (g *GameState) EndTurn() {
	g.CurrentPlayer = (g.CurrentPlayer + 1) % len(g.Players)
}

func (g *GameState) IsFarkle(dice []int) bool {
	return g.CalculateScore(dice) == 0
}
