def find_the_shortest_path(state):
    print(state)
    if not state.get_p():
        return
    find_the_shortest_path(state.get_p())
