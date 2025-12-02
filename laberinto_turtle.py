import turtle

TAM = 24

mapa = [
    "XXXXXXXXXXXXXXXXXXXXXXXX",
    "XP        X           X",
    "X XXX X XX XXXXXXXX X X",
    "X   X         X    X  X",
    "XXX X XXXX X XXXX X X X",
    "X   X   X  X      X   X",
    "X XXX X X  X X  X XXXXX",
    "X   X X   X X   X  GX X",
    "XXXXXXXXXXXXXXXXXXXXXXXX"
]

dibujante = turtle.Turtle()
dibujante.hideturtle()
dibujante.penup()
dibujante.speed(0)

jugador = turtle.Turtle()
jugador.shape("square")
jugador.color("blue")
jugador.penup()
jugador.speed(0)

meta = (0, 0)

def dibujar_cuadro(x, y, color):
    dibujante.goto(x, y)
    dibujante.color(color)
    dibujante.begin_fill()
    for _ in range(4):
        dibujante.forward(TAM)
        dibujante.right(90)
    dibujante.end_fill()

paredes = []

def crear_laberinto():
    global meta

    inicio_x = - (len(mapa[0]) // 2) * TAM
    inicio_y = (len(mapa) // 2) * TAM

    for fila in range(len(mapa)):
        for col in range(len(mapa[fila])):
            c = mapa[fila][col]

            x = inicio_x + col * TAM
            y = inicio_y - fila * TAM

            if c == "X":
                dibujar_cuadro(x, y, "black")
                paredes.append((x + TAM/2, y - TAM/2))

            elif c == "P":
                jugador.goto(x + TAM/2, y - TAM/2)

            elif c == "G":
                dibujar_cuadro(x, y, "green")
                meta = (x + TAM/2, y - TAM/2)

def puede_moverse(x, y):
    return (x, y) not in paredes

def mover(dx, dy):
    nuevo_x = jugador.xcor() + dx
    nuevo_y = jugador.ycor() + dy

    if puede_moverse(nuevo_x, nuevo_y):
        jugador.goto(nuevo_x, nuevo_y)

        if (nuevo_x, nuevo_y) == meta:
            jugador.color("gold")
            jugador.write("  ¡GANASTE!", font=("Arial", 16, "bold"))
            turtle.done()

def arriba(): mover(0, TAM)
def abajo(): mover(0, -TAM)
def izquierda(): mover(-TAM, 0)
def derecha(): mover(TAM, 0)

pantalla = turtle.Screen()
pantalla.title("Laberinto Turtle")

crear_laberinto()

pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(izquierda, "Left")
pantalla.onkeypress(derecha, "Right")

turtle.done()
