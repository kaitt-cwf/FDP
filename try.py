a = True

while a == True:
    try:
        pasajes = int(input("Ingrese la cantidad de pasajes a vender: "))
        a = False
    except:
        print("Dato no válido, ingrese un numero entero positivo.")