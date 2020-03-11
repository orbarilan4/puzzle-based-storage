from heuristic_programming.grid.grid_loads import get_grid_loads
from heuristic_programming.state import State
import numpy as np


# manhattan_distance_farthest_closest_pairs returns the farthest from all the closest paris
# In other words, looking for the closest pairs <load location,extraction point> for each load
# (list the distances for each load and his closest extraction point)
# and returns the distance between the farthest pair and returns closest_load, closest_extraction_point
# (maximum distance from the minimum distances)
# Example (when there are extraction points at [2,1],[2,2]).
# p x p
# p x p
# p e p
# The function will return: minimum_distance = 2.
# because there are two closest pairs: [1,1] - load point, [2,1] - extraction point => distance = 1
#                                      [0,1] - load point, [2,1] - extraction point => distance = 2
# and the maximum distance in the list is 2.
#                                      closest_load = [0,1]
#                                      closest_extraction_point = [2,1]
def manhattan_distance_farthest_closest_pairs(state):
    loads_location = get_grid_loads(state.grid)
    farthest_closest_pair_distance = 0
    for load_location in loads_location:
        # Distance from load to the closest extraction point
        minimum_distance_from_load_to_extraction_point = float("inf")
        for extraction_point in state.extraction_points:
            distance = abs(load_location[0] - extraction_point[0]) +\
                       abs(load_location[1] - extraction_point[1])
            if distance < minimum_distance_from_load_to_extraction_point:
                minimum_distance_from_load_to_extraction_point = distance
                closest_pair = load_location, extraction_point
        if farthest_closest_pair_distance < minimum_distance_from_load_to_extraction_point:
            farthest_closest_pair_distance = minimum_distance_from_load_to_extraction_point
            farthest_closest_pair = closest_pair
    return farthest_closest_pair_distance, farthest_closest_pair[0], farthest_closest_pair[1]


# manhattan_distance will return only the minimum_distance parameter
# from manhattan_distance_farthest_closest_pairs function
def manhattan_distance(self, state):
    distance, _, _ = manhattan_distance_farthest_closest_pairs(state)
    return distance
