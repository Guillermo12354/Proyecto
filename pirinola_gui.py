import tkinter as tk
import random

root = tk.Tk()
root.title("Pirinola - Juego")
root.geometry("350x330")
root.resizable(False, False)

# ==== VARIABLES DEL JUEGO ====
jugadores = ["Jugador 1", "Jugador 2"]
turno = 0
puntos = [5, 5]

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

btn_girar = tk.Button(root, text="Girar Pirinola", font=("Arial", 12))
btn_girar.pack(pady=10)

lbl_mensaje = tk.Label(root, text="", font=("Arial", 10), fg="blue")
lbl_mensaje.pack(pady=10)


def actualizar_tablero(mensaje=""):
    lbl_turno.config(text=f"Turno de: {jugadores[turno]}")
    lbl_puntos.config(text=f"{jugadores[0]}: {puntos[0]} puntos   |   {jugadores[1]}: {puntos[1]} puntos")
    lbl_mensaje.config(text=mensaje)


def verificar_ganador():
    # EMPATE
    if puntos[0] == 0 and puntos[1] == 0:
        lbl_resultado.config(text="Empate")
        btn_girar.config(state="disabled")
        reiniciar()
        return True

    # GANADORES normales
    if puntos[0] == 0:
        lbl_resultado.config(text="Ganó Jugador 2 🎉")
        btn_girar.config(state="disabled")
        reiniciar()
        return True

    if puntos[1] == 0:
        lbl_resultado.config(text="Ganó Jugador 1 🎉")
        btn_girar.config(state="disabled")
        reiniciar()
        return True

    return False


def reiniciar():
    # Reinicio suave sin parpadeos
    root.after(3000, nuevo_juego)


def nuevo_juego():
    global turno, puntos
    puntos = [5, 5]
    turno = 0
    lbl_resultado.config(text="")
    btn_girar.config(state="normal")
    actualizar_tablero("Nuevo juego iniciado.")


def girar():
    global turno, puntos

    # Bloquear botón para evitar doble clic (evitara acciines inecesarias)
    btn_girar.config(state="disabled")

    resultado = random.choice(opciones)
    lbl_resultado.config(text=resultado)

    jugador = turno
    otro = 1 - turno

    # EFECTOS
    if resultado == "Toma 1":
        puntos[jugador] += 1

    elif resultado == "Toma 2":
        puntos[jugador] += 2

    elif resultado == "Pon 1":
        puntos[jugador] = max(0, puntos[jugador] - 1)

    elif resultado == "Pon 2":
        puntos[jugador] = max(0, puntos[jugador] - 2)

    elif resultado == "Todos ponen":
        puntos[0] = max(0, puntos[0] - 1)
        puntos[1] = max(0, puntos[1] - 1)

    elif resultado == "Toma todo":
        puntos[jugador] += puntos[otro]
        puntos[otro] = 0

    # ¿Ya hay ganador?
    if verificar_ganador():
        return

    # CAMBIO DE TURNO (solo si el juego sigue)
    turno = 1 - turno
    actualizar_tablero("Turno cambiado.")

    # Rehabilitar botón otra vez
    btn_girar.config(state="normal")


# Enlazar botón 
btn_girar.config(command=girar)

# Iniciar tablero
actualizar_tablero()

root.mainloop()
