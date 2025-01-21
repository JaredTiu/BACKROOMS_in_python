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
       
        #display the background surface.
        screen.blit(bg, (0, 0))

        #this is the algorithm
        if stack: 
            current = stack.pop()
            current.visited = True 

            viable_neighbors = []
            for neighbor in current.neighbors:
                if not neighbor.visited:
                    viable_neighbors.append(neighbor)

            if viable_neighbors:
                select = randint(0, len(viable_neighbors)-1)
                stack.append(viable_neighbors[select])
                current.remove_shared_wall_of_the_cell(viable_neighbors[select])
                path.append(current)
            
            else: 
                if path:
                    backstep = path.pop()
                    stack.append(backstep)