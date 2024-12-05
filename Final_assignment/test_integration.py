import unittest
import os
from data_loader import load_relatives, load_transport_config
from route_optimizer import create_graph, compute_tsp
from visualizer import plot_graph

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.relatives = load_relatives()
        self.transport_config = load_transport_config()
        self.graph = create_graph(self.relatives, self.transport_config)

    def test_compute_route_distance(self):
        tsp_path, total_distance, total_cost, total_time = compute_tsp(self.graph, "distance")
        self.assertGreater(len(tsp_path), 1, "TSP path should contain more than one node")
        self.assertGreater(total_distance, 0, "Total distance should be greater than 0")
        self.assertGreater(total_cost, 0, "Total cost should be greater than 0")
        self.assertGreater(total_time, 0, "Total time should be greater than 0")
        plot_graph(self.graph, tsp_path, "distance", "test_plot_distance.html")
        self.assertTrue(os.path.exists("test_plot_distance.html"), "Plot file should be created")

    def test_compute_route_time(self):
        tsp_path, total_distance, total_cost, total_time = compute_tsp(self.graph, "time")
        self.assertGreater(len(tsp_path), 1, "TSP path should contain more than one node")
        self.assertGreater(total_distance, 0, "Total distance should be greater than 0")
        self.assertGreater(total_cost, 0, "Total cost should be greater than 0")
        self.assertGreater(total_time, 0, "Total time should be greater than 0")
        plot_graph(self.graph, tsp_path, "time", "test_plot_time.html")
        self.assertTrue(os.path.exists("test_plot_time.html"), "Plot file should be created")

    def test_compute_route_cost(self):
        tsp_path, total_distance, total_cost, total_time = compute_tsp(self.graph, "cost")
        self.assertGreater(len(tsp_path), 1, "TSP path should contain more than one node")
        self.assertGreater(total_distance, 0, "Total distance should be greater than 0")
        self.assertGreater(total_cost, 0, "Total cost should be greater than 0")
        self.assertGreater(total_time, 0, "Total time should be greater than 0")
        plot_graph(self.graph, tsp_path, "cost", "test_plot_cost.html")
        self.assertTrue(os.path.exists("test_plot_cost.html"), "Plot file should be created")

    def tearDown(self):
        # Clean up the generated plot files
        if os.path.exists("test_plot_distance.html"):
            os.remove("test_plot_distance.html")
        if os.path.exists("test_plot_time.html"):
            os.remove("test_plot_time.html")
        if os.path.exists("test_plot_cost.html"):
            os.remove("test_plot_cost.html")

if __name__ == '__main__':
    unittest.main()
