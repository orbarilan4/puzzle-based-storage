from heuristic_programming.state import State
from heuristic_programming.heuristics.heuristic import Heuristic
from heuristic_programming.heuristics.manhattan_distance import manhattan_distance
from heuristic_programming.heuristics.manhattan_distance_plus_blocks import manhattan_distance_plus_blocks
from heuristic_programming.heuristics.zero_dummy import zero_dummy
from heuristic_programming.states.final_states import create_all_final_states
from heuristic_programming.a_star import a_star
import random
import time
from settings import *
import numpy as np


# Generate basic state
def generate_state(grid_rows_number, grid_cols_number, load_points, extraction_points):
    grid = np.full((grid_rows_number, grid_cols_number), LOAD)
    for i in range(grid_rows_number):
        for j in range(grid_cols_number):
            # If it is not a 'load point' it will be 'escort' or 'package'
            if [i, j] not in load_points:
                grid[i, j] = random.choice([ESCORT, PACKAGE])
    grid[1,0] = ESCORT
    return State(grid, extraction_points, None)


def main():
    start_states = []
    iterations_number = int(ITERATIONS_NUMBER)
    for i in range(iterations_number):
        start_states.append(generate_state(2, 4, [[1, 1]], [[0, 0], [0, 3]]))
    print(ITERATIONS_NUMBER + " start states created, each one of them is an iteration")

    print("\nResults for A* Algorithm: (with manhattan distance considering blocks heuristic)")
    print("================================================================================")
    start_time = time.time()
    sum_of_developed_states = 0
    sum_of_close_lists = 0
    sum_of__path_lengths = 0
    for start_state in start_states:
        # print(start_state.grid)
        path, number_of_developed_states, close_list_size = \
            a_star(start_state, create_all_final_states(start_state), Heuristic(manhattan_distance_plus_blocks))
        sum_of__path_lengths += len(path)
        sum_of_developed_states += number_of_developed_states
        sum_of_close_lists += close_list_size
    print("the sum of the path lengths for all iterations: " + str(sum_of__path_lengths))
    print("the avg of developed states ever in open-list: " + str(sum_of_developed_states / iterations_number))
    print("the avg of the close-list size: " + str(sum_of_close_lists / iterations_number))
    print("the CPU time is: " + str(time.time() - start_time))

    print("\nResults for A* Algorithm: (with manhattan distance heuristic)")
    print("================================================================================")
    start_time = time.time()
    sum_of_developed_states = 0
    sum_of_close_lists = 0
    sum_of__path_lengths = 0
    for start_state in start_states:
        #print(start_state.grid)
        path, number_of_developed_states, close_list_size =\
            a_star(start_state, create_all_final_states(start_state), Heuristic(manhattan_distance))
        sum_of__path_lengths += len(path)
        sum_of_developed_states += number_of_developed_states
        sum_of_close_lists += close_list_size
    print("the sum of the path lengths for all iterations: " + str(sum_of__path_lengths))
    print("the avg of developed states ever in open-list: " + str(sum_of_developed_states / iterations_number))
    print("the avg of the close-list size: " + str(sum_of_close_lists / iterations_number))
    print("the CPU time is: " + str(time.time() - start_time))

    print("\nBFS Algorithm: (A* with zero dummy heuristic)")
    print("================================================================================")
    start_time = time.time()
    sum_of_developed_states = 0
    sum_of_close_lists = 0
    sum_of__path_lengths = 0
    for start_state in start_states:
        #print(start_state.grid)
        path, number_of_developed_states, close_list_size =\
            a_star(start_state, create_all_final_states(start_state), Heuristic(zero_dummy))
        sum_of__path_lengths += len(path)
        sum_of_developed_states += number_of_developed_states
        sum_of_close_lists += close_list_size
    print("the sum of the path lengths for all iterations: " + str(sum_of__path_lengths))
    print("the avg of developed states ever in open-list: " + str(sum_of_developed_states / iterations_number))
    print("the avg of the close-list size: " + str(sum_of_close_lists / iterations_number))
    print("the CPU time is: " + str(time.time() - start_time))


if __name__ == '__main__':
    main()
