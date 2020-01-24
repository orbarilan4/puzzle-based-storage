from settings import PACKAGE, ESCORT, LOAD


# For a given grid it finds the amount of escorts (marked in ESCORT) and packages (marked in PACKAGE)
def get_grid_summary(grid):
    summary = {PACKAGE: 0, ESCORT: 0, LOAD: 0}
    for row in range(0, grid.shape[0]):
        for col in range(0, grid.shape[1]):
            if grid[row, col] == PACKAGE:
                summary[PACKAGE] += 1
            if grid[row, col] == ESCORT:
                summary[ESCORT] += 1
            if grid[row, col] == LOAD:
                summary[LOAD] += 1
    return summary
