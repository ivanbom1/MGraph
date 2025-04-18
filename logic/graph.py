class MetroGraph:
    def __init__(self):
        self.adjacent_matrix = []
        self.nodes = []

    def add_station(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        
        if name in self.nodes:
            raise ValueError("Station with this name already exists.")
        
        self.nodes.append(name)
        size = len(self.nodes)
        for row in self.adjacent_matrix:
            row.append(0)
        self.adjacent_matrix.append([0] * size)

    def connect_stations(self, idx1, idx2, weight):
        if idx1 >= len(self.nodes) or idx2 >= len(self.nodes):
            raise IndexError("Station index out of range")
        self.adjacent_matrix[idx1][idx2] = weight
        self.adjacent_matrix[idx2][idx1] = weight

    def get_station_idx(self, name):
        if name in self.nodes:
            return self.nodes.index(name)
        raise ValueError(f"Station '{name}' not found")

    def find_shortest_path(self, start_name, end_name):
        pass

    def export_graph_data(self):
        return {
            "nodes": self.nodes,
            "matrix": self.adjacent_matrix
        }

    def import_graph_data(self, data):
        self.nodes = data.get("nodes", [])
        self.adjacent_matrix = data.get("matrix", [])
