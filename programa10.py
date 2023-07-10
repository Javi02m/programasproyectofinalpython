print("Programa10.\n converion de unidadades\n")
def conversion():

    a1=input("Ingresa la cantidad de metros que quiere convertir:")

    metros = float (a1)

    pies = metros * 3.281
    pulgadas = metros * 39.87

    print("el resultado de metros a pies es de:", round (pies,1))
    print("el resultado de metros a pulgadas es de:", round (pulgadas,1))
conversion()