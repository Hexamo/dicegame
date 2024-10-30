package ui

import (
	"fmt"
	"strings"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/githubnext/workspace-blank/internal"
)

type Model struct {
	Game *internal.GameState
}

func NewModel(game *internal.GameState) Model {
	return Model{Game: game}
}

func (m Model) Init() tea.Cmd {
	return nil
}

func (m Model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {
	case tea.KeyMsg:
		switch msg.String() {
		case "q", "esc":
			return m, tea.Quit
		case "r":
			m.Game.RollDice()
		case "e":
			m.Game.EndTurn()
		}
	}
	return m, nil
}

func (m Model) View() string {
	var b strings.Builder

	fmt.Fprintf(&b, "Player: %s\n", m.Game.Players[m.Game.CurrentPlayer].Name)
	fmt.Fprintf(&b, "Score: %d\n", m.Game.Players[m.Game.CurrentPlayer].Score)
	fmt.Fprintf(&b, "Dice: %v\n", m.Game.Dice)

	return b.String()
}
