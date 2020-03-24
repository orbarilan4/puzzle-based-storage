import time


# time_developed returns the minus number of elapsed seconds since Epoch (a fixed moment in time - 1970)
# Notice that the larger the number, the closer it is to epoch time
def time_developed(self, state):
    return -time.time()
