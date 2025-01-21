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

    def update(self, point, walls):
        self.pos = point
        grouped_walls = self.grouped_walls(walls)
        for ray in self.rays:
            ray.update(self.pos, self.dir, grouped_walls)

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
        self.length = max_length
        self.dir = None
        self.terminus = None