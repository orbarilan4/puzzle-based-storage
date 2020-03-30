from settings import LOAD, ESCORT
from heuristic_programming.grid.grid_items import get_grid_items


# closest_escort_and_load returns the distance between closest escort and load
# In other words, looking for the closest pairs <load location,escort location>
# and returns the distance between them
# Example:
# p x p p p e
# p p p p p p
# p p p p e p
# the distance is 4 - because the pairs <[0,1],[0,5]>.
def closest_escort_and_load(self, state):
    escort_locations = get_grid_items(state.grid, ESCORT)
    load_locations = get_grid_items(state.grid, LOAD)
    # Distance from escort to the closest load
    minimum_distance_from_escort_to_load = float("inf")
    for escort_location in escort_locations:
        for load_location in load_locations:
            distance = abs(escort_location[0] - load_location[0]) + \
                       abs(escort_location[1] - load_location[1])
            if distance < minimum_distance_from_escort_to_load:
                minimum_distance_from_escort_to_load = distance
    return minimum_distance_from_escort_to_load

