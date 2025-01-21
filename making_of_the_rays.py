import math 

class Particle:
    def __init__(self, position, ray_length):
        self.pos = position
        self.ray_length = ray_length
        self.dir = 0
        self.rays = []
        for angle in range(-400, 400, 2):
            ray = Ray(self.pos, angle, self.ray_length)
            self.rays.append(ray)

            