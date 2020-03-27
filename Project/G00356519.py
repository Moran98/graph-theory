# Aaron Moran -  G00356519
# Graph Theory Project
# Create using Python a program which will carry out the Thompsons Construction
# method on a Regular Expression to a NFA (Non-Deterministic Finite Automata).


class Account:
    # Used to display header for project.
    def __init__(self):
        print("===============GraphTheory===============")
        print("|\t(Aaron Moran - G00356519)\t|")
        print("=========================================")

class Fragment:
    # Start and accept states Constructor
    def __init__(self, start, accept):
        self.start=start
        self.accept=accept

class State:
  # Constructor. Fix supplied by Dr. Ian McLoughlin
  def __init__(self, label=None, edges=None):
    # Every state has 0, 1, or 2 edges from it.
    self.edges = edges if edges else []
    # Label for the arrows. None means epsilon.
    self.label = label