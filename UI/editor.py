import tkinter as tk

def start_editor():
    root = tk.Tk()
    root.title("Metro Route Creator")
    root.geometry("1280x720")

    label = tk.Label(root, text="Welcome to MGraph route creator!", font=("Times New Roman", 24))
    label.pack(pady=20)

    root.mainloop()