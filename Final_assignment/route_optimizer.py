import networkx as nx
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
        logging.info(f"Added node: {row['name']} at position: ({row['latitude']}, {row['longitude']})")

    for i, rel1 in relatives.iterrows():
        for j, rel2 in relatives.iterrows():
            if i < j:
                distance = compute_distance((rel1["latitude"], rel1["longitude"]), (rel2["latitude"], rel2["longitude"]))
                for mode, config in transport_config.items():
                    cost = distance * config["cost_per_km"]
                    time = distance / config["speed_kmh"] * 60 + config["transfer_time_min"]
                    G.add_edge(rel1["name"], rel2["name"], **{mode: {'cost': cost, 'time': time, 'distance': distance}})
                    logging.info(f"Added edge from {rel1['name']} to {rel2['name']} with {mode} cost: {cost}, time: {time}, distance: {distance}")
    logging.info(f"Graph created with nodes: {G.nodes(data=True)} and edges: {G.edges(data=True)}")
    return G

def compute_tsp(G, criterion):
    try:
        nodes = list(G.nodes)
        nodes.remove("Tarjan_Home")
        start_node = "Tarjan_Home"
        tsp_path = [start_node]
        total_distance = 0
        total_cost = 0
        total_time = 0

        while nodes:
            last_node = tsp_path[-1]
            nearest_node = None
            min_weight = float('inf')
            for node in nodes:
                if G.has_edge(last_node, node):
                    edge_data = G[last_node][node]
                    logging.info(f"Edge data for {last_node} to {node}: {edge_data}")
                    if criterion in edge_data:
                        weight = edge_data[criterion]
                        if weight < min_weight:
                            min_weight = weight
                            nearest_node = node
            if nearest_node:
                tsp_path.append(nearest_node)
                nodes.remove(nearest_node)
                total_distance += G[last_node][nearest_node]['distance']
                total_cost += G[last_node][nearest_node]['cost']
                total_time += G[last_node][nearest_node]['time']
            else:
                logging.error(f"No valid path found from {last_node}")
                break

        if tsp_path[-1] != start_node:
            tsp_path.append(start_node)
            total_distance += G[tsp_path[-2]][start_node]['distance']
            total_cost += G[tsp_path[-2]][start_node]['cost']
            total_time += G[tsp_path[-2]][start_node]['time']

        logging.info(f"TSP path: {tsp_path}, Total distance: {total_distance}, Total cost: {total_cost}, Total time: {total_time}")
        return tsp_path, total_distance, total_cost, total_time
    except Exception as e:
        logging.error(f"Error in compute_tsp: {e}")
        raise
