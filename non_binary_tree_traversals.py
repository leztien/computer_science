
"""
Non-Binary Tree Traversals
"""


import itertools
import random
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx
import pydot

try:
    from networkx.drawing.nx_agraph import graphviz_layout  # new
except ImportError:
    from networkx.drawing.nx_pydot import graphviz_layout   # old



class Node:
    def __init__(self, id, children=None):
        self.id = id
        self.children = children

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"


def make_tree(depth=5, max_children=3, **kwargs):
    """
    Makes a random non-binary tree (on a recursive basis)
    """
    # Get keyword arguments from kwargs
    counter = kwargs['counter'] if 'counter' in kwargs else itertools.count()
    current = kwargs['current'] if 'current' in kwargs else Node(next(counter))
    edges = kwargs.get('edges', [])

    # Base case
    p = 0.5  # probability of terminating a branch
    if depth == 1 or (edges and random.random() < p):
        return

    # Recursive case
    children = [Node(next(counter)) for _ in range(random.randint(2, max_children))]
    current.children = children

    edges.extend([(current.id, child.id) for child in children])

    for child in children:
        make_tree(depth - 1, max_children,
                  current=child, counter=counter, edges=edges)

    # Sanity check
    ls = sorted(set(sum([t for t in edges], ())))
    assert ls == list(range(len(ls)))

    # Return the root node and the edges list
    return (current, edges)


def draw_graph_from_edgelist(edges):
    T = nx.from_edgelist(edges)
    pos = nx.spring_layout(T)
    pos = graphviz_layout(T, prog="dot")

    nx.draw(T, pos,
            with_labels=True,
            node_size=350,
            node_color='lightgreen',
            font_size=14,
            font_weight='bold')
    plt.show()
    return T



# Traversal functions

def preorder(node):
    if not node:
        return []
    return [node.id] + sum([preorder(child) for child in node.children or []], [])


def postorder(node):
    if not node:
        return []
    return sum([postorder(child) for child in node.children or []], []) + [node.id]


def levelorder(node, depth=0, d=None):
    if not node:
        return

    if depth == 0:
        d = defaultdict(list)
    d[depth].append(node.id)

    for child in node.children or []:
        levelorder(child, depth=depth+1, d=d)

    if depth == 0:
        return sum([d[k] for k in sorted(d.keys())], [])



# Demo
if __name__ == '__main__':

    root, edges = make_tree(4, 3)
    draw_graph_from_edgelist(edges)

    l = preorder(root)
    print("\npre-order:", l)

    l = postorder(root)
    print("\npost-order:", l)

    l = levelorder(root)
    print("\nlevel-order: ", l)
