import typer
from data_loader import load_relatives, load_transport_config
from route_optimizer import create_graph, compute_tsp
from visualizer import plot_graph
from utils import log_execution, InvalidInputError
import logging
import time

# Ensure logging is configured
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = typer.Typer()

def format_time(minutes):
    """Convert minutes to hours and minutes."""
    hours = minutes // 60
    minutes = minutes % 60
    return f"{int(hours)} hours and {int(minutes)} minutes"

@log_execution
@app.command()
def compute_route(criterion: str = typer.Option("distance", "--criterion", "-c", help="Optimization criterion: 'distance', 'time', or 'cost'."), save_path: str = typer.Option(None, "--save-path", "-s", help="Path to save the plot.")):
    """Compute the optimal route based on the specified criterion."""
    try:
        if criterion not in {"distance", "time", "cost"}:
            raise InvalidInputError(f"Invalid criterion: {criterion}. Choose 'distance', 'time', or 'cost'.")

        # Load data
        relatives = load_relatives()
        logging.info(f"Loaded relatives data: {relatives}")

        transport_config = load_transport_config()
        logging.info(f"Loaded transport config: {transport_config}")

        # Create graph
        G = create_graph(relatives, transport_config)
        logging.info(f"Created graph with nodes: {G.nodes(data=True)} and edges: {G.edges(data=True)}")

        # Solve TSP
        start_time = time.time()
        try:
            tsp_path, total_weight, total_distance, total_cost, total_time = compute_tsp(G, criterion)
            logging.info(f"Computed TSP path: {tsp_path} with total {criterion}: {total_weight}")
        except Exception as e:
            logging.error(f"Error in compute_tsp: {e}")
            raise
        end_time = time.time()
        logging.info(f"Time to compute TSP: {end_time - start_time:.2f} seconds")

        # Visualize
        try:
            plot_graph(G, tsp_path, criterion, save_path)
        except Exception as e:
            logging.error(f"Error in plot_graph: {e}")
            raise

        formatted_time = format_time(total_time)
        typer.echo(f"TSP Path: {tsp_path}")
        typer.echo(f"Total Distance: {total_distance:.2f} kilometers")
        typer.echo(f"Total Cost: {total_cost:.2f} currency units")
        typer.echo(f"Total Time: {formatted_time}")
        typer.echo(f"Time to compute TSP: {end_time - start_time:.2f} seconds")

    except Exception as e:
        typer.echo(f"Unexpected Error: {e}")
        logging.error(f"Unexpected Error: {e}")

@app.command()
def interactive_session():
    """Start an interactive session to run commands continually."""
    relatives = load_relatives()
    transport_config = load_transport_config()
    G = create_graph(relatives, transport_config)

    while True:
        criterion = typer.prompt("Enter optimization criterion (distance, time, or cost)")
        if criterion not in {"distance", "time", "cost"}:
            typer.echo("Invalid criterion. Please enter 'distance', 'time', or 'cost'.")
            continue

        start_time = time.time()
        try:
            tsp_path, total_weight, total_distance, total_cost, total_time = compute_tsp(G, criterion)
            plot_graph(G, tsp_path, criterion)
            if criterion == "time":
                unit = "minutes"
            elif criterion == "cost":
                unit = "currency units"
            else:
                unit = "kilometers"

            end_time = time.time()
            formatted_time = format_time(total_time)
            typer.echo(f"TSP Path: {tsp_path}")
            typer.echo(f"Total Distance: {total_distance:.2f} kilometers")
            typer.echo(f"Total Cost: {total_cost:.2f} currency units")
            typer.echo(f"Total Time: {formatted_time}")
            typer.echo(f"Time to compute TSP: {end_time - start_time:.2f} seconds")
        except Exception as e:
            typer.echo(f"Unexpected Error: {e}")
            logging.error(f"Unexpected Error: {e}")

        cont = typer.prompt("Do you want to compute another route? (yes/no)", default="yes")
        if cont.lower() != "yes":
            break

if __name__ == "__main__":
    app()
