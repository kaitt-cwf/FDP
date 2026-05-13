a = 1

# Pedir al usuario que ingrese el peso, validar y clasificar
while a != 0:
    try:
        peso = int(input("Ingrese el peso en gramos: "))
        if 0 < peso:
            a = 0
        else:
            print("Ingrese solo numeros positivos")
    except ValueError as inter:
        print(inter)
        print("Ingrese solo numeros enteros positivos.")

    if peso <= 500:
        tamaño = "Lata normal"
    elif peso <= 1500:
        tamaño = "Lata mediana"
    else:
        tamaño = "Lata grande"

# Ingresar porcentaje de sodio, validar y clasificar
while a == 0:
    try:
        sodio = int(input("Ingrese el porcentaje de sodio: "))
        if 1 <= sodio <= 100:
            a = 1
        else:
            print("Ingrese solo numeros entre 1 y 100")
    except ValueError as inter:
        print(inter)
        print("Ingrese solo numeros enteros positivos.")
    
    if sodio < 5:
        tipo = "sin refuerzo"
    elif sodio <= 8:
        tipo = "especial"
    else:
        tipo = "acorazada"

# Preguntar donde venderá  y validar
while a != 0:
    try:
        pais = int(input("""Donde venderá el producto:
                         
1.- Nacionalmente
2.- Internacionalmente
                         
"""))
        match pais:
            case 1:
                a = 0
                sticker = "sin sticker sanitario."
            case 2:
                a = 0
                sticker = "con sticker sanitario."
            case _:
                print("Opción invalida.")
    except ValueError as inter:
        print(inter)
        print("Ingrese solo numeros enteros positivos.")
print("")
print(tamaño, tipo, sticker)

