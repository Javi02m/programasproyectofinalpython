print("programa que calcula el salario de sus empleados")
def salario():    
    sa = input("valor de salario bruto")
    sab = float(sa)
    ss = sab * 0.8
    se = sab * 0.2
    im = 1.5
    prestamo = 100 
    salarionetodeempleados= sab - ss - se- prestamo

    print(" el salario neto e:", round(ss,))
    print(" el salario neto e:", round(se,))
    print(" el salario neto e:", round(prestamo,))
    print(" el salario neto e:", round(salarionetodeempleados,))
    
salario() 