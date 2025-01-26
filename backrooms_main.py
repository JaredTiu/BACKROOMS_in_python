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
    
    # Load wall texture
    wall_texture = pygame.image.load('stonewall.png').convert()
    wall_texture_scaled = [pygame.transform.scale(wall_texture, (400, h)) for h in range(1, 401, 10)]
    
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

        # Update the particle based on user inputs
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
        p1.update(new_pos, maze)
        
        # Display the background
        screen.fill(background_color)

        # Draw the walls for debugging
        for wall in maze:
            pygame.draw.line(screen, (255, 0, 0), wall[0], wall[1], 2)  # Draw walls in red

        slice_w = width / len(p1.rays)
        for i, ray in enumerate(p1.rays):
            img_start = 0  # Initialize img_start
            if ray.active_wall:
                if ray.terminus[0] == ray.active_wall[0][0]:
                    img_start = abs(ray.terminus[1] - ray.active_wall[0][1]) * 10
                else: 
                    img_start = abs(ray.terminus[0] - ray.active_wall[0][1]) * 10

            if img_start >= 300:
                img_start -= 300

            if ray.corrected_distance > 0:  # Avoid division by zero
                h = (10 / ray.corrected_distance) * height
                if h > height:
                    h = height

                # Use precomputed textures for performance
                index = min(len(wall_texture_scaled) - 1, int(h / 10))
                temp_image = wall_texture_scaled[index]
                y = (height / 2) - (h / 2)
                screen.blit(temp_image, (i * slice_w, y), (img_start, 0, slice_w, h))

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()