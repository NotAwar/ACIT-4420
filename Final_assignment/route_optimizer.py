import networkx as nx
from itertools import permutations
import logging
from geopy.distance import geodesic

def compute_distance(coord1, coord2):
    """Compute the geodesic distance between two coordinates."""
    return geodesic(coord1, coord2).kilometers

def create_graph(relatives, transport_config):
    """Create a graph with nodes and weighted edges."""
    G = nx.Graph()
    for _, row in relatives.iterrows():
        G.add_node(row["name"], pos=(row["latitude"], row["longitude"]), street_name=row["street_name"])

    for i, rel1 in relatives.iterrows():
        for j, rel2 in relatives.iterrows():
            if i < j:
                distance = compute_distance((rel1["latitude"], rel1["longitude"]), (rel2["latitude"], rel2["longitude"]))
                for mode, config in transport_config.items():
                    cost = distance * config["cost_per_km"]
                    time = distance / config["speed_kmh"] * 60 + config["transfer_time_min"]
                    G.add_edge(rel1["name"], rel2["name"], **{mode: {'cost': cost, 'time': time, 'distance': distance}})
    return G

def compute_tsp(G, criterion):
    try:
        # Compute all permutations of nodes starting and ending at Tarjan's home
        nodes = list(G.nodes)
        nodes.remove("Tarjan_Home")
        min_path = None
        min_weight = float('inf')
        total_distance = 0
        total_cost = 0
        total_time = 0

        for perm in permutations(nodes):
            perm = ["Tarjan_Home"] + list(perm) + ["Tarjan_Home"]
            current_weight = 0
            current_distance = 0
            current_cost = 0
            current_time = 0
            valid_path = True
            for i in range(len(perm) - 1):
                if G.has_edge(perm[i], perm[i + 1]):
                    edge_data = G[perm[i]][perm[i + 1]]
                    if criterion in edge_data:
                        current_weight += edge_data[criterion]['distance']
                        current_distance += edge_data[criterion]['distance']
                        current_cost += edge_data[criterion]['cost']
                        current_time += edge_data[criterion]['time']
                    else:
                        valid_path = False
                        break
                else:
                    valid_path = False
                    break
            if valid_path and current_weight < min_weight:
                min_weight = current_weight
                min_path = perm
                total_distance = current_distance
                total_cost = current_cost
                total_time = current_time

        if min_path:
            tsp_path = list(min_path)
            total_weight = float(min_weight)
        else:
            tsp_path = []
            total_weight = float('inf')
        logging.info(f"TSP path: {tsp_path}, Total weight: {total_weight}")
        return tsp_path, total_weight, total_distance, total_cost, total_time
    except Exception as e:
        logging.error(f"Error in compute_tsp: {e}")
        raise
