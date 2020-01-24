from heuristic_programming.grid.grid_loads import get_grid_loads


# manhattan_distance_closest_pairs is function which looking for the closest pairs <some load location,extraction point>
# and return the distance between them and the pair closest_load, closest_extraction_point
# Example (when there are extraction points at [2,1],[2,2]).
# p x p
# p x p
# p e p
# The function will return: minimum_distance = 1. because the closest pair: [1,1] - load point, [2,1] - extraction point
#                           closest_load = [1,1]
#                           closest_extraction_point = [2,1]
def manhattan_distance_closest_pairs(state):
    loads_location = get_grid_loads(state.grid)
    minimum_distance = float("inf")
    for load_location in loads_location:
        for extraction_point in state.extraction_points:
            distance = abs(load_location[0] - extraction_point[0]) +\
                       abs(load_location[1] - extraction_point[1])
            if distance < minimum_distance:
                minimum_distance = distance
                closest_load = load_location
                closest_extraction_point = extraction_point
    return minimum_distance, closest_load, closest_extraction_point


# manhattan_distance will return only the minimum_distance parameter from manhattan_distance_pairs function
def manhattan_distance(self, state):
    minimum_distance, _, _ = manhattan_distance_closest_pairs(state)
    return minimum_distance



