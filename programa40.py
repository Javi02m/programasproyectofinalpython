print("programa40")
def programa_queresuelve_la_regla_de_tres_simple(c1,c2,c3):
    D = (c2 * c3/c1)
    return D


c1 = float (input("escriba el valor de a:"))
c2 = float(input("escriba el valor de b:"))
c3 = float (input("escriba el valor de c:"))

pr= programa_queresuelve_la_regla_de_tres_simple (c1,c2,c3)

print(pr)