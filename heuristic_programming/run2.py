from heuristic_programming.heuristics.heuristic import Heuristic
from heuristic_programming.heuristics.traditional.manhattan_distance import manhattan_distance
from heuristic_programming.heuristics.traditional.manhattan_distance_plus_blocks import manhattan_distance_plus_blocks
from heuristic_programming.heuristics.ordering.proximity_of_escorts_to_loads import proximity_of_escorts_to_loads
from heuristic_programming.heuristics.ordering.closest_escort_and_load import closest_escort_and_load
from heuristic_programming.heuristics.ordering.time_developed import time_developed
from heuristic_programming.heuristics.zero_dummy import zero_dummy
from heuristic_programming.a_star import a_star
from heuristic_programming.state import State
import numpy as np
import time
from settings import *
from heuristic_programming.states.generate_states import generate_state
import os
import shutil
import csv

heuristic_names = ['manhattan_distance_plus_blocks', 'manhattan_distance']


def main():
    create_new_results_directory("results")

    for extraction_points_number in range(1, EXTRACTION_POINTS_NUMBER + 1):
        for escorts_number in range(1, ESCORTS_NUMBER + 1):
            for heuristic_name in heuristic_names:
                print("The file of " + heuristic_name + " with " +
                      str(extraction_points_number) + " extraction points and " +
                      str(escorts_number) + " escorts is ready !")

                start_states = generate_state(ITERATIONS_NUMBER, ROWS_NUMBER, COLS_NUMBER,
                                              {ESCORT: escorts_number, LOAD: LOADS_NUMBER,
                                               PACKAGE: (ROWS_NUMBER * COLS_NUMBER) - LOADS_NUMBER - escorts_number},
                                              extraction_points_number)
                with open(os.path.join("results", heuristic_name, str(extraction_points_number) + "_extraction_points",
                                       "_for_" + str(escorts_number) + "_escorts.csv"), 'a', newline='') as csv_file:
                    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(
                        ['grid_string', 'rows_number', 'cols_number', 'extraction_point_locations', 'heuristic_name',
                         'close_list_size', 'open_list_counter', 'cpu_time', 'path_length'])
                    for start_state in start_states:
                        grid_string = start_state.get_grid_string()
                        extraction_point_locations = start_state.extraction_points
                        rows_number = start_state.grid.shape[0]
                        cols_number = start_state.grid.shape[1]
                        traditional_heuristic = manhattan_distance_plus_blocks\
                            if heuristic_name == heuristic_names[0] else manhattan_distance
                        path, open_list_counter, close_list_size = \
                            a_star(start_state,
                                   Heuristic(traditional_heuristic),
                                   Heuristic(proximity_of_escorts_to_loads),
                                   Heuristic(zero_dummy),
                                   Heuristic(zero_dummy))
                        writer.writerow(
                            [grid_string, rows_number, cols_number, extraction_point_locations, heuristic_name,
                             close_list_size, open_list_counter, 'cpu_time', len(path)])
                    csv_file.close()

                # start_states = generate_state(ITERATIONS_NUMBER, ROWS_NUMBER, COLS_NUMBER,
                #                               {ESCORT: i, LOAD: LOADS_NUMBER, PACKAGE: (ROWS_NUMBER * COLS_NUMBER)-LOADS_NUMBER-i},
                #                               EXTRACTION_POINTS_NUMBER)
        # f = open(os.path.join("results", "_for_" + str(i) + "_escorts.txt"), "a")
        # print("\nFor A* Algorithm: (with manhattan distance considering blocks heuristic)")
        # print("================================================================================")
        # f.write("\nFor A* Algorithm: (with manhattan distance considering blocks heuristic)")
        # f.write("\n================================================================================")
        # start_time = time.time()
        # sum_of_developed_states = 0
        # sum_of_close_lists = 0
        # for start_state in start_states:
        #     sum_of__path_lengths = 0
        #     print(start_state.grid)
        #     print(start_state.extraction_points)
        #     path, number_of_developed_states, close_list_size = \
        #         a_star(start_state,
        #                Heuristic(manhattan_distance_plus_blocks),
        #                Heuristic(proximity_of_escorts_to_loads),
        #                Heuristic(zero_dummy),
        #                Heuristic(time_developed))
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
        #
        # f = open(os.path.join("results", "_for_" + str(i) + "_escorts.txt"), "a")
        # print("\n\nFor A* Algorithm: (with manhattan distance heuristic)")
        # print("================================================================================")
        # f.write("\n\nFor A* Algorithm: (with manhattan distance heuristic)")
        # f.write("\n================================================================================")
        # start_time = time.time()
        # sum_of_developed_states = 0
        # sum_of_close_lists = 0
        # sum_of__path_lengths = 0
        # for start_state in start_states:
        #     print(start_state.grid)
        #     print(start_state.extraction_points)
        #     path, number_of_developed_states, close_list_size =\
        #         a_star(start_state,
        #                Heuristic(manhattan_distance_plus_blocks),
        #                Heuristic(proximity_of_escorts_to_loads),
        #                Heuristic(closest_escort_and_load),
        #                Heuristic(time_developed))
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

        # f = open(os.path.join("results", "_for_" + str(i) + "_escorts.txt"), "a")
        # print("\n\nBFS Algorithm: (A* with zero dummy heuristic)")
        # print("================================================================================")
        # f.write("\n\nBFS Algorithm: (A* with zero dummy heuristic)")
        # f.write("\n================================================================================")
        # start_time = time.time()
        # sum_of_developed_states = 0
        # sum_of_close_lists = 0
        # sum_of__path_lengths = 0
        # for start_state in start_states:
        #     print(start_state.grid)
        #     print(start_state.extraction_points)
        #     path, number_of_developed_states, close_list_size = \
        #         a_star(start_state, Heuristic(zero_dummy), Heuristic(zero_dummy))
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


def create_new_results_directory(name):
    if os.path.exists(name):
        shutil.rmtree(name)
    os.makedirs(name)
    os.makedirs(name + "/" + heuristic_names[0])
    os.makedirs(name + "/" + heuristic_names[1])
    for i in range(1, EXTRACTION_POINTS_NUMBER+1):
        os.makedirs(name + "/" + heuristic_names[0] + "/" + str(i) + "_extraction_points")
        os.makedirs(name + "/" + heuristic_names[1] + "/" + str(i) + "_extraction_points")


if __name__ == '__main__':
    main()
