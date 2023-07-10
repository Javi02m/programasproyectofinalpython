print("Programa14. \n Programa para calcular el costo total de compra de combustible \n")
def compra_combustible():

    Litro = float(input("Valor de cantidad de litros: "))

    print ("El costo total es:", round (((0.98* Litro) * 1.07),2))

compra_combustible()