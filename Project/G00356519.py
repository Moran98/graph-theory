# Aaron Moran -  G00356519
# Graph Theory Project
# Create using Python a program which will carry out the Thompsons Construction
# method on a Regular Expression to a NFA (Non-Deterministic Finite Automata).


class Account:
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
    # Constructor for the class
    def __init__(self, label = None, edges = []):
        self.edges = edges
        self.label = label