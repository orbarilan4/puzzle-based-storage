import numpy as np
from settings import *


# For a given grid it finds the amount of escorts (marked in 'e') and packages (marked in 'p')
def get_grid_summary(grid):
    summary = {'p': 0, 'e': 0}
    for row in range(0, grid.shape[0]):
        for col in range(0, grid.shape[1]):
            if grid[row, col] == PACKAGE:
                summary[PACKAGE] += 1
            if grid[row, col] == ESCORT:
                summary[ESCORT] += 1
    return summary


# Create the same grid with walls (it will be more easy to work like that)
def create_grid_walls(grid):
    grid_with_walls = np.full((grid.shape[0] + 2, grid.shape[1] + 2), WALL)
    for row in range(1, grid.shape[0] + 1):
        for col in range(1,grid.shape[1] + 1):
            grid_with_walls[row, col] = grid[row - 1, col - 1]
    return grid_with_walls


# Break the walls of the given grid (it will be more easy to work like that)
def break_grid_walls(grid):
    return grid[1:(grid.shape[0]-1), 1:(grid.shape[1]-1)]
