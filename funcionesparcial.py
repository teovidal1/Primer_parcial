def print_menu ():
    """Función que imprime el menú"""
    print ("""         
                        MENÚ

        1.CARGAR PACIENTES
        2.MOSTRAR LISTA DE PACIENTES
        3.BUSCAR PACIENTE POR NUMERO HISTORIA CLINICA
        4.ORDENAR PACIENTES POR NUMERO HISTORIA CLINICA
        5.BUSCAR PACIENTE CON MAS DIAS DE INTERNACION
        6.BUSCAR PACIENTE CON MENOS DIAS DE INTERNACION
        7.CONSULTAR CANTIDAD DE PACIENTES CON MAS DE 5 DIAS DE INTERNACION
        8.CONSULTAR EL PROMEDIO DEL TIEMPO DE INTERNACION
        9. SALIR
        """)
    
def cargar_pacientes (pacientes:list[list])->list[list]:
    """Función que agrega una cantidad definida de pacientes con numero clinico, nombre, edad, diagnostico y dias de internación a una lista.

    Args:
        pacientes (list[list]): Arreglo bidimensional 

    Returns:
        list[list]: Retorna la misma lista, con los datos agregados
    """
    cantidad_a_ingresar = int(input("¿Cuántos pacientes desea ingresar?: "))
    for i in range (cantidad_a_ingresar):

        num_hist_clinica = (input(f"Ingrese el número de historia clínica del {i+1}° paciente: "))
        while num_hist_clinica.isdigit()==False:
            num_hist_clinica = input(f"ERROR. Ingrese el número de historia clínica del {i+1}° paciente: ")

        num_hist_clinica=int(num_hist_clinica)

        nombre = input(f"Ingrese el nombre del {i+1}° paciente: ")

        edad = input(f"Ingrese la edad del {i+1}° paciente: ")
        while edad.isdigit()==False or int(edad)<0:
            edad = input(f"ERROR.Ingrese la edad del {i+1}° paciente: ")
        edad=int(edad)

        diagnostico = input(f"Ingrese el diagnóstico del {i+1}° paciente: ")

        dias_de_internacion = input(f"¿Cuántos días de internacion lleva? del {i+1}° paciente: ")
        while dias_de_internacion.isdigit()==False or int(dias_de_internacion)<0:
            dias_de_internacion = input(f"ERROR.¿Cuántos días de internacion lleva? del {i+1}° paciente: ")
        dias_de_internacion=int(dias_de_internacion)
        pacientes.append([num_hist_clinica,nombre,edad,diagnostico,dias_de_internacion])

def mostrar_lista_pacientes (pacientes:list[list]):
    """Printea la matriz

    Args:
        pacientes (list[list]): Arreglo bidimensional
    """
    for i in range (len(pacientes)):
        for j in range (len(pacientes[i])):
            print (pacientes[i][j], end=" // ")
        print ("")

def buscar_paciente_x_historia_clinica (pacientes:list[list]):
    """Busca el número de historia clínica y, si lo encuentra en la matriz, printea todos los datos de esa lista.

    Args:
        pacientes (list[list]): Arreglo bidimensional
    """
    encontrado = False
    paciente_buscado = input ("Ingrese el numero de historia clínica del paciente: ")
    for i in range (len(pacientes)):
        if pacientes[i][0]==paciente_buscado:
            print (f"""El paciente con número {paciente_buscado} se llama {pacientes[i][1]}, tiene {pacientes[i][2]} años de edad. 
                Se le diagnosticó {pacientes[i][3]} y está internado hace {pacientes[i][4]} días""")
            encontrado = True
    if not encontrado:
        print ("NO SE ENCONTRÓ EL PACIENTE BUSCADO.")

def ordenar_pacientes_por_número (pacientes:list[list])->list[list]:
    """Ordena la matriz por su número de historia clinica de cada usuario de forma ascendente

    Args:
        pacientes (list[list]): Arreglo bidimensional
    """
    cantidad_pacientes=len(pacientes)
    for i in range (cantidad_pacientes-1):
        for j in range (cantidad_pacientes-1-i):
            if (pacientes[j][0])>(pacientes[j+1][0]):
                temp = pacientes[j+1]
                pacientes[j+1] = pacientes[j]
                pacientes[j] = temp     

