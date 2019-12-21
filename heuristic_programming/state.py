import numpy as np


class State:
    def __init__(self, grid, parent=None):
        self.parent = parent # Denote the previous state (parent state)
        self.grid = grid  # Denote the actual grid which defines the state

        self.g = 0
        self.h = 0
        self.f = 0

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