import math
from random import randint

class Cell: 
    def __init__(self, position, side):
        self.pos = position
        self.side = side
        self.visited = False
        self.walls = []
        self.other_cells = []
        self.is_exit = False  # New attribute to mark the exit

        self.creating_walls()

    def creating_walls(self):
        top_right = (self.pos[0] + self.side, self.pos[1])
        bottom_right = (self.pos[0] + self.side, self.pos[1] + self.side)
        bottom_left = (self.pos[0], self.pos[1] + self.side)
        # Adding the cells to the list
        self.walls.append([self.pos, top_right])
        self.walls.append([bottom_left, bottom_right])
        self.walls.append([self.pos, bottom_left])
        self.walls.append([top_right, bottom_right])

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

    # Randomly select a cell to be the exit
    exit_cell = grid[randint(0, len(grid) - 1)]
    exit_cell.is_exit = True

    print(f"Exit cell generated at: {exit_cell.pos}")

    # Collect walls of the visited cells
    walls = []
    for cell in grid: 
        if cell.visited:
            walls.extend(cell.walls)

    return walls, exit_cell  # Return both walls and the exit cell