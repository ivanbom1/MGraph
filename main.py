from UI.editor import start_editor
from logic.graph import MetroGraph
from logic.datastore import load_route

if __name__ == "__main__":
    start_editor()

data = load_route("my_route")  # <- this is the "data" dict
graph = MetroGraph()
graph.import_data(data)

