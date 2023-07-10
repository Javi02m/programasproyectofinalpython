print("programa 12.programa que calcula el interes a pagar por un prestamo")
def calcular_interes():
    mont_p = float(input("ingrese el monto:"))
    ta_m = float(input("ingrese la tasa mesual:"))
    I = mont_p *(ta_m/100)
    print("el interes a pagar:",I)
calcular_interes()
    
    
