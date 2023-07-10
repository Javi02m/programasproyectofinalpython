print("Programa16.")
def not_f():
    N1 = float(input("Ingrese el valor de la primera evaluación: "))
    N2 = float(input("Ingrese el valor de la segunda evaluación: "))
    N3 = float(input("Ingrese el valor de la tercera evaluación: "))
    N4 = float(input("Ingrese el valor de la cuarta evaluación: "))
    N5 = float(input("Ingrese el valor de la quinta evaluación: "))

    PE1 = N1 * 0.20
    PE2 = N2 * 0.15
    PE3 = N3 * 0.25
    PE4 = N4 * 0.10
    PE5 = N5 * 0.30
    
    notafinal = PE1 + PE2 + PE3 + PE4 + PE5 / 100

    print("La nota final es:",round(notafinal, 2))
not_f()
