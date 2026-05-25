import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

from prever import analisar

janela = tk.Tk()

janela.withdraw()

texto = simpledialog.askstring(
    "Detector",
    "Digite a notícia:"
)

resultado = analisar(texto)
if resultado==0:
    mensagem="Essa noticía é falsa!"
else:
    mensagem="Essa noticia é verdadeira"
messagebox.showinfo(
    "Resultado",
    f"Resultado: {mensagem}"
)