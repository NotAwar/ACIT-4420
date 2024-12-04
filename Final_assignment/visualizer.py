import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(G, path=None, criterion="distance"):
    """
    Plots a flat 2D graph with nodes and edges. Highlights the TSP path if provided.
    """
    pos = nx.spring_layout(G, seed=42)  # Use a flat 2D layout
    node_labels = nx.get_node_attributes(G, "street_name")
    edge_labels = {
        (u, v): f"{d['weight'][criterion]:.2f}"
        for u, v, d in G.edges(data=True)
        if criterion in d["weight"]
    }

    nx.draw(
        G,
        pos,
        with_labels=False,
        node_color="lightblue",
        node_size=800,
        font_size=8,
    )
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    if path:
        path_edges = list(zip(path, path[1:] + [path[0]]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

    plt.title(f"Optimal Route by {criterion.capitalize()}")
    plt.show()
