from heuristic_programming.states.neighbors_states import create_all_neighbors_states
from heuristic_programming.states.final_states import is_final_state


def a_star(start_state, heuristic):
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_state)

    # Loop until you find the end
    while len(open_list) > 0:
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

            # Create the f, g, and h values
            child.g = current_state.g + 1
            child.h = heuristic.execute(child)
            child.f = child.g + child.h

            # Child is already in the open list
            flag = 0
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    flag = 1
            if flag == 1:
                continue

            # Add the child to the open list
            open_list.append(child)
