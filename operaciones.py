# Funciones para realizar las operaciones matemáticas
def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    return num1 / num2

# Función para mostrar el menú y solicitar la opción al usuario
def menu():
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion

# Ciclo principal para solicitar los números y realizar operaciones
while True:
    # Solicitar los números al usuario
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Mostrar el menú y solicitar la opción
    opcion = menu()

    # Realizar la operación seleccionada y mostrar el resultado
    if opcion == 1:
        resultado = sumar(num1, num2)
        print("El resultado de la suma es:", resultado)
    elif opcion == 2:
        resultado = restar(num1, num2)
        print("El resultado de la resta es:", resultado)
    elif opcion == 3:
        resultado = multiplicar(num1, num2)
        print("El resultado de la multiplicación es:", resultado)
    elif opcion == 4:
        resultado = dividir(num1, num2)
        print("El resultado de la división es:", resultado)
    elif opcion == 5:
        print("Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
