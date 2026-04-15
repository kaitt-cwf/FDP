# Se define donde se suman las notas 
suma_notas = 0

# Se le pide al usuario la cantidad de notas que quiere ingresar
cant = int(input("¿Cuantas notas quiere ingresar? \n"))


for a in range(cant):
    nota = float(input("Ingrese su nota: "))
    suma_notas = suma_notas + nota

prom = suma_notas/cant

print("Su promedio es", prom)

if prom < 4:
    print("Usted ha reprobado.")
else:
    print("Usted ha aprobado.")

