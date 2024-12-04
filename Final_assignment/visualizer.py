import plotly.graph_objects as go
import networkx as nx
import logging

def plot_graph(G, tsp_path, criterion, save_path=None):
    try:
        # Use the actual latitude and longitude for node positions
        pos = {node: (data['pos'][1], data['pos'][0]) for node, data in G.nodes(data=True)}
        logging.info(f"Graph positions: {pos}")

        # Draw all edges in light gray
        edge_x = []
        edge_y = []
        for edge in G.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.append(x0)
            edge_x.append(x1)
            edge_x.append(None)
            edge_y.append(y0)
            edge_y.append(y1)
            edge_y.append(None)

        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines',
            name='All Edges')

        # Highlight the TSP path with different colors for different modes of transport
        path_edge_traces = []
        color_map = {
            'Bus': '#FF6347',
            'Train': '#1f77b4',
            'Bicycle': '#2ca02c',
            'Walking': '#d62728'
        }
        width_map = {
            'Bus': 2,
            'Train': 1,
            'Bicycle': 3,
            'Walking': 4
        }
        for i in range(len(tsp_path) - 1):
            x0, y0 = pos[tsp_path[i]]
            x1, y1 = pos[tsp_path[i + 1]]
            mode = G[tsp_path[i]][tsp_path[i + 1]]['mode']
            path_edge_trace = go.Scatter(
                x=[x0, x1, None], y=[y0, y1, None],
                line=dict(width=width_map[mode], color=color_map[mode]),
                hoverinfo='none',
                mode='lines',
                name=mode)
            path_edge_traces.append(path_edge_trace)

        node_x = []
        node_y = []
        node_text = []
        for i, node in enumerate(tsp_path):
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            node_text.append(f"{i + 1}. {node.replace('_', ' ')}")

        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            text=node_text,
            textposition="top center",
            hoverinfo='text',
            marker=dict(
                color='#1f77b4',
                size=10,
                line=dict(width=2, color='#1f77b4')),
            textfont=dict(size=12, color='#1f77b4', family='Courier New'))

        # Highlight Tarjan's home
        home_node = "Tarjan_Home"
        home_x, home_y = pos[home_node]

        home_trace = go.Scatter(
            x=[home_x], y=[home_y],
            mode='markers+text',
            text=[f"Home: {home_node.replace('_', ' ')}"],
            textposition="bottom center",
            hoverinfo='text',
            marker=dict(
                color='#9467bd',
                size=15,
                line=dict(width=2, color='#9467bd')),
            textfont=dict(size=12, color='#9467bd', family='Courier New'),
            name='Tarjan Home')

        fig = go.Figure(data=[edge_trace] + path_edge_traces + [node_trace, home_trace],
                        layout=go.Layout(
                            title=f"TSP Path based on {criterion.capitalize()}",
                            titlefont_size=16,
                            showlegend=True,
                            legend=dict(
                                x=0,
                                y=1.0,
                                bgcolor='rgba(255, 255, 255, 0)',
                                bordercolor='rgba(255, 255, 255, 0)'
                            ),
                            hovermode='closest',
                            margin=dict(b=20, l=5, r=5, t=40),
                            annotations=[dict(
                                text="",
                                showarrow=False,
                                xref="paper", yref="paper")],
                            xaxis=dict(title='Longitude', showgrid=True, zeroline=False),
                            yaxis=dict(title='Latitude', showgrid=True, zeroline=False),
                            plot_bgcolor='#f0f0f0',
                            font=dict(family='Courier New', size=12, color='#7f7f7f')))

        if save_path:
            fig.write_html(save_path)
            logging.info(f"Plot saved to {save_path}")
        else:
            fig.show()
    except Exception as e:
        logging.error(f"Error in plot_graph: {e}")
        raise

# Ensure logging is configured
logging.basicConfig(level=logging.INFO, filename='logs/visualization_log.txt', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
