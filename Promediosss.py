# Se definen los contadores
aprobado = 0
reprobado = 0
suma_notas = 0

# Se le pide al usuario la cantidad de alumnos
alumnos = int(input("¿Cuantas notas quiere ingresar? \n"))

# Se pregunta por cada alumno
for a in range(alumnos):

    # Se le pide al usuario la cantidad de notas que quiere ingresar
    cant = int(input("¿Cuantas notas quiere ingresar? \n"))
    
    # Se pide la nota segun la cantidad ya pedida
    for a in range(cant):
        nota = float(input("Ingrese su nota: "))
        suma_notas = suma_notas + nota
    
    # Se calcula el promedio
    prom = suma_notas/cant

    # vuelve la sumatoria de notas a 0
    suma_notas = 0

    # Mensaje final y verificación de aprobación
    if prom < 4:
        print("Su promedio es", prom, "\nUsted ha reprobado.")
        reprobado += 1
    else:
        print("Su promedio es", prom, "\nUsted ha aprobado.")
        aprobado += 1





