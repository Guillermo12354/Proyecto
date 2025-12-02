print("Bienvenidos a la calculadora")

def sumar():
    a = int(input("Dame el primer valor: "))
    b = int(input("Dame el segundo valor: "))
    resultado = a + b
    print(f"El resultado de la suma es {resultado}")

def restar():
    a = int(input("Dame el primer valor: "))
    b = int(input("Dame el segundo valor: "))
    resultado = a - b
    print(f"El resultado de la resta es {resultado}")

def multiplicar():
    a = int(input("Dame el primer valor: "))
    b = int(input("Dame el segundo valor: "))
    resultado = a * b
    print(f"El resultado de la multiplicación es {resultado}")

def dividir():
    a = int(input("Dame el primer valor: "))
    b = int(input("Dame el segundo valor: "))
    if b == 0:
        print("No se puede dividir entre 0")
    else:
        resultado = a / b
        print(f"El resultado de la división es {resultado}")

def menu():
    print("\n--- MENÚ ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    seleccion = int(input("Selecciona una opción: "))

    if seleccion == 1:
        sumar()
    elif seleccion == 2:
        restar()
    elif seleccion == 3:
        multiplicar()
    elif seleccion == 4:
        dividir()
    else:
        print("Opción no válida")

repetir = "s"
while repetir.lower() == "s":
    menu()
    repetir = input("Presiona 's' para continuar: ")
