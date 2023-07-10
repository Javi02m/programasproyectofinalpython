print("Programa26")
def calificacion():
    l1 = float(input("Escriba la longitud del lado 1: "))
    l2 = float(input("Escriba la longitud del lado 2: "))
    l3 = float(input("Escriba la longitud del lado 3: "))

    if l1 == l2 and l2 == l3:
        clf = "Equilátero"
    
    elif l1 == l2 or l1 == l3 or l2 == l3:
        clf = "Isósceles"
    
    else:
        clf = "Escaleno"
    
    print("El triángulo es", clf)   

    print('\nFin del programa')
calificacion()