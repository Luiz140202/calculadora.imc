import tkinter as tk
from tkinter import messagebox

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de IMC")

        self.label_height = tk.Label(root, text="Altura (m):")
        self.label_height.grid(row=0, column=0, padx=270, pady=30,)

        self.entry_height = tk.Entry(root)
        self.entry_height.grid(row=0, column=1, padx=10, pady=10)

        self.label_weight = tk.Label(root, text="Peso (kg):")
        self.label_weight.grid(row=1, column=0, padx=270, pady=30)

        self.entry_weight = tk.Entry(root)
        self.entry_weight.grid(row=1, column=1, padx=10, pady=10)

        self.calculate_button = tk.Button(root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=30,)

        self.label_result = tk.Label(root, text="")
        self.label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calculate_bmi(self):
        try:
            height = float(self.entry_height.get())
            weight = float(self.entry_weight.get())
            if height <= 0 or weight <= 0:
                raise ValueError
            bmi = weight / (height ** 2)
            self.label_result.config(text=f"Seu IMC é: {bmi:.2f}")
            self.show_bmi_category(bmi)
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor válido para altura e peso.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 25:
            category = "Peso normal"
        elif 25 <= bmi < 30:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        messagebox.showinfo("Categoria de IMC", f"Sua categoria é: {category}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()
