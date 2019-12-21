from heuristic_programming.state import *
from copy import deepcopy
from heuristic_programming.utils.grid_utils import create_grid_walls
from heuristic_programming.utils.grid_utils import break_grid_walls


# For a given state it returns all the neighbor states
# Neighbor state is defined as T(state,operation) = neighbor_state
# Operation is defined as moving item (Package or Load) through some Escort
def create_all_neighbors_states(state):
    neighbors_states = []
    grid_rows_number = state.get_grid().shape[0]
    grid_cols_number = state.get_grid().shape[1]

    grid_with_walls = create_grid_walls(state.get_grid())

    grid = deepcopy(grid_with_walls)
    for row in range(1, grid_rows_number+1):
        for col in range(1, grid_cols_number+1):
            if grid[row, col] == 'e':
                if grid[row, col+1] == 'p' or grid[row, col+1] == 'x':
                    grid[row, col], grid[row, col+1] = grid[row, col+1], grid[row, col]
                    neighbors_states.append(State(break_grid_walls(grid), state))
                    grid = deepcopy(grid_with_walls)
                if grid[row, col-1] == 'p' or grid[row, col-1] == 'x':
                    grid[row, col], grid[row, col-1] = grid[row, col-1], grid[row, col]
                    neighbors_states.append(State(break_grid_walls(grid), state))
                    grid = deepcopy(grid_with_walls)
                if grid[row+1, col] == 'p' or grid[row+1, col] == 'x':
                    grid[row, col], grid[row+1, col] = grid[row+1, col], grid[row, col]
                    neighbors_states.append(State(break_grid_walls(grid), state))
                    grid = deepcopy(grid_with_walls)
                if grid[row-1, col] == 'p' or grid[row-1, col] == 'x':
                    grid[row, col], grid[row-1, col] = grid[row-1, col], grid[row, col]
                    neighbors_states.append(State(break_grid_walls(grid), state))
                    grid = deepcopy(grid_with_walls)
    return neighbors_states
