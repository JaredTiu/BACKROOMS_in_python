import math
from random import randint

class Cell: 
    def __init__(self, position, side):
        self.pos = position
        self.side = side
        self.visited = False
        self.walls = []
        self.other_cells = []

        self.creating_walls()

    def creating_walls(self):
        top_right = (self.pos[0] + self.side, self.pos[1])
        bottom_right = (self.pos[0] + self.side, self.pos[1] + self.side)
        bottom_left = (self.pos[0], self.pos[1] + self.side)
        # Adding the cells to the list
        self.walls.append([self.pos, top_right])  # Top wall
        self.walls.append([bottom_left, bottom_right])  # Bottom wall
        self.walls.append([self.pos, bottom_left])  # Left wall
        self.walls.append([top_right, bottom_right])  # Right wall

    def find_other_cells(self, grid):
        for cell in grid:
            if math.dist(self.pos, cell.pos) == self.side:
                self.other_cells.append(cell)

    def remove_shared_wall_of_the_cell(self, cell):
        for wall in self.walls:
            if wall in cell.walls:
                cell.walls.remove(wall)
                self.walls.remove(wall)

def create_grid(width, height, side):
    grid = []
    for i in range(0, height, side):
        for j in range(0, width, side):
            position = (j, i)
            grid.append(Cell(position, side))

    for cell in grid:
        cell.find_other_cells(grid)

    return grid

def generate_maze(width, height, side):
    grid = create_grid(width, height, side)

    stack, path = [grid[0]], []
    while stack: 
        current = stack.pop()
        current.visited = True 

        viable_neighbors = []
        for cell in current.other_cells:
            if not cell.visited:
                viable_neighbors.append(cell)

        if viable_neighbors:
            select = randint(0, len(viable_neighbors) - 1)
            stack.append(viable_neighbors[select])
            current.remove_shared_wall_of_the_cell(viable_neighbors[select])
            path.append(current)
        else: 
            if path:
                backstep = path.pop()
                stack.append(backstep)

    # Collect walls of the visited cells
    walls = []
    for cell in grid: 
        if cell.visited:
            walls.extend(cell.walls)

    # Randomly select a wall to be the exit
    exit_wall = walls[randint(0, len(walls) - 1)]
    exit_wall.append(True)  # Mark this wall as the exit

    # exit_wall = walls[0]  # Change this index as needed for testing
    # exit_wall.append(True)  # Mark this wall as the exit

    # Print the exit wall's coordinates
    print(f"Exit wall coordinates: {exit_wall[0]} to {exit_wall[1]}")

    return walls  # Return the walls, including the exit wall