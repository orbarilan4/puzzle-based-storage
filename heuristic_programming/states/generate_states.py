import itertools as it
import numpy as np
from heuristic_programming.grid.grid_summary import get_grid_summary
from heuristic_programming.state import State
from settings import *
import random
from copy import deepcopy


# For a given state (grid and his extractions points) it will generate all the optional final states
# Final state is defined by the location of the escorts and zero number of requested loads
# There is at least one Extraction Point with escort in final state (and there is no loads on the grid)
def generate_state(number_of_states, grid_cols_number, grid_details, extraction_points):

    combinations = []
    generated_states = []
    # It will find all the grid combinations for the a summary
    grid_cells_number = sum(grid_details.values())

    # Example: s = {'p': 2, 'e': 1} => combinations are 'epp' or 'pep' or 'ppe'
    numeric_combinations = list(it.combinations(range(grid_cells_number), grid_details[ESCORT]))
    random.shuffle(numeric_combinations)
    for num, bits in enumerate(numeric_combinations, start=0):
        if num < number_of_states:
            s = [PACKAGE] * grid_cells_number
            for bit in bits:
                s[bit] = ESCORT
            combinations.append(''.join(s))
        else:
            break

    # Each combination will be a state
    # Example: 'eepp' => [e e p p] or [e e] or [e]
    #                                 [p p]    [e]
    #                                          [p]
    #                                          [p]
    for combination in combinations:
        # Combination becomes a grid
        combination = np.array(list(combination))
        combination = np.reshape(combination, (-1, grid_cols_number))
        # Create new state from combination and add it to generated_states
        generated_state = State(combination, extraction_points, None)
        generated_states.append(generated_state)

    # Some random packages become requested loads
    # Example: [e e p p p p] and 1 load requested => [e e p p x p]
    for state in generated_states:
        number_of_loads = grid_details[LOAD]
        while number_of_loads > 0:
            random_location = [random.randint(0, grid_cells_number/grid_cols_number - 1),
                               random.randint(0, grid_cols_number - 1)]
            if state.grid[random_location[0]][random_location[1]] == PACKAGE:
                # Replacing a character from a certain index
                state.grid[random_location[0]][random_location[1]] = LOAD
                number_of_loads -= 1

    return generated_states
