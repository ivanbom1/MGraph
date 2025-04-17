import os
import json

SAVE_DIR = "data/saved routes"

def save_route(name, graph_data):
    os.makedirs(SAVE_DIR, exist_ok=True)
    path = os.path.join(SAVE_DIR, f"{name}.json")
    with open(path, "w") as f:
        json.dump(graph_data, f)
        

def load_route(name):
    path = os.path.join(SAVE_DIR, f"{name}.json")
    with open(path, "r") as f:
        return json.load(f)
    
def get_save_folder():
    return SAVE_DIR