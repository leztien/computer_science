"""
generic implementation of dfs which takes two callables
"""

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


def make_adjacency_matrix(n_nodes, density=None):
    """makes a random adjacency matrix representing a graph"""
    n = n_nodes
    p = density or 0.05
    while True:
        mx = np.random.rand(n,n)
        mx = np.triu(mx)
        mx += mx.T
        mx = (mx <= p).astype("uint8")
        mx[np.diag_indices(n)] = 0
        assert (mx == mx.T).all()
        if np.logical_or.reduce(mx, axis=0).all() and np.logical_or.reduce(mx, axis=1).all():
            break
        else:
            p += 0.01
    return(mx)


# Display the graph
n_nodes = 10
adjacency_matrix = make_adjacency_matrix(n_nodes)
G = nx.from_numpy_matrix(adjacency_matrix)
nx.draw(G, with_labels=True)

#########################################################################################


class Node:
    def __init__(self, state, parent=None, cost=None):
        self.state = state
        self.parent = parent
        self.cost = cost
        
    def __eq__(self, other):
        return self.state == other.state
    
    def __lt__(self, other):
        return self.cost < other.cost
    
    def __hash__(self):
        return self.state
    
    def __repr__(self): return f"{self.__class__.__name__}({self.state})"
    def __str__(self):  return self.__repr__()


class Space:
    """non-sequential searched space for dfs/bfs"""
    def __init__(self, *args, **kwargs):
        self.adjacency_matrix = args[0]  # represents a graph
        self.start_state = 0
        self.goal_state = len(self.adjacency_matrix) - 1
        
    def is_goal(self, state):
        return state == self.goal_state
    
    def get_neighbors(self, state):
        return [i for i,v in enumerate(self.adjacency_matrix[state]) if v]


def dfs(start_state, is_goal, get_neighbors):
    frontier = [Node(start_state)]
    visited = {start_state}
    
    while frontier:
        node = frontier.pop()   # Stack functionality
        
        if is_goal(node.state):
            path = [node.state,]
            while node.state != start_state:
                node = node.parent
                path.append(node.state)
            return path[::-1]
        
        
        for neighbor in get_neighbors(node.state):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            frontier.append( Node(neighbor, parent=node) )



if __name__ == '__main__':
    # DEMO
    space = Space(adjacency_matrix)
    start = space.start_state
    path = dfs(start, space.is_goal, space.get_neighbors)
    print("path =", path)
