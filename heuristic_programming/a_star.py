from heuristic_programming.state import State
from heuristic_programming.states.final_states import create_all_final_states
from heuristic_programming.states.neighbors_states import create_all_neighbors_states
import numpy as np


def a_star(start_state, end_states):
    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_state)
    count=0
    # Loop until you find the end
    while len(open_list) > 0:
        count+=1
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
        if current_state in end_states:
            path = []
            current = current_state
            while current is not None:
                path.append(current.grid)
                current = current.parent
            return path[::-1]  # Return reversed path

        # Generate children
        children = create_all_neighbors_states(current_state)

        # Loop through children
        for child in children:

            # Child is on the closed list
            if child in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_state.g + 1
            child.h = 0
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
            # for i in open_list:
            #     print(count)
            #     print(i)
            #     print(i.g)


def main():
    GRID = np.array([['e', 'p', 'p', 'p', 'p'],
                     ['p', 'p', 'p', 'p', 'p'],
                     ['p', 'p', 'x', 'p', 'p'],
                     ['p', 'p', 'p', 'p', 'p'],
                     ['e', 'p', 'p', 'p', 'p']])
    EXTRACTION_POINTS = np.array([[1,2]])
    x = a_star(State(GRID, None), create_all_final_states(GRID, EXTRACTION_POINTS))
    for i in x:
        print(i)
        print()

if __name__ == '__main__':
    main()