from logic.graph import MetroGraph
from logic.datastore import save_route, load_route

# === STEP 1: Create the graph manually ===
graph = MetroGraph()
graph.add_station("A")
graph.add_station("B")
graph.add_station("C")
graph.add_station("D")

graph.connect_stations(0, 1, 4)
graph.connect_stations(1, 2, 2)
graph.connect_stations(2, 3, 7)
graph.connect_stations(0, 3, 15)

data_to_save = graph.export_graph_data()
save_route("test_map", data_to_save)
print("✅ Graph saved as 'test_map.json'")

# === STEP 3: Load it into a new graph ===
loaded_data = load_route("test_map")
new_graph = MetroGraph()
new_graph.import_graph_data(loaded_data)
print("✅ Graph loaded successfully")

# === STEP 4: Run pathfinding ===
path, cost = new_graph.find_shortest_path("A", "D")
print("🔍 Shortest path from A to D:", path)
print("📏 Total cost:", cost)
