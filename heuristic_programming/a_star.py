from heuristic_programming.states.neighbors_states import create_all_neighbors_states, extract_loads
from heuristic_programming.states.final_states import is_final_state
from copy import deepcopy


# A* path finding
# for a given start_state it will try to find the easiest way to end state.
# traditional_heuristic -
#  Estimated distance from the current node to the end node (underestimate distance).
# first_ordering_heuristic -
#  In case there are some states with the same f value, this heuristic will take a part
# second_ordering_heuristic -
#  In case there are some states with the same f value and oh1, this heuristic will take a part.
# third_ordering_heuristic -
#  In case there are some states with the same f value and oh1 and oh2, this heuristic will take a part.
def a_star(start_state,
           traditional_heuristic,
           first_ordering_heuristic,
           second_ordering_heuristic,
           third_ordering_heuristic):

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(extract_loads(deepcopy(start_state)))

    # Loop until you find the end
    while len(open_list) > 0:

        # Ordering heuristic - open list sorted by second and third importance
        open_list.sort(key=lambda x: (x.oh1, x.oh2, x.oh3), reverse=False)

        # Get the current node
        current_state = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_state.f:
                current_state = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_state)

        # Found the goal
        if is_final_state(current_state):
            path = []
            current = current_state
            while current is not None:
                path.append(current.grid)
                current = current.parent
            # Return [reversed path] [the number of developed states (ever in open list)] [the size of the close list]
            return path[::-1], (len(open_list)+len(closed_list)), len(closed_list)

        # Generate children
        children = create_all_neighbors_states(current_state)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue

            # If child is not final state calculate his parameters
            # Otherwise the default values of his parameters will be 0
            if not is_final_state(child):
                # Create the f, g, and h values
                child.g = current_state.g + 1
                child.h = traditional_heuristic.execute(child)
                child.f = child.g + child.h
                child.oh1 = first_ordering_heuristic.execute(child)
                child.oh2 = second_ordering_heuristic.execute(child)
                child.oh3 = third_ordering_heuristic.execute(child)

            # Child is already in the open list
            flag = 0
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    flag = 1
            if flag == 1:
                continue

            # Add the child to the open list
            open_list.append(child)