def encontrar_paciente_mas_dias (pacientes:list[list])->list[list]:
    """Busca en la matriz el paciente con más días de internacion y printea sus datos

    Args:
        pacientes (list[list]): Arreglo bidimensional
    """
    paciente_mas_dias = float("-inf")
    cantidad_pacientes = len(pacientes)

    for i in range (cantidad_pacientes):
        if pacientes[i][4]>paciente_mas_dias:
            paciente_mas_dias=pacientes[i][4]
            nombre_paciente_mas_dias = pacientes[i][1]
            numero_historial_paciente_mas_dias = pacientes[i][0]
            edad_paciente_mas_dias = pacientes [i][2]
            diagnostico_paciente_mas_dias = pacientes [i][3]

    print (f"""El paciente con más días es {nombre_paciente_mas_dias}, numero clínico {numero_historial_paciente_mas_dias}. Tiene {edad_paciente_mas_dias} años,
        le diagnosticaron {diagnostico_paciente_mas_dias} y está internado hace {paciente_mas_dias} """)        

def paciente_menos_dias (pacientes:list[list])->list[list]:
    """Busca en la matriz el paciente con menos días de internacion y printea sus datos

    Args:
        pacientes (list[list]): Arreglo bidimensional
    """
    paciente_menos_dias = float("inf")
    cantidad_pacientes = len(pacientes)
    
    for i in range (cantidad_pacientes):
        if pacientes[i][4]<paciente_menos_dias:
            paciente_menos_dias=pacientes[i][4]
            nombre_paciente_menos_dias = pacientes[i][1]
            numero_historial_paciente_menos_dias = pacientes[i][0]
            edad_paciente_menos_dias = pacientes [i][2]
            diagnostico_paciente_menos_dias = pacientes [i][3]

    print (f"""El paciente con menos días es {nombre_paciente_menos_dias}, numero clínico {numero_historial_paciente_menos_dias}. Tiene {edad_paciente_menos_dias} años,
        le diagnosticaron {diagnostico_paciente_menos_dias} y está internado hace {paciente_menos_dias} """)

def cantidad_pacientes_mas_5_dias (pacientes:list[list]):
    """Busca en la matriz a todos los pacientes con más de 5 dias de internacion, printea la cantidad y los nombres de cada uno

    Args:
        pacientes (list[list]): Arreglo bidimensional
    """
    cantidad_mas_5_dias = 0
    lista_pacientes_mas_de_5_dias = []
    for i in range (len(pacientes)):
        if pacientes[i][4]>5:
            cantidad_mas_5_dias+=1
            lista_pacientes_mas_de_5_dias.append(pacientes[i][1])
    print (f"Hay {cantidad_mas_5_dias} pacientes internados hace más de 5 días: ", end= "")
    contador_escritos=0
    for i in range (len(lista_pacientes_mas_de_5_dias)):
        contador_escritos+=1
        if contador_escritos==len(lista_pacientes_mas_de_5_dias):
            print (lista_pacientes_mas_de_5_dias[i])
        elif contador_escritos==(len(lista_pacientes_mas_de_5_dias)-1):
            print (lista_pacientes_mas_de_5_dias[i], end= " y ")
        else:
            print (lista_pacientes_mas_de_5_dias[i], end= ", ")  
    print (" ")         

def calcular_promedio_internacion(pacientes:list[list]):
    """Calcula el promedio de días de internacion que aparecen en la matriz y lo printea

    Args:
        pacientes (list[list]): Arreglo bidimensional
    """
    suma_tiempos_internacion = 0
    for i in range (len(pacientes)):
        suma_tiempos_internacion += pacientes[i][4]
    promedio_tiempo_internacion= suma_tiempos_internacion/(len(pacientes))

    print (f"El tiempo promedio de internación es {promedio_tiempo_internacion}")