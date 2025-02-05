#this will be a file support for backrooms main 
import pygame
import math

class Particle: 
    def __init__(self, position, ray_length):
        self.pos = position
        self.ray_length = ray_length
        self.dir = 0
        self.rays = []
        for angle in range(-300, 300, 1):
            ray = Ray(self.pos, angle, self.ray_length)
            self.rays.append(ray)

    def update(self, point, walls):
        self.pos = point
        grouped_walls = self.grouped_walls(walls)
        for ray in self.rays:
            ray.update(self.pos, self.dir, grouped_walls)
    
    def collision_detection(self, new_pos, walls):
        for wall in walls:
            if self.line_intersects_wall(self.pos, new_pos, wall):
                return True
        return False
    
    def line_intersects_wall(self, start, end, wall):
        x1, y1 = wall[0]  # First point of the wall
        x2, y2 = wall[1]  # Second point of the wall
        x3, y3 = start    # Start point of the player's movement
        x4, y4 = end      # End point of the player's movement

        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return False  # Lines are parallel

        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        u = -((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom

        return 0 <= t <= 1 and 0 <= u <= 1
    
    def grouped_walls(self, walls):
        distances = []
        for wall in walls:
            distance_a = math.dist(wall[0], self.pos)
            distance_b = math.dist(wall[1], self.pos)
            if distance_a <= distance_b:
                distances.append(distance_a)
            else:
                distances.append(distance_b)
        ordered_walls = [x for _, x in sorted(zip(distances, walls))]

        distances = sorted(distances)
        grouped_walls = []
        temp = [ordered_walls[0]]

        for i in range(1, len(distances)-1):
            if distances[i] == distances[i-1]:
                temp.append(ordered_walls[i])

            else:
                grouped_walls.append(temp)
                temp = [ordered_walls[i]]
        
        grouped_walls.append(temp)
        return grouped_walls

class Ray:
    def __init__(self, position, angle, max_length):
        self.pos = position
        self.init_angle = angle 
        self.angle_rad = math.radians(angle/10)
        self.length = max_length
        self.dir = None
        self.terminus = None 
        self.distance = self.length
        self.corrected_distance = None
        self.active_wall = None

    def update(self, point, direction, grouped_walls):
        self.pos = point
        self.update_direction(direction)
        self.update_terminus(grouped_walls)
        self.update_corrected_distance()

    def update_direction(self, direction):
        a = self.init_angle + direction
        angle = math.radians(a/10)
        self.dir = (math.cos(angle), math.sin(angle))

    def update_corrected_distance(self):
        self.corrected_distance = self.distance * math.cos(self.angle_rad)

    def update_terminus(self, grouped_walls):
        for group in grouped_walls: 
            distance = self.length
            minimum_terminus =  None
            for wall in group: 
                x1, y1 = wall[0][0], wall[0][1]
                x2, y2 = wall[1][0], wall[1][1]
                x3, y3 = self.pos[0], self.pos[1]
                x4, y4 = self.pos[0] + self.dir[0], self.pos[1] + self.dir[1]

                divisor = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
                if divisor == 0: 
                    #if segment and ray parallel then there is no intersection
                    continue

                t = ((x1 - x3)*(y3 - y4) - (y1-y3)*(x3-x4)) / divisor 
                u = -((x1 - x2)*(y1-y3) - (y1 - y2)*(x1-x3)) / divisor

                if t >= 0 and t <= 1 and u > 0: 
                    x_point = x1 + t * (x2 - x1)
                    y_point = y1 + t * (y2 - y1)
                    distance_check = math.dist(self.pos, (x_point, y_point))
                    if distance_check < distance: 
                        distance = distance_check
                        minimum_terminus = (x_point, y_point)
                        self.active_wall = wall

            if distance != self.length:
                self.distance = distance
                self.terminus = minimum_terminus
                return  
        
        point_x = self.pos[0] + self.dir[0] * self.length
        point_y = self.pos[1] + self.dir[1] * self.length
        self.terminus = (point_x, point_y)
        self.distance = self.length
        self.active_wall = None

def display_fade_out_message(screen, message, font, duration=3000):
    # Render the text
    text_surface = font.render(message, True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    
    # Fade out effect
    for alpha in range(255, -1, -5):  # Decrease alpha from 255 to 0
        text_surface.set_alpha(alpha)  # Set the alpha for the text surface
        screen.fill((0, 0, 0))  # Fill the screen with black
        screen.blit(text_surface, text_rect)  # Draw the text
        pygame.display.update()  # Update the display
        pygame.time.delay(duration // 51)  # Control the speed of the fade out

print("code ran correctly!")
