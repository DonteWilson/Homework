import pygame

ADJACENTS = {"F"   : [(1,0),(-1,0),(0,1),(0,-1)],
             "G"  : [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)],
             "H" : [(1,-2),(1,2),(-1,-2),(-1,2),(2,1),(2,-1),(-2,1),(-2,-1)]}

def F(x,y):
    #First Distance heuristic
    return x+y
def G(x,y):
    #Second Distance heuristic
    return max(x,y)
def H(x,y):
    #Third Heuristics
    return max((x//2+x%2),(y//2+y%2))

HEURISTICS = {"F"   : F,
              "G"  : G,
              "H" : H}

class Star(object):
    #Sets up the Astar algorithm
    def __init__(self,start,end,destination,obstacles):
   
        self.start,self.end = start,end
        self.moves = ADJACENTS[destination]
        self.heuristic = HEURISTICS[destination]
        self.obstacles = obstacles
        self.setup()

    def setup(self):
        #Defines the set up for the algorithm
        self.closed_set = set((self.start,)) #Set of cells already evaluated
        self.open_set   = set() #Set of cells to be evaluated.
        self.came_from = {} #Used to reconstruct path once solved.
        self.gx = {self.start:0} #Cost from start to current position.
        self.hx = {} #Optimal estimate to goal based on heuristic.
        self.fx = {} #Distance-plus-cost heuristic function.
        self.current = self.start
        self.current = self.Guide()
        self.solution = []
        self.solved = False

    def get_neighbors(self):
        #Checks surroundings for neighboring objects.
        neighbors = set()
        for (i,j) in self.moves:
            check = (self.current[0]+i,self.current[1]+j)
            if check not in (self.obstacles|self.closed_set):
                neighbors.add(check)
        return neighbors

    def Guide(self):
      #Follows the current path set by the user to follow
        next_node = None
        for node in self.get_neighbors():
            tentative_gx = self.gx[self.current]+1
            if node not in self.open_set:
                self.open_set.add(node)
                tentative_best = True
            elif node in self.gx and tentative_gx < self.gx[node]:
                tentative_best = True
            else:
                tentative_best = False

            if tentative_best:
                x,y = abs(self.end[0]-node[0]),abs(self.end[1]-node[1])
                self.came_from[node] = self.current
                self.gx[node] = tentative_gx
                self.hx[node] = self.heuristic(x,y)
                self.fx[node] = self.gx[node]+self.hx[node]
                if not next_node or self.fx[node]<self.fx[next_node]:
                    next_node = node
        return next_node

    def get_path(self,node):
        #Reconstructs the path
        if node in self.came_from:
            self.solution.append(node)
            self.get_path(self.came_from[node])

    def evaluate(self):
        #executes the algorithm
        if self.open_set and not self.solved:
            for node in self.open_set:
                if (self.current not in self.open_set) or (self.fx[node]<self.fx[self.current]):
                    self.current = node
            if self.current == self.end:
                self.get_path(self.current)
                self.solved = True
            self.open_set.discard(self.current)
            self.closed_set.add(self.current)
            self.current = self.Guide()
        elif not self.solution:
            self.solution = "Not possible"