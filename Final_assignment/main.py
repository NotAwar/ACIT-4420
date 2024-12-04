import typer
from data_loader import load_relatives, load_transport_config
from route_optimizer import create_graph, compute_tsp
from visualizer import plot_graph
from utils import log_execution, InvalidInputError

app = typer.Typer()

@app.command()
@log_execution
def compute_route(
    criterion: str = typer.Option(
        "distance",
        "--criterion",
        "-c",
        help="Optimization criterion: 'distance', 'time', or 'cost'."
    )
):
    """Compute the optimal route based on the specified criterion."""
    try:
        if criterion not in {"distance", "time", "cost"}:
            raise InvalidInputError(f"Invalid criterion: {criterion}. Choose 'distance', 'time', or 'cost'.")

        # Load data
        relatives = load_relatives()
        transport_config = load_transport_config()

        # Create graph
        G = create_graph(relatives, transport_config)

        # Solve TSP
        tsp_path, total_weight = compute_tsp(G, criterion)

        # Visualize
        plot_graph(G, tsp_path, criterion)
        typer.echo(f"TSP Path: {tsp_path}")
        typer.echo(f"Total {criterion.capitalize()}: {total_weight:.2f}")

    except Exception as e:
        typer.echo(f"Unexpected Error: {e}")

if __name__ == "__main__":
    app()
