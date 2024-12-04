import typer
import pandas as pd

def display_relatives_table(relatives: pd.DataFrame):
    """Display relatives' data in a formatted table."""
    from tabulate import tabulate
    table = tabulate(
        relatives,
        headers=["Name", "Latitude", "Longitude"],
        tablefmt="grid",
    )
    typer.echo("Relatives Information:")
    typer.echo(table)

def display_route(path: list, criterion: str):
    """Display the optimal route in a user-friendly format."""
    typer.echo(f"\nOptimal Route (by {criterion}):")
    for idx, stop in enumerate(path):
        typer.echo(f"{idx + 1}. {stop}")
    typer.echo("")

def get_user_criteria() -> str:
    """Prompt the user to select a route optimization criterion."""
    criterion = typer.prompt(
        "Enter optimization criterion (time or cost)",
        default="time",
    )
    if criterion not in ["time", "cost"]:
        typer.echo("Invalid input! Defaulting to 'time'.")
        criterion = "time"
    return criterion

def get_start_and_target() -> (str, str):
    """Prompt the user to enter the starting and target locations."""
    start = typer.prompt("Enter the starting location (e.g., Relative_1)")
    target = typer.prompt("Enter the target location (e.g., Relative_10)")
    return start, target
