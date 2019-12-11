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


# Create the same grid with walls (it will be more easy to work like that)
def create_grid_walls(grid):
    grid_with_walls = np.full((grid.shape[0] + 2, grid.shape[1] + 2), 'w')
    for row in range(1, grid.shape[0] + 1):
        for col in range(1,grid.shape[1] + 1):
            grid_with_walls[row, col] = grid[row - 1, col - 1]
    return grid_with_walls


# Break the same grid with walls (it will be more easy to work like that)
def break_grid_walls(grid):
    return grid[1:(grid.shape[0]-1),1:(grid.shape[1]-1)]


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
                    neighbors_states.append(State(break_grid_walls(grid), state.get_f()+1, state))
                    grid = deepcopy(grid_with_walls)
                if grid[row, col-1] == 'p' or grid[row, col-1] == 'x':
                    grid[row, col], grid[row, col-1] = grid[row, col-1], grid[row, col]
                    neighbors_states.append(State(break_grid_walls(grid), state.get_f()+1, state))
                    grid = deepcopy(grid_with_walls)
                if grid[row+1, col] == 'p' or grid[row+1, col] == 'x':
                    grid[row, col], grid[row+1, col] = grid[row+1, col], grid[row, col]
                    neighbors_states.append(State(break_grid_walls(grid), state.get_f()+1, state))
                    grid = deepcopy(grid_with_walls)
                if grid[row-1, col] == 'p' or grid[row-1, col] == 'x':
                    grid[row, col], grid[row-1, col] = grid[row-1, col], grid[row, col]
                    neighbors_states.append(State(break_grid_walls(grid), state.get_f()+1, state))
                    grid = deepcopy(grid_with_walls)
    return neighbors_states


# A = [['e', 'x', 'e'], ['p', 'e', 'p'], ['p', 'p', 'p']]
# B = np.array(A)

def main():
    A = [['e', 'x', 'e'], ['p', 'e', 'p'], ['p', 'p', 'p']]
    B = np.array(A)
    s = []
    s.append(create_all_final_states(B))  # Add S0 group into S
    i = 0
    while True:
        s.append([])
        for state in s[i]:
            for q in create_all_neighbors_states(state):
                if(i == 0 or (q not in s[i-1])) and (q not in s[i]) and (q not in s[i+1]):
                    s[i+1].append(q)
        i += 1
        if not s[i]:
            break

    count = 0
    for v in s:
        for z in v:
            print(str(count) + ":")
            print(z)
        count +=1
        print()

if __name__ == '__main__':
    main()