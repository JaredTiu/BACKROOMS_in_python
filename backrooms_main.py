import pygame
import math
from maze_creation import generate_maze  
from Backrooms_support import Ray, Particle

def main():
    pygame.init()
    width, height = 1000, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    background_color = (20, 20, 20)
    wall_texture = pygame.image.load('stonewall.png').convert()
    wall_texture = pygame.transform.scale(wall_texture, (400, 100))
    
    p1 = Particle((20, 20), 500)  # Create a Particle instance
    maze = generate_maze(width, height, 40)  # Generate the maze

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

        # Update particle direction based on user input
        if left:
            p1.dir -= 20
        if right: 
            p1.dir += 20 
        if forward or reverse:
            angle = math.radians((p1.dir) / 10)
            movement = 1 if forward else -1
            x = p1.pos[0] + (movement * math.cos(angle))
            y = p1.pos[1] + (movement * math.sin(angle))
            new_pos = (x, y)
            p1.update(new_pos, maze)  

        p1.rays = []  # Clear previous rays
        for angle in range(-150, 150, 5):  # Cast rays every 5 degrees instead of 1
            ray = Ray(p1.pos, angle, p1.ray_length)
            p1.rays.append(ray)

        # Display the background
        screen.fill(background_color)
        
        slice_w = width / len(p1.rays)
        offset = 0
        for i, ray in enumerate(p1.rays):
            if ray.active_wall:
                if ray.terminus[0] == ray.active_wall[0][0]:
                    img_start = abs(ray.terminus[1] - ray.active_wall[0][1]) * 10
                else: 
                    img_start = abs(ray.terminus[0] - ray.active_wall[0][1]) * 10

            if img_start >= 300:
                img_start -= 300

            h = (10 / ray.corrected_distance) * height

            if h > height:
                h = height
            w = h * 4
            y = (height / 2) - (h / 2)
            temp_image = pygame.transform.scale(wall_texture, (w, h))
            screen.blit(temp_image, (offset + (i * slice_w), y), (img_start, 0, slice_w, h))

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()