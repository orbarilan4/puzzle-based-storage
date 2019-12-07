import numpy as np
import itertools as it
from state import *

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

# For a given summary (dict) it will generate all the optional states
def create_all_final_states(grid):
    summary = get_grid_summary(grid)
    combinations = []
    s0 = []

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
        s0.append(new_final_state)
    return s0




A = [['e', 'e', 'x', 'e'], ['p', 'p', 'p', 'p']]
B = np.array(A)
print(B.size)
for i in create_all_final_states(B):
    print(i.grid)
    print()

