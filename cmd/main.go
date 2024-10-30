package main

import (
	"log"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/githubnext/workspace-blank/internal"
	"github.com/githubnext/workspace-blank/ui"
)

func main() {
	game := internal.NewGame()
	p := tea.NewProgram(ui.NewModel(game))
	if err := p.Start(); err != nil {
		log.Fatal(err)
	}
}
