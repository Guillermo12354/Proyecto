import tkinter as tk
from tkinter import ttk
import math
import subprocess
import sys
import os

root = tk.Tk()
root.title("MultiApp - Menú Principal")
root.geometry("400x500")
root.resizable(False, False)

def abrir_menu():
    frame_areas.pack_forget()
    frame_calc.pack_forget()
    frame_menu.pack(fill="both", expand=True)

def abrir_calculadora_areas():
    frame_menu.pack_forget()
    frame_calc.pack_forget()
    frame_areas.pack(fill="both", expand=True)

def abrir_calculadora_normal():
    frame_menu.pack_forget()
    frame_areas.pack_forget()
    frame_calc.pack(fill="both", expand=True)


def abrir_carreras():
    archivo = os.path.join(os.getcwd(), "carreras_turtle.py")
    subprocess.Popen([sys.executable, archivo])

def abrir_laberinto():
    archivo = os.path.join(os.getcwd(), "laberinto_turtle.py")
    subprocess.Popen([sys.executable, archivo])


frame_menu = tk.Frame(root)

titulo = tk.Label(frame_menu, text="MENÚ PRINCIPAL", font=("Arial", 18))
titulo.pack(pady=20)

btn1 = ttk.Button(frame_menu, text="Calculadora de Áreas", width=30, command=abrir_calculadora_areas)
btn1.pack(pady=10)

btn2 = ttk.Button(frame_menu, text="Calculadora Normal", width=30, command=abrir_calculadora_normal)
btn2.pack(pady=10)

btn3 = ttk.Button(frame_menu, text="Juego de Carreras", width=30, command=abrir_carreras)
btn3.pack(pady=10)

btn4 = ttk.Button(frame_menu, text="Laberinto", width=30, command=abrir_laberinto)
btn4.pack(pady=10)

frame_menu.pack(fill="both", expand=True)



frame_areas = tk.Frame(root)

titulo2 = tk.Label(frame_areas, text="Calculadora de Áreas", font=("Arial", 16))
titulo2.pack(pady=10)

label_fig = tk.Label(frame_areas, text="Selecciona una figura:")
label_fig.pack()

combo_fig = ttk.Combobox(frame_areas, values=["Círculo", "Cuadrado", "Triángulo"])
combo_fig.pack(pady=5)

frame_inputs = tk.Frame(frame_areas)
frame_inputs.pack(pady=10)

label_res = tk.Label(frame_areas, text="", font=("Arial", 14))
label_res.pack()

def actualizar_inputs(*args):
    for widget in frame_inputs.winfo_children():
        widget.destroy()

    seleccion = combo_fig.get()

    if seleccion == "Círculo":
        tk.Label(frame_inputs, text="Radio:").pack()
        entry_r = tk.Entry(frame_inputs)
        entry_r.pack()

        def calcular():
            r = float(entry_r.get())
            area = math.pi * r * r
            label_res.config(text=f"Área: {area:.2f}")

        ttk.Button(frame_inputs, text="Calcular", command=calcular).pack(pady=5)

    elif seleccion == "Cuadrado":
        tk.Label(frame_inputs, text="Lado:").pack()
        entry_l = tk.Entry(frame_inputs)
        entry_l.pack()

        def calcular():
            lado = float(entry_l.get())
            area = lado * lado
            label_res.config(text=f"Área: {area:.2f}")

        ttk.Button(frame_inputs, text="Calcular", command=calcular).pack(pady=5)

    elif seleccion == "Triángulo":
        tk.Label(frame_inputs, text="Base:").pack()
        entry_b = tk.Entry(frame_inputs)
        entry_b.pack()

        tk.Label(frame_inputs, text="Altura:").pack()
        entry_h = tk.Entry(frame_inputs)
        entry_h.pack()

        def calcular():
            base = float(entry_b.get())
            altura = float(entry_h.get())
            area = (base * altura) / 2
            label_res.config(text=f"Área: {area:.2f}")

        ttk.Button(frame_inputs, text="Calcular", command=calcular).pack(pady=5)

combo_fig.bind("<<ComboboxSelected>>", actualizar_inputs)

btn_regresar_areas = ttk.Button(frame_areas, text="Volver al menú", command=abrir_menu)
btn_regresar_areas.pack(pady=20)


frame_calc = tk.Frame(root)

tk.Label(frame_calc, text="Calculadora Normal", font=("Arial", 16)).pack(pady=10)

frame_calc_inputs = tk.Frame(frame_calc)
frame_calc_inputs.pack(pady=10)

tk.Label(frame_calc_inputs, text="Valor 1:").grid(row=0, column=0)
entry_a = tk.Entry(frame_calc_inputs)
entry_a.grid(row=0, column=1)

tk.Label(frame_calc_inputs, text="Valor 2:").grid(row=1, column=0)
entry_b = tk.Entry(frame_calc_inputs)
entry_b.grid(row=1, column=1)

label_calc_res = tk.Label(frame_calc, text="", font=("Arial", 14))
label_calc_res.pack(pady=10)

def sumar():
    a = float(entry_a.get())
    b = float(entry_b.get())
    label_calc_res.config(text=f"Resultado: {a+b}")

def restar():
    a = float(entry_a.get())
    b = float(entry_b.get())
    label_calc_res.config(text=f"Resultado: {a-b}")

def multiplicar():
    a = float(entry_a.get())
    b = float(entry_b.get())
    label_calc_res.config(text=f"Resultado: {a*b}")

def dividir():
    a = float(entry_a.get())
    b = float(entry_b.get())
    if b == 0:
        label_calc_res.config(text="No se puede dividir entre 0")
    else:
        label_calc_res.config(text=f"Resultado: {a/b}")

# BOTONES

frame_botones_calc = tk.Frame(frame_calc)
frame_botones_calc.pack(pady=10)

ttk.Button(frame_botones_calc, text="Sumar", width=12, command=sumar).grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_botones_calc, text="Restar", width=12, command=restar).grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_botones_calc, text="Multiplicar", width=12, command=multiplicar).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(frame_botones_calc, text="Dividir", width=12, command=dividir).grid(row=1, column=1, padx=5, pady=5)

ttk.Button(frame_calc, text="Volver al menú", command=abrir_menu).pack(pady=20)


root.mainloop()
