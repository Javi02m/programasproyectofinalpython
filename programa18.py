print("programa18")
def calcular_interes_compuesto():
    capital = float(input("Ingrese el capital inicial: "))
    tasa_interes = float(input("Ingrese la tasa de interés anual (%): "))
    periodo = int(input("Ingrese el período de inversión (en años): "))

    tasa_interes_decimal = tasa_interes / 100
    monto_final = capital * (1 + tasa_interes_decimal) ** periodo

    print("El monto final de la inversión es:", monto_final)


calcular_interes_compuesto()