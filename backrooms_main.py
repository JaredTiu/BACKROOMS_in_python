import pygame
import math
from sys import exit
from maze_creation import generate_maze
from Backrooms_support import Particle, display_fade_out_message

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    
    wall_texture = pygame.image.load('ol6febcwjh871.PNG').convert()
    ceiling_image = pygame.image.load('images.jpg').convert()
    floor_image = pygame.image.load('floor.png').convert()  # Load the floor texture

    ceiling_scaled_width = width  # Set the width to the screen width
    ceiling_scaled_height = height // 2  # Set the height to half of the screen height
    ceiling_image = pygame.transform.scale(ceiling_image, (ceiling_scaled_width, ceiling_scaled_height))

    # Scale the floor image if needed
    floor_scaled_width = width  # Set the width to the screen width
    floor_scaled_height = height // 2  # Set the height to half of the screen height
    floor_image = pygame.transform.scale(floor_image, (floor_scaled_width, floor_scaled_height))

    pygame.mixer.music.load("A1 - It's just a burning memory.mp3")
    pygame.mixer.music.play(loops=-1)

    pygame.font.init()
    font_size_for_intro = 50
    font_for_intro = pygame.font.Font(None, font_size_for_intro)

    p1 = Particle((20, 20), 250)
    maze = generate_maze(width, height, 40)  # Get the maze walls

    display_fade_out_message(screen, "ESCAPE THE BACKROOMS", font_for_intro)

    left, right, forward, reverse = False, False, False, False 

    # Initialize font for displaying text
    font_size_for_yehey = 100
    font_for_yehey = pygame.font.Font(None, font_size_for_yehey)
    font = pygame.font.SysFont("Arial", 24)
    
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

        # Check if the player has reached the exit wall
        for wall in maze:
            if len(wall) == 3 and wall[2]:  # Check if this is the exit wall
                if p1.line_intersects_wall(p1.pos, new_pos, wall[:2]): 
                    player_yehey = "YEHEY!"
                    text_surface = font_for_yehey.render(player_yehey, True, (0, 0, 0)) 
                    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
                    screen.blit(text_surface, text_rect)  # Center the text
                    pygame.display.update()  # Update the display to show the message
                    pygame.time.wait(2000)  # Wait for 2000 milliseconds (2 seconds)
                    print("You found the exit!")
                    pygame.quit()
                    exit()

        # Draw the floor and ceiling
        # screen.blit(ceiling_image, (0, 0))
        # screen.blit(floor_image, (0, height // 2))

        # Draw the maze walls
        slice_w = width / len(p1.rays)
        for i, ray in enumerate(p1.rays):
            if ray.active_wall:
                # Calculate height based on distance
                h = (15 / ray.corrected_distance) * height
                if h > height:
                    h = height

                # Calculate the position to draw the wall
                y = (height / 2) - (h / 2)

                # Check if this wall is the exit wall
                is_exit_wall = False
                for wall in maze:
                    if len(wall) == 3 and wall[2]:  # Check if this is the exit wall
                        if wall[:2] == ray.active_wall:  # Compare wall coordinates
                            is_exit_wall = True
                            break

                if is_exit_wall:
                    # Draw the exit wall as a line
                    line_color = (255, 0, 0)  # Red color for the exit line
                    line_width = 5  # Width of the line
                    pygame.draw.line(screen, line_color, (i * slice_w, y), (i * slice_w, y + h), line_width)  # Draw exit line
                else:
                    # Calculate the texture slice with a slight overlap
                    tex_slice = int((i / len(p1.rays)) * wall_texture.get_width())
                    tex_slice = min(tex_slice, wall_texture.get_width() - 1)

                    # Create a subsurface of the texture for the current slice
                    texture_slice = wall_texture.subsurface(tex_slice, 0, 2, wall_texture.get_height())  # Slightly wider slice

                    # Scale the texture slice to the height of the wall
                    scaled_texture = pygame.transform.smoothscale(texture_slice, (int(slice_w + 1), int(h)))  # Slightly wider slice

                    # Draw the scaled texture slice with a slight overlap
                    screen.blit(scaled_texture, (i * slice_w - 1, y))  # Slight overlap

        # Display the player's position on the screen
        player_position_text = f"Player Position: ({int(p1.pos[0])}, {int(p1.pos[1])})"
        text_surface = font.render(player_position_text, True, (255, 255, 255))  # White text
        screen.blit(text_surface, (10, 10))

        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()