# -*-coding:Latin-1 -*

import os, sys
import pygame
import globals
from models import map, character, projectile, building
# from pygame.locals import * # pourrait Ãªtre tolÃ©rÃ©
from constants import NB_SQUARES_PER_ROW, NB_SQUARES_PER_COL, SQUARE_SIDE # a-t-on mieux ?

from gamestates.gameState import GameContext, GameState, MenuState, ActionState

def main():
	"""initialise les modeles puis gere les evenements et construit la vue dans une boucle

	"""
	pygame.init()
	
	screen = pygame.display.set_mode((NB_SQUARES_PER_ROW * SQUARE_SIDE, NB_SQUARES_PER_COL * SQUARE_SIDE))

	# Création du game context et des games states associés 
	gc = GameContext()

	clock = pygame.time.Clock()
	while 1:
		gc.handle_events()
		next_state = gc.update()
		gc.render(screen)
		pygame.display.flip()       #a placer après le changement éventuel de gamestate  

		# quitter si la valeur de renvoi Ã©tait nulle
		# Ã  remplacer par un Ã©tat d'exit en cours...
		if not next_state == "keep":
			if next_state == "exit":
				return
			gc.change_state(next_state)
		clock.tick(globals.FPS)


	pygame.display.flip()

	
if __name__ == '__main__': main()
