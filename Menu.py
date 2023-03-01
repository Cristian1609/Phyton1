import math

while True:
    print("=== MENÚ ===")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Circunferencia")
    print("4. Salir")
    opcion = input("Selecciona una opción (1-4): ")

    if opcion == "1":
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        lado1 = float(input("Ingresa el lado 1 del triángulo: "))
        lado2 = float(input("Ingresa el lado 2 del triángulo: "))
        lado3 = float(input("Ingresa el lado 3 del triángulo: "))
        area = (base * altura) / 2
        perimetro = lado1 + lado2 + lado3
        print(f"El área del triángulo es: {area}")
        print(f"El perímetro del triángulo es: {perimetro}")

    elif opcion == "2":
        lado = float(input("Ingresa el lado del cuadrado: "))
        area = lado ** 2
        perimetro = lado * 4
        print(f"El área del cuadrado es: {area}")
        print(f"El perímetro del cuadrado es: {perimetro}")

    elif opcion == "3":
        radio = float(input("Ingresa el radio de la circunferencia: "))
        area = math.pi * (radio ** 2)
        perimetro = 2 * math.pi * radio
        print(f"El área de la circunferencia es: {area}")
        print(f"El perímetro de la circunferencia es: {perimetro}")

    elif opcion == "4":
        break
    else:
        print("Opción inválida. Intente de nuevo.")
