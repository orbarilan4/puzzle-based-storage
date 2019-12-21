import numpy as np
from dynamic_programming.states.final_states import create_all_final_states
from dynamic_programming.states.neighbors_states import create_all_neighbors_states
from dynamic_programming.utils.state_utils import find_the_shortest_path
from dynamic_programming.state import State

# Hard Coded input
GRID = np.array([['e', 'p', 'p', 'p', 'p'],
                 ['p', 'p', 'p', 'p', 'p'],
                 ['p', 'p', 'x', 'p', 'p'],
                 ['p', 'p', 'p', 'p', 'p'],
                 ['e', 'p', 'p', 'p', 'p']])
EXTRACTION_POINTS = np.array([[1,2]])


# Print the number of states in S
def print_number_of_states(states):
    count = 0
    for si in states:
        for state in si:
            count += 1
    return count


def main():
    s = list()
    s.append(create_all_final_states(GRID, EXTRACTION_POINTS))  # Add S0 group into S
    i = 0
    while True:
        s.append([])
        for state in s[i]:
            for q in create_all_neighbors_states(state):
                if(i == 0 or (q not in s[i-1])) and (q not in s[i]) and (q not in s[i+1]):
                    s[i+1].append(q)
        i += 1
        if not s[i]:
            break

    # Find the state that present the given grid in S
    for states in s:
        for state in states:
            if State(GRID, 0, None) == state:
                print("The time for the given state is: " + str(state.get_f()))
                print("The order of operation will be:")
                find_the_shortest_path(state)

    print("The number of states created by the algorithm is: " + str(print_number_of_states(s)))


if __name__ == '__main__':
    main()