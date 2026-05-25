import tkinter as tk
from tkinter import messagebox

from prever import analisar

def executar():

    texto = entrada.get("1.0", tk.END)

    resultado = analisar(texto)
    if resultado==0:
        resultado="Essa noticia é falsa!"
    else:
        resultado="Essa noticia é real"
    messagebox.showinfo(
        "Resultado",
        f"Resultado: {resultado}"
    )

janela = tk.Tk()

janela.title("Detector de Fake News")

janela.geometry("700x400")

titulo = tk.Label(
    janela,
    text="Digite a notícia:",
    font=("Arial", 16)
)

titulo.pack(pady=10)

entrada = tk.Text(
    janela,
    width=70,
    height=12,
    font=("Arial", 12)
)

entrada.pack(pady=10)

botao = tk.Button(
    janela,
    text="Analisar",
    command=executar,
    font=("Arial", 12)
)

botao.pack(pady=10)

janela.mainloop()