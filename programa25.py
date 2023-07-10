print("programa25")
def produc():
    PP = float(input("Ingrese precio original del producto: "))
    P = float(input("Ingrese el porcentaje de descuento: "))

    P/100
    P = PP * P/100
    PrecioFinal = PP - P

    if PP < 50:
        print("Oferta Especial", PrecioFinal)
    else:
        print("Precio Final", PrecioFinal)
produc()