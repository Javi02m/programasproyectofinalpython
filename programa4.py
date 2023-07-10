print("programa que calcula el area de un triangulo\n")
def c__a_t(base,aaltura):
    A = (base * aaltura)/2
    return A

base= float(input("escriba la base del triangulo:"))
aaltura= float(input("escriba la altura del triangulo:"))

x =c__a_t(base,aaltura)

print(x)