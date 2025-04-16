import heapq

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
        self.adjacent_matrix.append([0] * size)

    def connect_stations(self, idx1, idx2, weight):
        if idx1 >= len(self.nodes) or idx2 >= len(self.nodes):
            raise IndexError("Station index is out of range")

        self.adjacent_matrix[idx1][idx2] = weight
        self.adjacent_matrix[idx2][idx1] = weight

    def get_station_idx(self, name):
        if name in self.nodes:
            return self.nodes.index(name)
        else:
            raise ValueError(f"Station {name} not found")

    def find_shortest_path(self, start_name, end_name):
        start = self.get_station_idx(start_name)
        end = self.get_station_idx(end_name)
        n = len(self.nodes)

        distances = [float("inf")] * n
        prev = [None] * n
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_distance, current_node = heapq.heappop(queue)

            if current_node == end:
                break

            for neighbor, weight in enumerate(self.adjacent_matrix[current_node]):
                if weight > 0:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        prev[neighbor] = current_node
                        heapq.heappush(queue, (distance, neighbor))

        path = []
        pos = end
        while pos is not None:
            path.append(self.nodes[pos])
            pos = prev[pos]
        path.reverse()

        return path, distances[end] if distances[end] != float("inf") else ([], None)

    def export_graph_data(self):
        return {
            "nodes": self.nodes,
            "matrix": self.adjacent_matrix
        }

    def import_graph_data(self, data):
        self.nodes = data.get("nodes", [])
        self.adjacent_matrix = data.get("matrix", [])

    def __str__(self):
        return f"Stations: {self.nodes}\nMatrix: {self.adjacent_matrix}"
