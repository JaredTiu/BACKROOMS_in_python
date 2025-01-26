import pygame
import math
from sys import exit
from maze_creation import generate_maze
from Backrooms_support import Particle

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    background_color = (20, 20, 20)
    floor_color = (50, 50, 50) 
    ceiling_color = (100, 100, 100)
    
    wall_texture = pygame.image.load('capture.PNG').convert()
    
    p1 = Particle((20, 20), 250)
    maze = generate_maze(width, height, 40)
    
    left, right, forward, reverse = False, False, False, False 
    
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
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT: 
                    left = False
                if event.key == pygame.K_RIGHT: 
                    right = False 
                if event.key == pygame.K_UP:
                    forward = False
                if event.key == pygame.K_DOWN: 
                    reverse = False

        # Calculate the new position based on user inputs
        new_pos = p1.pos
        if left:
            p1.dir -= 20
        if right: 
            p1.dir += 20 
        if forward:
            angle = math.radians(p1.dir / 10)
            x = p1.pos[0] + (1 * math.cos(angle))
            y = p1.pos[1] + (1 * math.sin(angle))
            new_pos = (x, y)
        if reverse:
            angle = math.radians((p1.dir) / 10)
            x = p1.pos[0] - (1 * math.cos(angle))
            y = p1.pos[1] - (1 * math.sin(angle))
            new_pos = (x, y)

        # Check for collision before updating the position
        if not p1.collision_detection(new_pos, maze):
            p1.update(new_pos, maze)  # Update only if no collision

        # Display the background
        screen.fill(background_color)

        # Draw the ceiling
        pygame.draw.rect(screen, ceiling_color, (0, 0, width, height // 2))
        
        # Draw the floor
        pygame.draw.rect(screen, floor_color, (0, height // 2, width, height // 2))

        slice_w = width / len(p1.rays)
        for i, ray in enumerate(p1.rays):
            if ray.active_wall:
                # Calculate height based on distance
                h = (15 / ray.corrected_distance) * height
                if h > height:
                    h = height

                # Calculate the position to draw the wall
                y = (height / 2) - (h / 2)

                # Draw the wall texture directly without slicing
                scaled_texture = pygame.transform.smoothscale(wall_texture, (int(slice_w), int(h)))
                screen.blit(scaled_texture, (i * slice_w, y))

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()