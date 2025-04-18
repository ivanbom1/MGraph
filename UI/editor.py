import tkinter as tk
from tkinter import simpledialog, messagebox, colorchooser
from logic.datastore import save_route
import json
import os

station_radius = 10
stations_ui = {}

def start_editor(root, graph, file_path):
    global stations_ui
    stations_ui = {}

    try:
        with open(file_path, "r") as f:
            data = json.load(f)
            stations_ui = data.get("stations_ui", {})
    except:
        stations_ui = {}

    stations_ui = {name: info for name, info in stations_ui.items() if name in graph.nodes}

    canvas = tk.Canvas(root, bg="white")
    canvas.pack(fill="both", expand=True)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    def redraw():
        canvas.delete("all")

        matrix = graph.adjacent_matrix
        for i, name1 in enumerate(graph.nodes):
            for j, name2 in enumerate(graph.nodes):
                if i < j and matrix[i][j] > 0:
                    if name1 in stations_ui and name2 in stations_ui:
                        x1, y1 = stations_ui[name1]['coords']
                        x2, y2 = stations_ui[name2]['coords']
                        canvas.create_line(x1, y1, x2, y2, width=2)

        for name in graph.nodes:
            if name not in stations_ui:
                continue

            info = stations_ui[name]
            x, y = info['coords']
            color = info['color']
            line = info.get('line', "")

            canvas.create_oval(
                x - station_radius, y - station_radius,
                x + station_radius, y + station_radius,
                fill=color, outline="black"
            )
            canvas.create_text(x, y - 15, text=name, font=("Arial", 10, "bold"))
            if line:
                canvas.create_text(x, y + 15, text=f"({line})", font=("Arial", 8), fill="gray")

    def add_station():
        name = simpledialog.askstring("Station Name", "Enter the station name:")
        if not name:
            return

        line = simpledialog.askstring("Line Name", "Enter metro line name (optional):") or ""

        color = colorchooser.askcolor(title="Choose Station Color")[1]
        if not color:
            color = "gray"

        messagebox.showinfo("Place Station", f"Click on the canvas to place station '{name}'.")

        def place_station(event):
            canvas.unbind("<Button-1>")

            try:
                graph.add_station(name)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return

            stations_ui[name] = {
                'coords': (event.x, event.y),
                'color': color,
                'line': line
            }

            redraw()

        canvas.bind("<Button-1>", place_station)

    def connect_stations():
        if len(graph.nodes) < 2:
            return messagebox.showerror("Error", "At least 2 stations required.")

        s1 = simpledialog.askstring("Connect From", "Enter first station name:")
        s2 = simpledialog.askstring("Connect To", "Enter second station name:")
        if s1 not in graph.nodes or s2 not in graph.nodes:
            return messagebox.showerror("Error", "One or both stations not found.")

        try:
            weight = int(simpledialog.askstring("Weight", "Enter distance (e.g. 1):"))
        except:
            return messagebox.showerror("Error", "Invalid weight.")

        i1 = graph.nodes.index(s1)
        i2 = graph.nodes.index(s2)
        graph.connect_stations(i1, i2, weight)
        redraw()

    def save_graph():
        if file_path:
            data = {
                "nodes": graph.nodes,
                "matrix": graph.adjacent_matrix,
                "stations_ui": stations_ui
            }
            with open(file_path, "w") as f:
                json.dump(data, f, indent=4)
                
            messagebox.showinfo("Saved", "Map saved successfully!")

    tk.Button(button_frame, text="Add Station", command=add_station).pack(side="left", padx=10)
    tk.Button(button_frame, text="Add Connection", command=connect_stations).pack(side="left", padx=10)
    tk.Button(button_frame, text="Save Map", command=save_graph).pack(side="left", padx=10)

    redraw()
