estudiantes = []
continuar = True

while continuar:
    nombre = input("Ingresa el nombre del estudiante: ")
    p1 = float(input("Ingresa la nota de la primera evaluación: "))
    p2 = float(input("Ingresa la nota de la segunda evaluación: "))
    p3 = float(input("Ingresa la nota de la tercera evaluación: "))
    definitiva = (p1 + p2 + p3) / 3
    estudiantes.append((nombre, definitiva))
    respuesta = input("¿Desea ingresar más datos? (s/n): ")
    if respuesta == "n"  :
        continuar = False

num_aprobados = 0
num_reprobados = 0
promedio_total = 0

for estudiante in estudiantes:
    nombre = estudiante[0]
    definitiva = estudiante[1]
    promedio_total += definitiva

    if definitiva >= 3:
        print(f"{nombre} ha aprobado con una definitiva de {definitiva:.2f}")
        num_aprobados += 1
    else:
        print(f"{nombre} ha reprobado con una definitiva de {definitiva:.2f}")
        num_reprobados += 1

promedio_total /= len(estudiantes)
print(f"\nResumen:")
print(f"Cantidad de aprobados: {num_aprobados}")
print(f"Cantidad de reprobados: {num_reprobados}")
print(f"Promedio total de las definitivas: {promedio_total:.2f}")
