from settings import LOAD
from heuristic_programming.grid.grid_summary import get_grid_summary


# For a given state check if is final state
def is_final_state(state):
    if get_grid_summary(state.grid)[LOAD] == 0:
        return True
    return False






