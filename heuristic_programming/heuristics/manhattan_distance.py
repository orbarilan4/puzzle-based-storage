from heuristic_programming.utils.grid_utils import get_grid_loads


# Manhattan distance is function which looking for the closest pairs <some load location,extraction point>
# and return the distance between them
def manhattan_distance(self, state):
    loads_location = get_grid_loads(state.grid)
    minimum_distance = float("inf")
    for load_location in loads_location:
        for extraction_point in state.extraction_points:
            distance = abs(load_location[0] - extraction_point[0]) +\
                       abs(load_location[1] - extraction_point[1])
        if distance < minimum_distance:
            minimum_distance = distance
    return minimum_distance



