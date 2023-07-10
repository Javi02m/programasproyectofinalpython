print("programa39")
def calcular_area_triangulo(bas,aalt):
    A = (bas * aalt)/2
    return A

bas= float(input("escriba la base del triangulo:"))
aalt= float(input("escriba la altura del triangulo:"))

x =calcular_area_triangulo (bas,aalt)

print(x)