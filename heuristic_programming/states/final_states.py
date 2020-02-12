from settings import LOAD


def is_final_state(state):
    for extraction_point in state.extraction_points:
        if state.grid[extraction_point[0]][extraction_point[1]] == LOAD:
            return True
    return False
