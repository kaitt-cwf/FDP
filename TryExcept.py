total = 0
cant = 0
a = 0

while a != 4:
    try:
        print("""
1.- Radio stereo Sony   $70.000
2.- LGTV 55 pulgadas    $500.000
3.- Playstation 5       $580.000
4.- Salir
                """)
        a = int(input("Ingrese una opción: "))
        print("")

        match a:
            case 1:
                total += int(70000*1.19)
                cant += 1
                print(f"El total acumulado es de {total} en un total de {cant} articulos.")
            case 2:
                total += int(500000*1.19)
                cant += 1
                print(f"El total acumulado es de {total} en un total de {cant} articulos.")
                
            case 3:
                total += int(580000*1.19)
                cant += 1
                print(f"El total acumulado es de {total} en un total de {cant} articulos.")
            case 4:
                print(f"El total a pagar es de {total} en un total de {cant} articulos.")
                print("Saliendo del sistema.")
            
            
    except:
        print("Debe ingresar solo numeros enteros")    
    



