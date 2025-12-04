import tkinter as tk
import random

root = tk.Tk()
root.title("Juego del Dado")
root.geometry("300x260")
root.resizable(False, False)

lbl_instr = tk.Label(root, text="Adivina el número del dado (1-6):", font=("Arial", 12))
lbl_instr.pack(pady=10)

entry_num = tk.Entry(root, font=("Arial", 12), justify="center")
entry_num.pack(pady=5)

lbl_resultado = tk.Label(root, text="", font=("Arial", 14))
lbl_resultado.pack(pady=20)


def lanzar_dado():
    try:
        usuario = int(entry_num.get())
        if usuario < 1 or usuario > 6:
            lbl_resultado.config(text="Número inválido. Solo 1 a 6.")
            return

        dado = random.randint(1, 6)

        if usuario == dado:
            lbl_resultado.config(text=f"Salió {dado} 🎉 Ganaste!")
        else:
            lbl_resultado.config(text=f"Salió {dado} ❌ Perdiste")
    except:
        lbl_resultado.config(text="Escribe un número válido")


btn_jugar = tk.Button(root, text="Lanzar Dado", font=("Arial", 12), command=lanzar_dado)
btn_jugar.pack(pady=10)

root.mainloop()
