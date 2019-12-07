class State:
  def __init__(self, grid, f, p):
    self.grid = grid  # Denote the actual grid which defines the state
    self.f = f  # Denote the optimal retrieval time of the load
    self.p = p  # Denote the next optimal state
