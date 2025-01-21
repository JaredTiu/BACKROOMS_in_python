#this is for the window to check the rays

import pygame
import math
from maze_reference import maze
from making_of_the_rays import Particle

#main loop

def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 400 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((20,20,20))

    p1 = Particle((20,20), 500)

    left, right, forward, Reverse = False, False, False, False 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                exit()