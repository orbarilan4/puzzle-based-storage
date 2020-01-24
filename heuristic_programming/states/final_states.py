import itertools as it
import numpy as np
from heuristic_programming.grid.grid_summary import get_grid_summary
from heuristic_programming.state import State
from settings import *


# For a given state (grid and his extractions points) it will generate all the optional final states
# Final state is defined by the location of the escorts and zero number of requested loads
# There is at least one Extraction Point with escort in final state (and there is no loads on the grid)
def create_all_final_states(state):
    summary = get_grid_summary(state.grid)
    # Final state has no loads (requested loads will become escorts)
    summary[ESCORT] += summary[LOAD]
    del summary[LOAD]

    combinations = []
    final_states = []
    # It will find all the grid combinations for the a summary
    # Example: s = {'p': 2, 'e': 1} => combinations are 'epp' or 'pep' or 'ppe'
    for bits in it.combinations(range(state.grid.size), summary[ESCORT]):
        s = [PACKAGE] * state.grid.size
        for bit in bits:
            s[bit] = ESCORT
        combinations.append(''.join(s))

    # Each combination will be a final state (only if there is at least one extraction point empty)
    for combination in combinations:
        # Combination becomes a grid
        combination = np.array(list(combination))
        combination = np.reshape(combination, (-1, state.grid.shape[1]))
        # Create new state from combination and add it to s0
        new_final_state = State(combination, state.extraction_points, None)
        if is_there_empty_extraction_point(new_final_state):
            final_states.append(new_final_state)
    return final_states


# If there is at least one extraction point empty (contains ESCORT) return true else false
def is_there_empty_extraction_point(state):
    for extraction_point in state.extraction_points:
        if state.grid[extraction_point[0], extraction_point[1]] == ESCORT:
            return True
    return False
