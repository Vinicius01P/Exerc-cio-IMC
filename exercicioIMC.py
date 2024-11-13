import tkinter as tk
from tkinter import messagebox


def calcular_imc():
    try:
        altura = float(entry_altura.get()) / 100
        peso = float(entry_peso.get())
        imc = peso / (altura ** 2)
        resultado_label.config(text=f"IMC: {imc:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores válidos para altura e peso.")


def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    resultado_label.config(text="IMC: ")


root = tk.Tk()
root.title("Calculadora de IMC")


tk.Label(root, text="Nome:").grid(row=0, column=0, padx=5, pady=5)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Endereço:").grid(row=1, column=0, padx=5, pady=5)
entry_endereco = tk.Entry(root)
entry_endereco.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Altura (cm):").grid(row=2, column=0, padx=5, pady=5)
entry_altura = tk.Entry(root)
entry_altura.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Peso (kg):").grid(row=3, column=0, padx=5, pady=5)
entry_peso = tk.Entry(root)
entry_peso.grid(row=3, column=1, padx=5, pady=5)


calcular_btn = tk.Button(root, text="Calcular", command=calcular_imc)
calcular_btn.grid(row=4, column=0, padx=5, pady=5)


reiniciar_btn = tk.Button(root, text="Reiniciar", command=reiniciar)
reiniciar_btn.grid(row=4, column=1, padx=5, pady=5)


resultado_label = tk.Label(root, text="IMC: ")
resultado_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


root.mainloop()
