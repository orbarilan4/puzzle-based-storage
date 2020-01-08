import itertools as it
import numpy as np
from dynamic_programming.utils.grid_utils import get_grid_summary
from dynamic_programming.state import State
from settings import *


# For a given summary (dict) and extraction points it will generate all the optional final states
# Final state is defined by the location of the requested Package (Load)
# if the Load is in the I/0 point it is a final state
def create_all_final_states(grid, extraction_points):
    summary = get_grid_summary(grid)
    grid_size_without_extraction_points = grid.size - len(extraction_points)
    combinations = []
    final_states = []

    # For each extraction point
    for extraction_point in extraction_points:
        # It will find all the grid combinations for the a summary
        # Example: s = {'p': 2, 'e': 1} => combinations are 'epp' or 'pep' or 'ppe'
        for bits in it.combinations(range(grid.size -1), summary[ESCORT]):
            s = [PACKAGE] * (grid.size - 1)
            for bit in bits:
                s[bit] = ESCORT
            # Add load (x) to the extraction point location and save it
            extraction_point_location = extraction_point[0] * grid.shape[1] + (extraction_point[1])
            s.insert(extraction_point_location, LOAD)
            combinations.append(''.join(s))

    # Each combination will be a final state
    for combination in combinations:
        # Combination becomes a grid
        combination = np.array(list(combination))
        combination = np.reshape(combination, (-1, grid.shape[1]))
        # Create new state from combination and add it to s0
        new_final_state = State(combination, 0, None)
        final_states.append(new_final_state)
    return final_states
