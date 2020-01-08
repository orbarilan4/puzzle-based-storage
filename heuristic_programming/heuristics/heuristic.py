import types


# Heuristic is using strategy pattern.
# The main goal of this ability is to enable client to choose from different heuristics to complete the specified task.
# Different algorithms can be swapped in and out without any complications for the mentioned task.
class Heuristic:
    def __init__(self, func=None):
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        return 0
