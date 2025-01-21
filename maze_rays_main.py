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

    left, right, forward, reverse = False, False, False, False 
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    left = True 
                if event.key == pygame.K_RIGHT:
                    right = True 
                if event.key == pygame.K_UP:
                    forward = True
                if event.key == pygame.K_DOWN:
                    Reverse = True
            if event.type == pygame.K_UP:
                if event.key == pygame.K_LEFT: 
                    left = False
                if event.key == pygame.K_RIGHT: 
                    right = False 
                if event.key == pygame.K_UP:
                    forward = False
                if event.key == pygame.K_DOWN: 
                    reverse = False

        #this is for updating the particle based on the user input
        new_pos = p1.pos
        if left:
            p1.dir -= -20
        if right: 
            p1.dir += 20
        if forward:
            angle = math.radians((p1.dir)/10)
            x = p1.pos[0] + (1 * math.cos(angle))
            y = p1.pos[1] + (1 * math.sin(angle))
            new_pos = (x, y)
        if reverse:
            angle = math.radians((p1.dir)/10)
            x = p1.pos[0] - (1 * math.cos(angle))
            y = p1.pos[1] - (1 * math.sin(angle))
            new_pos = (x, y)
        p1.update(new_pos, maze)


            
