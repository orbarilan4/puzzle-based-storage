import itertools as it
import numpy as np
from dynamic_programming.utils.grid_utils import get_grid_summary
from dynamic_programming.state import State


# For a given summary (dict) it will generate all the optional final states
# Final state is defined by the location of the requested Package (Load)
# if there is Load at the I/0 point ([n,m] point) it is a final state
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
