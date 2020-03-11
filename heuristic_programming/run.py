from heuristic_programming.state import State
from heuristic_programming.heuristics.heuristic import Heuristic
from heuristic_programming.heuristics.manhattan_distance import manhattan_distance
from heuristic_programming.heuristics.manhattan_distance_plus_blocks import manhattan_distance_plus_blocks
from heuristic_programming.heuristics.zero_dummy import zero_dummy
from heuristic_programming.a_star import a_star
from heuristic_programming.grid.grid_summary import get_grid_summary
import time
from settings import *
from heuristic_programming.states.generate_states import generate_state
import random
import os
import shutil
import numpy as np


def main():
    create_new_results_directory("results")

    for i in range(2, ESCORTS_NUMBER+1):
        print("\n\nRESULTS FOR " + str(i) + " ESCORTS")
        start_states = generate_state(ITERATIONS_NUMBER, ROWS_NUMBER, COLS_NUMBER,
                                      {ESCORT: i, LOAD: LOADS_NUMBER, PACKAGE: (ROWS_NUMBER * COLS_NUMBER)-LOADS_NUMBER-i},
                                      EXTRACTION_POINTS_NUMBER)
        # start_states = [State(grid=np.array([['e','x','p','x'],['p','p','p','p']]),extraction_points=[[1,2]])]
        # f = open(os.path.join("results", "_for_" + str(i) + "_escorts.txt"), "a")
        # print("\nFor A* Algorithm: (with manhattan distance considering blocks heuristic)")
        # print("================================================================================")
        # f.write("\nFor A* Algorithm: (with manhattan distance considering blocks heuristic)")
        # f.write("\n================================================================================")
        # start_time = time.time()
        # sum_of_developed_states = 0
        # sum_of_close_lists = 0
        # sum_of__path_lengths = 0
        # for start_state in start_states:
        #     print(start_state.grid)
        #     print(start_state.extraction_points)
        #     path, number_of_developed_states, close_list_size = \
        #         a_star(start_state, Heuristic(manhattan_distance_plus_blocks))
        #     for j in path:
        #         print(j)
        #     sum_of__path_lengths += len(path)
        #     sum_of_developed_states += number_of_developed_states
        #     sum_of_close_lists += close_list_size
        # f.write("\nthe sum of the path lengths for all iterations: " + str(sum_of__path_lengths))
        # f.write("\nthe avg of developed states ever in open-list: " + str(sum_of_developed_states / ITERATIONS_NUMBER))
        # f.write("\nthe avg of the close-list size: " + str(sum_of_close_lists / ITERATIONS_NUMBER))
        # f.write("\nthe avg CPU time is: " + str((time.time() - start_time) / ITERATIONS_NUMBER))
        # f.close()

        f = open(os.path.join("results", "_for_" + str(i) + "_escorts.txt"), "a")
        print("\n\nFor A* Algorithm: (with manhattan distance heuristic)")
        print("================================================================================")
        f.write("\n\nFor A* Algorithm: (with manhattan distance heuristic)")
        f.write("\n================================================================================")
        start_time = time.time()
        sum_of_developed_states = 0
        sum_of_close_lists = 0
        sum_of__path_lengths = 0
        for start_state in start_states:
            print(start_state.grid)
            print(start_state.extraction_points)
            path, number_of_developed_states, close_list_size =\
                a_star(start_state, Heuristic(manhattan_distance))
            for j in path:
                print(j)
            sum_of__path_lengths += len(path)
            sum_of_developed_states += number_of_developed_states
            sum_of_close_lists += close_list_size
        f.write("\nthe sum of the path lengths for all iterations: " + str(sum_of__path_lengths))
        f.write("\nthe avg of developed states ever in open-list: " + str(sum_of_developed_states / ITERATIONS_NUMBER))
        f.write("\nthe avg of the close-list size: " + str(sum_of_close_lists / ITERATIONS_NUMBER))
        f.write("\nthe avg CPU time is: " + str((time.time() - start_time) / ITERATIONS_NUMBER))
        f.close()

        f = open(os.path.join("results", "_for_" + str(i) + "_escorts.txt"), "a")
        print("\n\nBFS Algorithm: (A* with zero dummy heuristic)")
        print("================================================================================")
        f.write("\n\nBFS Algorithm: (A* with zero dummy heuristic)")
        f.write("\n================================================================================")
        start_time = time.time()
        sum_of_developed_states = 0
        sum_of_close_lists = 0
        sum_of__path_lengths = 0
        for start_state in start_states:
            print(start_state.grid)
            print(start_state.extraction_points)
            path, number_of_developed_states, close_list_size = \
                a_star(start_state, Heuristic(zero_dummy))
            for j in path:
                print(j)
            sum_of__path_lengths += len(path)
            sum_of_developed_states += number_of_developed_states
            sum_of_close_lists += close_list_size
        f.write("\nthe sum of the path lengths for all iterations: " + str(sum_of__path_lengths))
        f.write("\nthe avg of developed states ever in open-list: " + str(sum_of_developed_states / ITERATIONS_NUMBER))
        f.write("\nthe avg of the close-list size: " + str(sum_of_close_lists / ITERATIONS_NUMBER))
        f.write("\nthe avg CPU time is: " + str((time.time() - start_time) / ITERATIONS_NUMBER))
        f.close()


def create_new_results_directory(name):
    if os.path.exists(name):
        shutil.rmtree(name)
    os.makedirs(name)


if __name__ == '__main__':
    main()
