import numpy as np


class State:
    def __init__(self, grid, f, p):
        self.grid = grid  # Denote the actual grid which defines the state
        self.f = f  # Denote the optimal retrieval time of the load
        self.p = p  # Denote the next optimal state

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

    def get_f(self):
        return self.f

    def get_p(self):
        return self.p

    def set_grid(self, grid):
        self.grid = grid
