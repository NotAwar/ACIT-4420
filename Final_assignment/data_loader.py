import pandas as pd
import json
import logging

def load_relatives():
    """Load relatives data from a predefined list or another source."""
    try:
        # Example of loading data from a predefined list
        data = [
            {"name": "Tarjan_Home", "latitude": 37.5326, "longitude": 126.9247, "street_name": "Yeouido"},
            {"name": "Relative_1", "latitude": 37.4979, "longitude": 127.0276, "street_name": "Gangnam-daero"},
            {"name": "Relative_2", "latitude": 37.4833, "longitude": 127.0322, "street_name": "Yangjae-daero"},
            {"name": "Relative_3", "latitude": 37.5172, "longitude": 127.0286, "street_name": "Sinsa-daero"},
            {"name": "Relative_4", "latitude": 37.5219, "longitude": 127.0411, "street_name": "Apgujeong-ro"},
            {"name": "Relative_5", "latitude": 37.5340, "longitude": 127.0026, "street_name": "Hannam-daero"},
            {"name": "Relative_6", "latitude": 37.5443, "longitude": 127.0557, "street_name": "Seongsu-daero"},
            {"name": "Relative_7", "latitude": 37.5172, "longitude": 127.0391, "street_name": "Cheongdam-ro"},
            {"name": "Relative_8", "latitude": 37.5800, "longitude": 126.9844, "street_name": "Bukhan-ro"},
            {"name": "Relative_9", "latitude": 37.5110, "longitude": 127.0590, "street_name": "Samseong-ro"},
            {"name": "Relative_10", "latitude": 37.5133, "longitude": 127.1028, "street_name": "Jamsil-ro"}
        ]
        relatives = pd.DataFrame(data)
        logging.info(f"Loaded relatives data: {relatives}")
        return relatives
    except Exception as e:
        logging.error(f"Error loading relatives data: {e}")
        raise

def load_transport_config():
    """Load transport configuration from a JSON file."""
    try:
        with open('transport_config.json', 'r') as file:
            transport_config = json.load(file)
        logging.info(f"Loaded transport config: {transport_config}")
        return transport_config
    except Exception as e:
        logging.error(f"Error loading transport config: {e}")
        raise
