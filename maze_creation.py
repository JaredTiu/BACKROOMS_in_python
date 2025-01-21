import math

#this is the math for creating the maze for the main backroom game
class Cell: 
    def __init__(self, position, side):
            self.pos = position
            self.side = side
            self.visited = False
            self.walls = []
            self.neighbors = []

            self.create_walls()

    def creating_walls(self):
            top_right = (self.pos[0]+self.side, self.pos[1])
            bottom_right = (self.pos[0]+self.side, self.pos[1]+ self.side)
            bottom_left = (self.pos[0], self.pos[1]+ self.side)
            self.walls.append([self.pos, top_right])
		    self.walls.append([bottom_left, bottom_right])
		    self.walls.append([self.pos, bottom_left])
		    self.walls.append([top_right, bottom_right])