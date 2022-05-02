"""
A* algorithm finding a path in a maze
"""


import heapq


def parse_maze(maze):
    WALL = '#'
    states = []
    for i,line in enumerate(maze.split('\n')):
        for j,c in enumerate(line):
            if c != WALL:
                states.append((i,j))
    return states


def draw_path(maze, path):
    grid = [list(line.strip()) for line in maze.split('\n')][:-1]
    for i,j in path:
        grid[i][j] = '*'
    return '\n'.join((''.join(line) for line in grid))


class Space:
    """non-sequential searched space for dfs/bfs"""
    def __init__(self, *args, **kwargs):
        self.states = args[0]  # represents a (raw) space
        if 'parser' in kwargs:
            self.states = kwargs['parser'](self.states)
        
        self.start = min(self.states)  # start state
        self.goal = max(self.states)   # goal state
        
    def is_goal(self, state):
        return state == self.goal
    
    def get_neighbors(self, state):
        (i,j) = state
        candidates = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
        return [state for state in candidates if state in self.states]
    
    def heuristic(self, state):
        i,j = state
        a,b = self.goal
        return ((i-a)**2 + (j-b)**2)**(1/2)



class WeightedNode:
    def __init__(self, state, parent=None, cost=None, heuristic=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        
    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic
    
    def __repr__(self):
        return __class__.__name__ + "(state={}, parent={}, cost={}, heuristic={})".format(self.state, self.parent.state, self.cost, self.heuristic)
    def __str__(self):  return self.__repr__()
    
    

class PriorityQueue:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
    
    def push(self, item):
        heapq.heappush(self.heap, item)
    
    def pop(self):
        return heapq.heappop(self.heap)
    
    def __len__(self):
        return len(self.heap)
    
    def __repr__(self):
        return self.__class__.__name__ + f"({str(self.heap)[1:-1]})"
    def __str__(self): return self.__repr__()
    
    
    
def astar(start_state, is_goal, get_neighbors, get_heuristic):
    # Frontier als leere Prioritätswarteschlange initialisieren
    frontier = PriorityQueue()
    
    # Den Startknoten erzeugen und auf Frontier ablegen
    frontier.push( WeightedNode(start_state, 
                                cost=0,
                                heuristic=get_heuristic(start_state)) )
    
    # Besuchte Zustände mit den (aktuell) geringsten Kosten (welche aktualisiert werden können)
    explored_costs = {start_state: 0}  # a single state can end up with different costs
    
    # Die Haupt-Schleife
    while frontier:
        # Den besten Knoten aus der Prioritätsschlange holen
        n = frontier.pop()  # n = the best node from the Priority Queue
        
        # Ziel erreicht? Dann den Pfad rekonstruieren und zurückgeben
        if is_goal(n.state):
            path = [n.state,]
            while n.state != start_state:
                n = n.parent
                path.append(n.state)
            return path[::-1]
        
        # Der Kost für die benachbarten Knoten/Zustände
        current_cost = n.cost + 1
        
        # Alle Nachbarn des aktuellen Zustandes holen
        for s in get_neighbors(n.state):  # s = neighboring_state
            # Wenn die gespeicherten Kosten höher sind als die aktuellen Kosten 
            if s not in explored_costs\
                or explored_costs[s] > current_cost:
                    # Kosten aktualisieren (nämlich mit den niedrigeren)
                    explored_costs[s] = current_cost  # update with the lower cost
                    # Nachfolger-Knoten erzeugen und auf Frontier legen
                    frontier.push( WeightedNode(state=s,
                                                parent=n,
                                                cost=current_cost,
                                                heuristic=get_heuristic(s)) )
                    

maze = """\
#########
#S      #
# ##### #
#       #
# ## ## #
#       #
# ##### #
#      G#
#########
"""


if __name__ == '__main__':
    # DEMO
    space = Space(maze, parser=parse_maze)
    path = astar(start_state=space.start,
                is_goal=space.is_goal,
                get_neighbors=space.get_neighbors,
                get_heuristic=space.heuristic)
    
    print("path =", path)
    print(draw_path(maze, path))
