import numpy as np
import itertools as it
from state import *
from copy import deepcopy

# For a given grid it finds the amount of escorts (marked in 'e') and packages (marked in 'p')
def get_grid_summary(grid):
    summary = {'p': 0, 'e': 0}
    for row in range(0, grid.shape[0]):
        for col in range(0, grid.shape[1]):
            if grid[row,col] == 'p':
                summary['p'] += 1
            if grid[row,col] == 'e':
                summary['e'] += 1
    return summary


# For a given summary (dict) it will generate all the optional final states
def create_all_final_states(grid):
    summary = get_grid_summary(grid)
    combinations = []
    final_states = []

    # It will find all the grid combinations for the a summary
    # Example: s = {'p': 2, 'e': 1} => combinations are 'epp' or 'pep' or 'ppe'
    for bits in it.combinations(range(grid.size - 1), summary['e']):
        s = ['p'] * (grid.size - 1)
        for bit in bits:
            s[bit] = 'e'
        # Add load (x) to the end of the combination and save it
        combinations.append(''.join(s) + 'x')

    # Each combination will be a final state
    for combination in combinations:
        # Combination becomes a grid
        combination = np.array(list(combination))
        combination = np.reshape(combination, (-1, grid.shape[1]))
        # Create new state from combination and add it to s0
        new_final_state = State(combination, 0, None)
        final_states.append(new_final_state)
    return final_states


def create_all_neighbors_states(grid):
    neighbors_states = []
    grid_rows_number = grid.shape[0]
    grid_cols_number = grid.shape[1]

    # Create the same grid with walls (it will be more easy to work like that)
    grid_with_walls = np.full((grid_rows_number + 2, grid_cols_number + 2), 'w')
    for row in range(1, grid_rows_number+1):
        for col in range(1, grid_cols_number+1):
            grid_with_walls[row, col] = grid[row-1, col-1]

    grid = deepcopy(grid_with_walls)
    for row in range(1, grid_rows_number+1):
        for col in range(1, grid_cols_number+1):
            if grid[row, col] == 'e':
                if grid[row, col+1] == 'p' or grid[row, col+1] == 'x':
                    grid[row, col], grid[row, col+1] = grid[row, col+1], grid[row, col]
                    neighbors_states.append(grid)
                    grid = deepcopy(grid_with_walls)
                if grid[row, col-1] == 'p' or grid[row, col-1] == 'x':
                    grid[row, col], grid[row, col-1] = grid[row, col-1], grid[row, col]
                    neighbors_states.append(grid)
                    grid = deepcopy(grid_with_walls)
                if grid[row+1, col] == 'p' or grid[row+1, col] == 'x':
                    grid[row, col], grid[row+1, col] = grid[row+1, col], grid[row, col]
                    neighbors_states.append(grid)
                    grid = deepcopy(grid_with_walls)
                if grid[row-1, col] == 'p' or grid[row-1, col] == 'x':
                    grid[row, col], grid[row-1, col] = grid[row-1, col], grid[row, col]
                    neighbors_states.append(grid)
                    grid = deepcopy(grid_with_walls)
    return neighbors_states


A = [['e', 'x', 'e'], ['p', 'e', 'p'], ['p', 'p', 'p']]
B = np.array(A)
for i in create_all_neighbors_states(B):
    print(i)
# def main():
#     A = [['e', 'x', 'e'], ['p', 'e', 'p'], ['p', 'p', 'p']]
#     B = np.array(A)
#     s = []
#     s.append(create_all_final_states(B))  # Add S0 group into S
#     i = 0
#     while s[i-1] != None:
#         s[i+1] = []
#         for state in s[i]:
#             for q in neighbors_states(state):
#         print("a")
#         i += 1
#
# if __name__ == '__main__':
#     main()