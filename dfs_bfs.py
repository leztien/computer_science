
"""
simple implementation of DFS/BFS
"""


def dfs_bfs(start):
    frontier = [start,]
    explored = set()
    parents = dict()   # to trace the path back
    
    while frontier:
        # DFS or BFS 
        c = frontier.pop()                  # Stack = LIFO = DFS
        #c = frontier[0]; del frontier[0]   # Queue = FIFO = BFS = shortest path
        
        if c is GOAL:
            path = [c,]
            while c is not start:
                c = parents[c]
                path.append(c)
            return path[::-1]
        
        # mark the current node as explored
        explored.add(c)
        
        # get neighbors of c
        neighbors = [n for n in get_neighbors(c)
                     if n not in frontier and n not in explored]

        # add the unexplored neighbors to the frontier
        frontier.extend(neighbors)
        
        # record each neighbor's parent
        for n in neighbors:
            parents[n] = c
        

def get_neighbors(s, adjacency_matrix=None):
    adjacency_matrix = adjacency_matrix or globals()["adjacency_matrix"]
    return [j for j,v in enumerate(adjacency_matrix[s]) if v]





if __name__ == '__main__':
    
    adjacency_matrix = [[0,1,1,0,0],
                        [1,0,0,1,1],
                        [1,0,0,1,0],
                        [0,1,1,0,1],
                        [0,1,0,1,0]]
    START = 0
    GOAL = len(adjacency_matrix) - 1
    
    path = dfs_bfs(START)
    print("PATH =", path)
    
    
    #VISUALIZE:
    import numpy as np
    import networkx as nx
    
    G = nx.from_numpy_matrix(np.array(adjacency_matrix))
    nx.draw(G, with_labels=True)

