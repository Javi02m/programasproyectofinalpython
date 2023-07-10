print("Programa15. \n Programa que de el total de la compra con impuesto \n")
def impuesto(): 
    A1 = input("Escribir valor del articulo 1: ")
    A2 = input("Escribir valor del articulo 2: ")
    A3 = input("Escribir valor del articulo 3: ")

    Art1= float(A1)
    Art2 = float(A2)
    Art3 = float(A3)

    P_A = Art1 + Art2 + Art3
    Impuesto = P_A * 1.07

    print("total de la compra con el impuesto es de: ", round(Impuesto, 2))
    
impuesto()