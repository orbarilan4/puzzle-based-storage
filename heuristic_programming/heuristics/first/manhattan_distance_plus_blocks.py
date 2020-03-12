from heuristic_programming.heuristics.first.manhattan_distance import manhattan_distance_farthest_closest_pairs
from heuristic_programming.grid.get_mini_grid import get_mini_grid
from heuristic_programming.grid.grid_paths import find_paths
import numpy as np
from settings import PACKAGE, LOAD


# manhattan_distance_plus_blocks is function which looking for the farthest from all the closest pairs
# and return the pair distance, considering packages on the way to one of the extraction points
# Note: global_minimum_number_of_blocks_in_path is the minimum number of blocks (on the ways) for all extraction points
# Example (when there are extraction points at [0,0],[2,2])
# p p p
# p x p
# e e p
# global_minimum_number_of_blocks_in_path is 1. because there is a way to [2,2] with only one block.
# The method is to add the global_minimum_number_of_blocks_in_path to the distance calculation,
# this step makes sense since we will need at least one move to get rid of a block.
# Example (when there are extraction points at [2,1],[2,2]).
# p x p
# p x p
# e p p
# The function will return: minimum_distance = 2. because the closest pair: [1,1] - load point, [2,1] - extraction point
#                           closest_load = [1,1]
#                           closest_extraction_point = [2,1]
def manhattan_distance_plus_blocks(self, state):
    # Calculate the basic manhattan distance and get the 2 points
    manhattan_distance, load_location, _ = manhattan_distance_farthest_closest_pairs(state)

    global_minimum_number_of_blocks_in_path = float("inf")

    for extraction_point in state.extraction_points:

        # Get the mini grid for the two points
        mini_grid, top_left_point, bottom_right_point = get_mini_grid(state.grid, load_location, extraction_point)

        # If the load is not in top-left point (or bottom-right) of our mini grid do a flip(turn it to a good situation)
        # Example: good situations : x p    p p
        #                            e e    e x
        #
        #          bad situations:   p x    p p
        #                            e e    x e
        # Notice that extraction point always will be at the opposite corner to the load (by definition of mini_grid)
        # - Need to do that because find_paths function which comes after, works only from the top-left point
        #   and it returns all the paths to the opposite corner.
        if load_location != top_left_point and load_location != bottom_right_point:
            mini_grid = np.flip(mini_grid, 1)

        # Holding all the paths
        paths = find_paths(mini_grid)

        # Searching for the minimum number of blocks in path
        minimum_number_of_blocks_in_path = float("inf")
        for path in paths:
            number_of_blocks_in_path = path.count(PACKAGE) + path.count(LOAD) - 1  # Minus 1 because we start with Load
            if number_of_blocks_in_path < minimum_number_of_blocks_in_path:
                minimum_number_of_blocks_in_path = number_of_blocks_in_path

        if minimum_number_of_blocks_in_path < global_minimum_number_of_blocks_in_path:
            global_minimum_number_of_blocks_in_path = minimum_number_of_blocks_in_path

    return manhattan_distance + global_minimum_number_of_blocks_in_path
