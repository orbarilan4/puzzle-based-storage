from settings import ESCORT, LOAD
from heuristic_programming.grid.grid_items import get_grid_items


# proximity_of_escorts_to_loads returns the average distance between escorts and loads
# In other words, looking for the closest pairs <load location,escort location> for each escort
# (list the distances for each escort and his closest load)
# and returns the average distance for all the pairs
# Example:
# x e p
# p p p
# x p e
# for [0,1] escort the distance is 1.
# for [2,2] escort the distance is 2.
# so, the average distance is 1.5.
def proximity_of_escorts_to_loads(self, state):
    escort_locations = get_grid_items(state.grid, ESCORT)
    load_locations = get_grid_items(state.grid, LOAD)
    sum_of_distances_between_escorts_to_their_closest_loads = 0
    for escort_location in escort_locations:
        # Distance from escort to the closest load
        minimum_distance_from_escort_to_load = float("inf")
        for load_location in load_locations:
            distance = abs(escort_location[0] - load_location[0]) + \
                       abs(escort_location[1] - load_location[1])
            if distance < minimum_distance_from_escort_to_load:
                minimum_distance_from_escort_to_load = distance
        sum_of_distances_between_escorts_to_their_closest_loads += minimum_distance_from_escort_to_load
    return sum_of_distances_between_escorts_to_their_closest_loads / len(escort_locations)
