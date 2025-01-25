#this will be the main code for the main game. 

import pygame
import math
from sys import exit
from maze_creation import generate_maze
from Backrooms_support import Particle

def main():
    pygame.init()
    width, height = 1200, 400
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    background = pygame.Surface((width, height))
    background.fill((20,20,20))
    ceiling = pygame.Surface((width//2, height//2))
    ceiling.fill((87,82,73))
    floor = pygame.Surface((width//2, height//2))
    floor.fill((113,82,41))
    
    wall_texture = pygame.image.load('stonewall.png').convert()
    wall_texture = pygame.transform.scale(wall_texture, (400, 100))
	
    p1 = Particle((20,20), 500)
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

		#now based on those user inputs we will be updating the particle. 
        new_pos = p1.pos
        if left:
            p1.dir -= 20
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
		
		#this displays the background, rays, walls and particle
        screen.blit(background, (0, 0))
        screen.blit(ceiling, (width//2, 0))
        screen.blit(floor, (width//2, height//2))
        # for ray in p1.rays:
        #     pygame.draw.aaline(screen, (240,240,240), ray.pos, ray.terminus, 1)
        # # for wall in maze:
        # #     pygame.draw.line(screen, (200,200,200), wall[0], wall[1], 2)
        # pygame.draw.circle(screen, (100, 255, 100), p1.pos, 7)
        

        slice_w = (width//2)/len(p1.rays)
        offset = width//2
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
            y = (height/2) - (h/2)
            temp_image = pygame.transform.scale(wall_texture, (w, h))
            screen.blit(temp_image, (offset+(i*slice_w), y), (img_start,0,slice_w,h))

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()

    