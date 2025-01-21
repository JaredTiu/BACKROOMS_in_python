import pygame 
from maze_creation import create_grid
from random import randint

#main program

def main():
    pygame.init()
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((20,20,20))

    grid = create_grid(WIDTH, HEIGHT, 40)

    stack, path = [grid[0]], []
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
       
