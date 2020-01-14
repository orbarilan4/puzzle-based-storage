import numpy as np
from settings import PACKAGE, ESCORT, LOAD, WALL


# For a given grid it finds the amount of escorts (marked in 'e') and packages (marked in 'p')
def get_grid_summary(grid):
    summary = {PACKAGE: 0, ESCORT: 0}
    for row in range(0, grid.shape[0]):
        for col in range(0, grid.shape[1]):
            if grid[row, col] == PACKAGE:
                summary[PACKAGE] += 1
            if grid[row, col] == ESCORT:
                summary[ESCORT] += 1
    return summary


# For a given grid it finds all the loads in it
def get_grid_loads(grid):
    loads = []
    for row in range(0, grid.shape[0]):
        for col in range(0, grid.shape[1]):
            if grid[row, col] == LOAD:
                loads.append([row, col])
    return loads


# For a given grid and two points, it will generate a 'mini grid'.
# Which start in first_point and end in second_point (or vice versa)
# Example: first point = [1,1]
#          second_point = [0,2]
#          grid = [ p p x ]
#                 [ p e e ]
#                 [ p p p ]
# The mini grid will be: mini_grid = [ p x ]
#                                    [ e e ]
# Other definition: 'mini grid' the minimum rectangle in grid which contains both points
def get_mini_grid(grid, first_point, second_point):
    # Create two points which will define the rectangle by his smallest coordinate (point) and the largest
    start_point = []
    end_point = []
    for i in range(0, 2):
        start_point.append(first_point[i] if first_point[i] < second_point[i] else second_point[i])
    for i in range(0, 2):
        end_point.append(first_point[i] if first_point[i] > second_point[i] else second_point[i])

    # Create the mini grid (the rectangle) by the two points
    return grid[start_point[0]:(end_point[0] + 1), start_point[1]:(end_point[1] + 1)], start_point, end_point


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
