from settings import LOAD


# For a given grid it finds all the loads in it
# Return the locations
def get_grid_loads(grid):
    loads = []
    for row in range(0, grid.shape[0]):
        for col in range(0, grid.shape[1]):
            if grid[row, col] == LOAD:
                loads.append([row, col])
    return loads
