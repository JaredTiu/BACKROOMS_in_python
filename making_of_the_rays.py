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

    def update(self, point, direction, grouped_walls):
        self.pos = point
        self.update_direction(direction)
        self.update_terminus(grouped_walls)

    def update_direction(self, direction):
        a = self.init_angle + direction
        angle = math.radians(a/10)
        self.dir = (math.cos(angle), math.sin(angle))

    def update_terminus(self, grouped_walls):
        for group in grouped_walls: 
            distance, minimum_terminus = self.length, None
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