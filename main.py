import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import json
import os

from UI.editor import start_editor
from logic.graph import MetroGraph
from logic.datastore import load_route, save_route, get_save_folder

SAVE_FOLDER = get_save_folder()
os.makedirs(SAVE_FOLDER, exist_ok=True)

class MetroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Metro Route Creator")
        self.root.geometry("1280x720")
        self.graph = MetroGraph()
        self.current_file = None
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()

        tk.Button(self.root, text="Create New File +", width=25, height=2, command=self.create_new_file).pack(pady=10)
        tk.Button(self.root, text="Open File", width=25, height=2, command=self.open_existing_file).pack(pady=10)

    def create_new_file(self):
        file_name = simpledialog.askstring("New File", "Enter name for a new metro map: ")
        if file_name:
            self.graph = MetroGraph()
            self.current_file = os.path.join(SAVE_FOLDER, f"{file_name}.json")
            self.save_current_graph()
            messagebox.showinfo("Created", f"New metro file {file_name}.json created!")
            self.open_editor()

    def open_existing_file(self):
        filepath = filedialog.askopenfilename(
            title="Open Metro File",
            filetypes=[("JSON Files", "*.json")],
            initialdir=SAVE_FOLDER
        )

        if filepath:
            with open(filepath, "r") as f:
                data = json.load(f)
                self.graph = MetroGraph()
                self.graph.import_graph_data(data)
                self.current_file = filepath
                messagebox.showinfo("Opened", f"Opened metro file: {os.path.basename(filepath)}")
                self.open_editor()

    def save_current_graph(self):
        if self.current_file:
            with open(self.current_file, "w") as f:
                json.dump(self.graph.export_graph_data(), f, indent=4)

    def open_editor(self):
        self.clear_window()
        start_editor(self.root, self.graph, self.current_file)
        
        #tk.Button(self.root, text="Back to Menu", command=self.create_main_menu).pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()    

if __name__ == "__main__":
    root = tk.Tk()
    app = MetroApp(root)
    root.mainloop()
