import tkinter as tk
from tkinter import ttk
import requests

class CyberCriminalSoftware:
    def __init__(self, root):
        self.root = root
        self.root.title("Cyber Criminal Software")
        self.root.geometry("500x300")

        self.label = ttk.Label(self.root, text="Enter the target URL:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(self.root, width=50)
        self.entry.pack(pady=10)

        self.button = ttk.Button(self.root, text="Gather Information", command=self.gather_info)
        self.button.pack(pady=10)

        self.text = tk.Text(self.root, height=10, width=50)
        self.text.pack(pady=10)

    def gather_info(self):
        url = self.entry.get()
        response = requests.get(url)
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, response.text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CyberCriminalSoftware(root)
    root.mainloop()