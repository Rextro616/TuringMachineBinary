import tkinter as tk
from tkinter import messagebox
from turingMachine import TuringMachine

class TuringMachineInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Máquina de Turing 0^n1^n")
        self.createInterface()

    def createInterface(self):
        self.tapeLabel = tk.Label(self.root, text="Cinta de entrada:")
        self.tapeLabel.grid(row=0, column=0, padx=10, pady=10)

        self.entryTape = tk.Entry(self.root)
        self.entryTape.grid(row=0, column=1, padx=10, pady=10)

        self.executeButton = tk.Button(self.root, text="Ejecutar", command=self.execute)
        self.executeButton.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.resultLabel = tk.Label(self.root, text="Resultado:")
        self.resultLabel.grid(row=2, column=0, padx=10, pady=10)

        self.resultVariable = tk.StringVar()
        self.labelShowResult = tk.Label(self.root, textvariable=self.resultVariable)
        self.labelShowResult.grid(row=2, column=1, padx=10, pady=10)

    def execute(self):
        tape = self.entryTape.get()  
        if not tape:
            messagebox.showwarning("Entrada inválida", "Por favor ingresa una cinta válida.")
            return

        turingMachine = TuringMachine(tape)

        resultado = turingMachine.start()
        self.resultVariable.set(resultado)
