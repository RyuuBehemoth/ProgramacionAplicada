import tkinter as tk
from tkinter import messagebox
from classes import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Calculadora Básica")

        self.num1_entry = tk.Entry(root, width=10)
        self.num1_entry.grid(row=0, column=1)

        self.num2_entry = tk.Entry(root, width=10)
        self.num2_entry.grid(row=1, column=1)

        tk.Label(root, text="Número 1:").grid(row=0, column=0)
        tk.Label(root, text="Número 2:").grid(row=1, column=0)

        # Botones para cada operación
        tk.Button(root, text="Sumar", command=self.sumar).grid(row=2, column=0)
        tk.Button(root, text="Restar", command=self.restar).grid(row=2, column=1)
        tk.Button(root, text="Multiplicar", command=self.multiplicar).grid(row=3, column=0)
        tk.Button(root, text="Dividir", command=self.dividir).grid(row=3, column=1)
        tk.Button(root, text="Módulo", command=self.modulo).grid(row=4, column=0)

        self.result_label = tk.Label(root, text="Resultado: ")
        self.result_label.grid(row=5, column=0, columnspan=2)

    def get_values(self):
        try:
            a = int(self.num1_entry.get())
            b = int(self.num2_entry.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")
            return None, None

    def mostrar_resultado(self, resultado):
        self.result_label.config(text=f"Resultado: {resultado}")

    def sumar(self):
        a, b = self.get_values()
        if a is not None:
            self.mostrar_resultado(self.calc.add(a, b))

    def restar(self):
        a, b = self.get_values()
        if a is not None:
            self.mostrar_resultado(self.calc.substract(a, b))

    def multiplicar(self):
        a, b = self.get_values()
        if a is not None:
            self.mostrar_resultado(self.calc.multiply(a, b))

    def dividir(self):
        a, b = self.get_values()
        if a is not None:
            try:
                self.mostrar_resultado(self.calc.divide(a, b))
            except:
                messagebox.showerror("Error", "No se puede dividir entre cero.")

    def modulo(self):
        a, b = self.get_values()
        if a is not None:
            try:
                self.mostrar_resultado(self.calc.module(a, b))
            except:
                messagebox.showerror("Error", "No se puede dividir entre cero.")

# Ejecutar la interfaz
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
