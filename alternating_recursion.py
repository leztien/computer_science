
"""
Alternating Recursion Tree-Search
"""


import itertools
import random
from collections import defaultdict

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pydot

try:
    from networkx.drawing.nx_agraph import graphviz_layout  # new
except ImportError:
    from networkx.drawing.nx_pydot import graphviz_layout   # old



class State:  # not used here at all
    def __init__(self, representation=None,
                       initial=None, goal=None,
                       actions=None, id=None):
        self.representation = representation  # atomic / factored / structural
        self.initial = initial  # bool
        self.goal = goal  # bool
        self.actions = actions

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"


class Node:
    """
    A Node is a wrapper around a State
    although here State is not used at all, only Nodes
    """
    def __init__(self, state=None,
                       parent=None, children=None,
                       id=None):
        self.state = state
        self.parent = parent
        self.children = children
        self.id = id    # ordinal number as int

    def __lt__(self, other):
        return self.id < other.id

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"



def make_tree(depth=5, max_children=3, **kwargs):
    """
    Makes a random non-binary tree (on a recursive basis)
    Returns the nodes and the edgelist
    """
    # Get keyword arguments from kwargs
    counter = kwargs['counter'] if 'counter' in kwargs else itertools.count()
    current = kwargs['current'] if 'current' in kwargs else Node(id=next(counter))
    nodes = kwargs.get('nodes', [current,])
    edges = kwargs.get('edges', [])

    # Base case
    p = 0.5  # probability of terminating a branch
    if depth == 1 or (edges and random.random() < p):
        return

    # Recursive case
    children = [Node(id=next(counter)) for _ in range(random.randint(2, max_children))]
    current.children = children

    nodes.extend(children)
    edges.extend((current.id, child.id) for child in children)

    for child in children:
        make_tree(depth - 1, max_children,
                  current=child, counter=counter,
                  nodes=nodes, edges=edges)

    # Sanity check
    ls = sorted(set(sum([t for t in edges], ())))
    assert ls == list(range(len(ls)))

    # Return the nodes and the edges list
    return (nodes, edges)


def nodes_per_level(node, depth=0, dictionary=None):
    """ Level-order tree traversal"""
    # Base
    if not node:
        return

    if depth == 0:
        dictionary = defaultdict(list)
    dictionary[depth].append(node.id)

    # Recurse
    for child in node.children or []:
        nodes_per_level(child, depth=depth+1, dictionary=dictionary)

    if depth == 0:
        return dict(dictionary)


def draw_graph_from_edgelist(edges, root_or_nodelist):

    # Make nx tree
    T = nx.from_edgelist(edges)
    pos = graphviz_layout(T, prog="dot")

    # Get the root
    try:
        root = min(root_or_nodelist)
    except TypeError:
        try:
            root = root_or_nodelist[0]
        except TypeError:
            root = root_or_nodelist

    # Get the levels
    d = nodes_per_level(root)

    # Create a boolean nd-array
    a = np.empty(shape=len(T), dtype=np.bool_)

    # Loop over the dictionary
    for k,v in d.items():
        a[v] = k%2

    # add coloring to the nodes
    color_map = [('pink', 'lightblue')[int(b)] for i,b in enumerate(a)]

    # draw nodes, edges, node labels
    nx.draw_networkx_nodes(T, pos, node_color=color_map, node_size=400)
    nx.draw_networkx_edges(T, pos, width=1)
    nx.draw_networkx_labels(T, pos, font_size=12, font_family="sans-serif")
    plt.show()



# Alternating recurion function

def alternating_recursion_search(root):
    leaves = list()
    even_level_search(root, leaves)
    return leaves

def even_level_search(node, leaves):
    if not node.children:
        return node

    for child in node.children:
        if odd_level_search(child, leaves):
            leaves.append(child)

def odd_level_search(node, leaves):
    if not node.children:
        return node

    for child in node.children:
        if even_level_search(child, leaves):
            leaves.append(child)



# Demo
if __name__ == '__main__':

    nodes, edges = make_tree(depth=5, max_children=3)
    root = nodes[0]
    draw_graph_from_edgelist(edges, root)

    leaves = alternating_recursion_search(root)
    print("\nfound the leaves:", leaves)

