# Función para calcular el factorial de un número
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Pedir al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Calcular el factorial del número ingresado
fact = factorial(numero)
print("El factorial de", numero, "es", fact)

# Inicializar variables para contar números pares e impares, y para acumular sus valores
num_pares = 0
acum_pares = 0
num_impares = 0
acum_impares = 0

# Recorrer los números del 1 al número ingresado, contar y acumular los valores pares e impares
for i in range(1, numero+1):
    if i % 2 == 0:
        num_pares += 1
        acum_pares += i
    else:
        num_impares += 1
        acum_impares += i

# Imprimir los resultados
print("Cantidad de números pares:", num_pares)
print("Valor acumulado de los pares:", acum_pares)
print("Cantidad de números impares:", num_impares)
print("Valor acumulado de los impares:", acum_impares)
