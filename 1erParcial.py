from funcionesparcial import *

pacientes = []

while True:

    cantidad_pacientes= len(pacientes)

    print_menu()
    opcion = int(input("Ingrese la opción: "))

    while opcion !=1 and cantidad_pacientes==0 and opcion!= 9:
        opcion = int(input("ERROR: NO CUENTA CON PACIENTES. Ingrese la opción: "))

    match opcion:
        case 1:
            cargar_pacientes(pacientes)
        case 2:
            mostrar_lista_pacientes(pacientes)
        case 3:
            buscar_paciente_x_historia_clinica(pacientes)
        case 4:
            ordenar_pacientes_por_número(pacientes)
        case 5:
            encontrar_paciente_mas_dias(pacientes)
        case 6:
            paciente_menos_dias(pacientes)
        case 7:
            cantidad_pacientes_mas_5_dias(pacientes)
        case 8: 
            calcular_promedio_internacion(pacientes)
        case 9: 
            break
        case _:
            print ("OPCION INCORRECTA")

print ("Programa finalizado.")
