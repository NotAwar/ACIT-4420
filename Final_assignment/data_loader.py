import pandas as pd
import json

def load_relatives():
    """Load relatives' geographic data with street names."""
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
        {"name": "Relative_10", "latitude": 37.5133, "longitude": 127.1028, "street_name": "Jamsil-ro"},
    ]
    return pd.DataFrame(data)

def load_transport_config(config_file="transport_config.json"):
    """Load transport mode configurations."""
    with open(config_file, "r") as file:
        return json.load(file)
