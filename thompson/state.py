# Aaron Moran
# Classes in Python // Thompsons Construction

class State:
    # Member variables
    # Every State has 0,1 or 2 edges.
    edges = []
    
    # Label fro the arrows
    # None means epsilon
    label = None
    
    # Constructor for the class
    def __init__(self, label = None, edges = []):
        self.edges = edges
        self.label = label

myInstance = State(label='a', edges=[])
myOtherInstance = State(edges=[myInstance])
print(myInstance.label)
print(myInstance.edges)
print(myOtherInstance.edges[0])


class Frag:
    # Start state for the NFA fragment
    start = None
    # Accept state of the NFA fragment
    accept = None
    
    # Constructor for the class
    def __init__(self, label= None, edges = []):
        self.edges = edges
        self.label = label


myFrag = Frag(myInstance, myOtherInstance)
print(myFrag)
