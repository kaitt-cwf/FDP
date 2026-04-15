# Se define donde se suman las notas 
suma_notas = 0

# Se le pide al usuario la cantidad de notas que quiere ingresar
cant = int(input("¿Cuantas notas quiere ingresar? \n"))

# Se pide la nota segun la cantidad ya pedida
for a in range(cant):
    nota = float(input("Ingrese su nota: "))
    suma_notas = suma_notas + nota

# Se calcula el promedio
prom = suma_notas/cant


# Mensaje final y verificación de aprobación
if prom < 4:
    print("Su promedio es", prom, "\nUsted ha reprobado.")
else:
    print("Su promedio es", prom, "\nUsted ha aprobado.")

