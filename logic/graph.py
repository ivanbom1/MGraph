class MetroGraph:
    def __init__(self):
        self.adjacent_matrix = []
        self.nodes = []
    
    def add_station(self, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        
        self.nodes.append(name)

        size = len(self.nodes)
        for row in self.adjacent_matrix:
            row.append(0)
        self.adjacent_matrix.append([0]*size)

    
    def connect_stations(self, idx1, idx2, weight=1):
        if idx1 >= len(self.nodes) or idx2 >= len(self.nodes):
            raise IndexError("Station index is out of range")
        
        self.adjacent_matrix[idx1][idx2] = weight
        self.adjacent_matrix[idx2][idx1] = weight

    def get_station_idx(self, name):
        if name in self.nodes:
            return self.nodes.index(name)
        else:
            raise ValueError(f"Station {name} not found")

    def find_shortest_path(self, start, end):
        pass

    def __str__(self):
        return f"Stations: {self.nodes}\nMatrix: {self.adjacent_matrix}"
