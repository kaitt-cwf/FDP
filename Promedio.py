
suma_notas = 0

cant = int(input("¿Cuantas notas quiere ingresar? \n"))

for a in range(cant):
    nota = float(input("Ingrese su nota: "))
    suma_notas = suma_notas + nota

print("Su promedio es", suma_notas/cant)
