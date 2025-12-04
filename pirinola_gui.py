import tkinter as tk
import random

root = tk.Tk()
root.title("Pirinola - Juego")
root.geometry("350x330")
root.resizable(False, False)

# ==== VARIABLES DEL JUEGO ====
jugadores = ["Jugador 1", "Jugador 2"]
turno = 0
puntos = [5, 5]  # cada jugador inicia con 5 fichas

opciones = [
    "Toma 1",
    "Toma 2",
    "Pon 1",
    "Pon 2",
    "Todos ponen",
    "Toma todo"
]

# ===== UI =====
lbl_turno = tk.Label(root, text=f"Turno de: {jugadores[turno]}", font=("Arial", 12))
lbl_turno.pack(pady=5)

lbl_puntos = tk.Label(root, text="", font=("Arial", 12))
lbl_puntos.pack(pady=5)

lbl_resultado = tk.Label(root, text="", font=("Arial", 18))
lbl_resultado.pack(pady=15)

btn_girar = tk.Button(root, text="Girar Pirinola", font=("Arial", 12), command=lambda: girar())
btn_girar.pack(pady=10)

lbl_mensaje = tk.Label(root, text="", font=("Arial", 10), fg="blue")
lbl_mensaje.pack(pady=10)


def actualizar_tablero(mensaje=""):
    """Actualiza el texto en pantalla"""
    lbl_turno.config(text=f"Turno de: {jugadores[turno]}")
    lbl_puntos.config(text=f"{jugadores[0]}: {puntos[0]} puntos   |   {jugadores[1]}: {puntos[1]} puntos")
    lbl_mensaje.config(text=mensaje)


def verificar_ganador():
    """Revisa si un jugador ganó"""
    if puntos[0] <= 0:
        lbl_resultado.config(text="Ganó Jugador 2 🎉")
        reiniciar()
        return True
    elif puntos[1] <= 0:
        lbl_resultado.config(text="Ganó Jugador 1 🎉")
        reiniciar()
        return True
    return False


def reiniciar():
    """Reinicia el juego automáticamente después de 3 sec"""
    root.after(3000, nuevo_juego)


def nuevo_juego():
    global turno, puntos
    puntos = [5, 5]
    turno = 0
    lbl_resultado.config(text="")
    actualizar_tablero("Nuevo juego iniciado.")


def girar():
    """Aplica efecto de pirinola"""
    global turno, puntos

    resultado = random.choice(opciones)
    lbl_resultado.config(text=resultado)

    jugador = turno
    otro = 1 - turno

    # ===== EFECTOS =====
    if resultado == "Toma 1":
        puntos[jugador] += 1

    elif resultado == "Toma 2":
        puntos[jugador] += 2

    elif resultado == "Pon 1":
        puntos[jugador] -= 1

    elif resultado == "Pon 2":
        puntos[jugador] -= 2

    elif resultado == "Todos ponen":
        puntos[0] -= 1
        puntos[1] -= 1

    elif resultado == "Toma todo":
        puntos[jugador] += puntos[otro]
        puntos[otro] = 0

    # Evitar puntos negativos
    puntos[0] = max(0, puntos[0])
    puntos[1] = max(0, puntos[1])

    # ¿Ya hay ganador?
    if verificar_ganador():
        return

    # Cambiar turno
    turno = 1 - turno
    actualizar_tablero()


# Iniciar tablero
actualizar_tablero()

root.mainloop()
