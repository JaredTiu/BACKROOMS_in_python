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
        screen.blit(background, (0, 0))

        #this is the algorithm
        if stack: 
            current = stack.pop()
            current.visited = True 

            viable_neighbors = []
            for cell in current.other_cells:
                if not cell.visited:
                    viable_neighbors.append(cell)

            if viable_neighbors:
                select = randint(0, len(viable_neighbors) -1)
                stack.append(viable_neighbors[select])
                current.remove_shared_wall_of_the_cell(viable_neighbors[select])
                path.append(current)
            
            else: 
                if path:
                    backstep = path.pop()
                    stack.append(backstep)

        #shows the current cell 
        if stack: 
            position = (current.pos[0]+20, current.pos[1]+20)
            pygame.draw.circle(screen, (255,255,100) , position, 12)

        #showing the maze that is constructed
        for cell in grid: 
            if cell.visited:
                for wall in cell.walls:
                    pygame.draw.line(screen, (200,200,200), wall[0], wall[1], 2)

        pygame.display.update()
        clock.tick(15)

if __name__ == '__main__':
    main()