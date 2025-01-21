import math

#this is the math for creating the maze for the main backroom game
class Cell: 
        def __init__(self, position, side):
            self.pos = position
            self.side = side
            self.visited = False
            self.walls = []

            self.create_walls()

            
