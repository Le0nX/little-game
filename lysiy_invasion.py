import sys
import pygame

def run_game():
	"""Initializing the game and creates a window"""
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Lysiy Invasion")

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.flip()

run_game()