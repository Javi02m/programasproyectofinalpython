print("programa20")

def calcular_salario_neto():
    salario_bruto = float(input("Ingrese el salario bruto del empleado: "))

    
    seguro_social = salario_bruto * 0.08
    seguro_educativo = salario_bruto * 0.02
    impuestos = salario_bruto * 0.15
    prestamo = 100

    
    salario_neto = salario_bruto - seguro_social - seguro_educativo - impuestos - prestamo

    print("El salario neto a pagar es:", salario_neto)


calcular_salario_neto()