a = 1
suma = 0

while a != 0:
    try:
        a = int(input("Ingrese el número a sumar : "))
        suma += a
    except:
        print("Solo ingrese números enteros\n")

print(suma)