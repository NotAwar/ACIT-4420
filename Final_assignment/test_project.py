import pytest
from data_loader import load_relatives, compute_distance
from route_optimizer import create_graph, compute_tsp

def test_load_relatives():
    relatives = load_relatives()
    assert len(relatives) == 10

def test_compute_distance():
    coord1 = (37.4979, 127.0276)
    coord2 = (37.5172, 127.0286)
    distance = compute_distance(coord1, coord2)
    assert distance > 0

def test_tsp():
    relatives = load_relatives()
    transport_config = {"Bus": {"speed_kmh": 40, "cost_per_km": 2, "transfer_time_min": 5}}
    G = create_graph(relatives, transport_config)
    tsp_path, total_weight = compute_tsp(G, "distance")
    assert len(tsp_path) == len(relatives)
