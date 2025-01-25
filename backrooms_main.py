#this will be the main code for the main game. 

import pygame
import math
from sys import exit
from maze_creation import generate_maze
from Backrooms_support import Particle

def main():
    pygame.init()
    width, height = 1200, 400
    screen = pygame.display.set.mode((width, height))
    clock = pygame.time.Clock()

    background = pygame.surface((width, height))
    background.fill((20,20,20))
    ceiling = pygame.Surface((width//2, height//2))
    ceiling.fill((87,82,73))
    floor = pygame.Surface((width//2, height//2))
    floor.fill((113,82,41))
    
    wall_texture = pygame.image.load('stonewall.png').convert()
    wall_texture = pygame.transform.scale(wall_texture, (400, 100))
	
    p1 = Particle((20,20), 500)
	
    left = False
	right = False
	forward = False
	reverse = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					left = True
				if event.key == pygame.K_RIGHT:
					right = True
				if event.key == pygame.K_UP:
					forward = True
				if event.key == pygame.K_DOWN:
					reverse = True
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					left = False
				if event.key == pygame.K_RIGHT:
					right = False
				if event.key == pygame.K_UP:
					forward = False
				if event.key == pygame.K_DOWN:
					reverse = False