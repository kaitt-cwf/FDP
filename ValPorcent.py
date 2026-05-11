a = 0

while a == 0:
    porcent = float(input("Ingrese un porcentaje:"))

    if porcent <= 100 and porcent >= 0:
        print("Porcentaje correcto.")
        a += 1
    else:
        a = 0
        print("Porcentaje fuera de rango.")