import tkinter as tk
import random

# Lista de emojis del juego
emojis = ["7️⃣", "☢️", "⚠️"]

# Historial de partidas
juegos = []

def jugar():
    seleccion = []

    # Vaciar la pantalla previa
    resultado_label.config(text="")
    slot1_label.config(text="")
    slot2_label.config(text="")
    slot3_label.config(text="")

    # Mostrar 3 resultados aleatorios
    for i in range(3):
        emoji = random.choice(emojis)
        seleccion.append(emoji)

    # Mostrar resultados en la GUI
    slot1_label.config(text=seleccion[0], font=("Arial", 32))
    slot2_label.config(text=seleccion[1], font=("Arial", 32))
    slot3_label.config(text=seleccion[2], font=("Arial", 32))

    # Verificar si gana
    if seleccion[0] == seleccion[1] == seleccion[2]:
        resultado_label.config(text="🎉 GANASTE 🎉", fg="green")
        juegos.append("Ganó")
    else:
        resultado_label.config(text="Perdiste 😢", fg="red")
        juegos.append("Perdió")

    # Actualizar historial
    actualizar_historial()

def actualizar_historial():
    historial_text.delete("1.0", tk.END)
    for i, estado in enumerate(juegos, start=1):
        historial_text.insert(tk.END, f"Juego {i}: {estado}\n")

def reiniciar():
    juegos.clear()
    historial_text.delete("1.0", tk.END)
    resultado_label.config(text="")
    slot1_label.config(text="")
    slot2_label.config(text="")
    slot3_label.config(text="")

# Interfaz
root = tk.Tk()
root.title("Juego de Emojis SLOT")
root.geometry("350x420")
root.resizable(False, False)

tk.Label(root, text="🎰 Slot Emoji Game 🎰", font=("Arial", 16)).pack(pady=10)

slot_frame = tk.Frame(root)
slot_frame.pack(pady=10)

slot1_label = tk.Label(slot_frame, text="", font=("Arial", 32), width=2)
slot1_label.grid(row=0, column=0, padx=5)

slot2_label = tk.Label(slot_frame, text="", font=("Arial", 32), width=2)
slot2_label.grid(row=0, column=1, padx=5)

slot3_label = tk.Label(slot_frame, text="", font=("Arial", 32), width=2)
slot3_label.grid(row=0, column=2, padx=5)

resultado_label = tk.Label(root, text="", font=("Arial", 14))
resultado_label.pack(pady=10)

tk.Button(root, text="🎮 Jugar", width=15, command=jugar).pack(pady=5)
tk.Button(root, text="🔄 Reiniciar", width=15, command=reiniciar).pack(pady=5)

tk.Label(root, text="📜 Historial", font=("Arial", 12)).pack(pady=5)

historial_text = tk.Text(root, height=8, width=30)
historial_text.pack()

tk.Button(root, text="Salir", command=root.destroy).pack(pady=10)

root.mainloop()
