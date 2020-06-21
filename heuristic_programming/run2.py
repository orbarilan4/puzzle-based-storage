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
from functools import partial
from multiprocessing import Pool
from settings import *
from heuristic_programming.states.generate_states import generate_state
import os
import shutil
import csv
import itertools

heuristic_names = ['manhattan_distance_plus_blocks', 'manhattan_distance', 'zero_dummy']


def main():
    create_new_results_directory("results")
    pool = Pool(processes=PROCESSES_NUMBER)

    for loads_number in range(1, LOADS_NUMBER + 1):
        for extraction_points_number in range(2, EXTRACTION_POINTS_NUMBER + 1):
            for escorts_number in range(1, ESCORTS_NUMBER + 1):
                generated_stats = generate_state(ITERATIONS_NUMBER, ROWS_NUMBER, COLS_NUMBER,
                                                 {ESCORT: escorts_number, LOAD: loads_number,
                                                  PACKAGE: (ROWS_NUMBER * COLS_NUMBER) - loads_number - escorts_number},
                                                 extraction_points_number)
                for heuristic_name in heuristic_names:
                    print("The file of " + heuristic_name + " with: " + str(loads_number) + " loads and " +
                          str(extraction_points_number) + " extraction points and " +
                          str(escorts_number) + " escorts is ready !")

                    with open(os.path.join("results", heuristic_name,
                                           "_for_" + str(loads_number) + "_loads",
                                           "_for_" + str(extraction_points_number) + "_extraction_points",
                                           "_for_" + str(escorts_number) + "_escorts.csv"), 'a',
                              newline='') as csv_file:
                        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                        writer.writerow(
                            ['grid_string', 'rows_number', 'cols_number', 'extraction_point_locations',
                             'heuristic_name',
                             'close_list_size', 'open_list_counter', 'cpu_time', 'path_length'])
                        csv_file.close()

                        # Separate generate_states into chucks
                        start_states = [generated_stats[i::len(generated_stats)] for i in range(len(generated_stats))]

                        pool.map(multi_run_wrapper, zip(start_states,
                                                        itertools.repeat(loads_number),
                                                        itertools.repeat(heuristic_name),
                                                        itertools.repeat(extraction_points_number),
                                                        itertools.repeat(escorts_number)))
    pool.close()


def multi_run_wrapper(args):
    return run(*args)


def run(start_states, loads_name, heuristic_name, extraction_points_number, escorts_number):
    with open(os.path.join("results", heuristic_name,
                           "_for_" + str(loads_name) + "_loads",
                           "_for_" + str(extraction_points_number) + "_extraction_points",
                           "_for_" + str(escorts_number) + "_escorts.csv"), 'a',
              newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for start_state in start_states:
            grid_string = start_state.get_grid_string()
            extraction_point_locations = start_state.extraction_points
            rows_number = start_state.grid.shape[0]
            cols_number = start_state.grid.shape[1]
            if heuristic_names[0] == heuristic_name:
                traditional_heuristic = manhattan_distance_plus_blocks
            elif heuristic_name[1] == heuristic_name:
                traditional_heuristic = manhattan_distance
            else:
                traditional_heuristic = zero_dummy
            path, open_list_counter, close_list_size, cpu_time = \
                a_star(start_state,
                       Heuristic(traditional_heuristic),
                       Heuristic(zero_dummy),
                       Heuristic(zero_dummy),
                       Heuristic(zero_dummy))
            writer.writerow(
                [grid_string, rows_number, cols_number, extraction_point_locations, heuristic_name,
                 close_list_size, open_list_counter, cpu_time, len(path)])
        csv_file.close()


def create_new_results_directory(name):
    if os.path.exists(name):
        shutil.rmtree(name)
    os.makedirs(name)
    os.makedirs(name + "/" + heuristic_names[0])
    os.makedirs(name + "/" + heuristic_names[1])
    for i in range(1, EXTRACTION_POINTS_NUMBER + 1):
        for j in range(1, LOADS_NUMBER + 1):
            for h in range(0, len(heuristic_names)):
                os.makedirs(name + "/" + heuristic_names[h] + "/_for_" + str(j) + "_loads" + "/_for_" + str(i) +
                            "_extraction_points")


if __name__ == '__main__':
    main()
