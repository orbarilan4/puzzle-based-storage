import numpy as np
import uuid


# Built by 'grid' and its 'extraction points'.
# State can has parent which it's state too.
# And State has parameters g,h,f
class State:
    def __init__(self, grid, extraction_points, parent=None):
        self.parent = parent  # Denote the previous state (parent state)
        self.grid = grid  # Denote the actual grid which defines the state
        self.extraction_points = extraction_points  # Denote the grid extraction points (I/O point)

        self.g = 0  # The distance between the current node and the start node
        self.h = 0  # Traditional (Classic) Heuristic, the estimated distance from the current node to the end node
        self.f = 0  # The total cost of the node
        self.oh1 = 0  # Ordering Heuristic : First-Class
        self.oh2 = 0  # Ordering Heuristic : Second-Class
        self.oh3 = 0  # Ordering Heuristic : Third-Class

    def __eq__(self, other):
        return np.array_equal(self.grid, other.grid)

    def __str__(self):
        output = ""
        for row in range(0, self.grid.shape[0]):
            for col in range(0, self.grid.shape[1]):
                output += " " + self.grid[row, col]
            output += "\n"
        return output

    def get_grid(self):
        return self.grid

    def get_grid_string(self):
        output = ""
        for row in range(0, self.grid.shape[0]):
            for col in range(0, self.grid.shape[1]):
                output += self.grid[row, col]
        return output

