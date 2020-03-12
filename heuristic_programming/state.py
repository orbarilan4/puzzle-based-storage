import numpy as np


# Built by 'grid' and its 'extraction points'.
# State can has parent which it's state too.
# And State has parameters g,h,f
class State:
    def __init__(self, grid, extraction_points, parent=None):
        self.parent = parent  # Denote the previous state (parent state)
        self.grid = grid  # Denote the actual grid which defines the state
        self.extraction_points = extraction_points  # Denote the grid extraction points (I/O point)

        self.g = 0  # the distance between the current node and the start node
        self.h = 0  # first heuristic, the estimated distance from the current node to the end node
        self.f = 0  # the total cost of the node
        self.h2 = 0  # second heuristic, the ordering heuristic

    def __eq__(self, other):
        return np.array_equal(self.grid, other.grid)

    def __str__(self):
        output = ""
        for row in range(0, self.grid.shape[0]):
            for col in range(0, self.grid.shape[1]):
                output += " " + self.grid[row, col]
            output += "\n"
        return output

    def set_grid(self, grid):
        self.grid = grid

    def set_g(self, g):
        self.g = g

    def set_f(self, f):
        self.f = f

    def set_h(self, h):
        self.h = h

    def get_grid(self):
        return self.grid
