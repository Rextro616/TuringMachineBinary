import tkinter as tk
from interface import TuringMachineInterface

if __name__ == "__main__":
    root = tk.Tk()
    app = TuringMachineInterface(root)
    root.mainloop()