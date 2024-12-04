import networkx as nx
from itertools import permutations

def compute_tsp(G, criterion="distance"):
    """
    Compute the optimal TSP path and total weight for the given criterion.
    """
    nodes = list(G.nodes())
    best_path = None
    best_weight = float('inf')

    for path in permutations(nodes):
        weight = sum(G[u][v]["weight"][criterion] for u, v in zip(path, path[1:] + path[:1]))
        if weight < best_weight:
            best_weight = weight
            best_path = path

    return best_path, best_weight
