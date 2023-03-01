

def ingresar_venta(dia):
    venta = float(input("Ingrese la venta del " + dia + ": "))
    return venta

def menu():
    print("1. Ingresar ventas por día")
    print("2. Mostrar total de ventas")
    print("3. Mostrar promedio de ventas")
    print("4. Salir")
    opcion = int(input("Seleccione una opción: "))
    return opcion


lunes = martes = miercoles = jueves = viernes = sabado = domingo = 0


dias_semana = 0


while True:
   
    opcion = menu()

    
    if opcion == 1:
        lunes = ingresar_venta("lunes")
        martes = ingresar_venta("martes")
        miercoles = ingresar_venta("miércoles")
        jueves = ingresar_venta("jueves")
        viernes = ingresar_venta("viernes")
        sabado = ingresar_venta("sábado")
        domingo = ingresar_venta("domingo")
        print("Ventas ingresadas exitosamente.")
        dias_semana = 7
   
    elif opcion == 2:
        total = lunes + martes + miercoles + jueves + viernes + sabado + domingo
        print("El total de ventas de la semana es:", total)
   
    elif opcion == 3:
        promedio = (lunes + martes + miercoles + jueves + viernes + sabado + domingo) / dias_semana
        print("El promedio de ventas de la semana es:", promedio)
    
    elif opcion == 4:
        print("Hasta luego!")
        break
    
    else:
        print("Opción inválida. Intente de nuevo.")

