import turtle
import random

carros = []
colores = ["red", "blue", "green", "orange"]

for i in range(4):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(colores[i])
    t.penup()
    t.goto(-200, 100 - i * 50)
    carros.append(t)

meta = 10
posiciones = [0, 0, 0, 0]
ganador = None

while not ganador:
    for i in range(4):
        avance = random.randint(0, 1)
        posiciones[i] += avance
        carros[i].forward(avance * 20)
        if posiciones[i] >= meta:
            ganador = i
            break

turtle.done()
