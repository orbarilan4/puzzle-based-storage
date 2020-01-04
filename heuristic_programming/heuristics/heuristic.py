import types


class Heuristic:
    def __init__(self, func=None):
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        return 0



# def execute_replacement2(self, state):
#     print(self.name + 'from execute 2')
#
#
# def main():
#     strat0 = StrategyExample()
#     strat1 = StrategyExample(execute_replacement1)
#     strat1.name = 'Strategy Example 1'
#     strat2 = StrategyExample(execute_replacement2)
#     strat2.name = 'Strategy Example 2'
#     strat0.execute(str(1))
#     strat1.execute()
#     strat2.execute(str(1))
#
#
# main()