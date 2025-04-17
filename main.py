import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import json
import os

from UI.editor import start_editor
from logic.graph import MetroGraph
from logic.datastore import load_route


if __name__ == "__main__":
    start_editor()

data = load_route("my_route")  # <- this is the "data" dict
graph = MetroGraph()
graph.import_data(data)

SAVE_FOLDER = "saved_routes"
os.makedirs(SAVE_FOLDER, exist_ok=True)

class MetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metro Route Creator")
        self.graph = MetroGraph()
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        tk.Button(self.root, text="Create New File +", width=25, height=2, command=self.open_existing_file).pack(pady=10)

        tk.Button(self.root, text="Open File", width=25, height=2, command=self.open_existing_file).pack(pady=10)

    