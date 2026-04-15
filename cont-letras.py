# contador de vocal y consonante
vocal = 0
consonante = 0

# se pide el nombre al usuario
nombre = input("Ingrese su nombre ")

# clasificacion entre vocal y consonante, luego se suman donde corresponde
for i in nombre:

    if i in "aAeEiIoOuU":
        vocal += 1
    else:
        consonante += 1

# mensaje final
print("La cantidad de vocales es", vocal)
print("La cantidad de consonantes es", consonante)