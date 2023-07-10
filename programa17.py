print("programa17")
def kilogramos():
        kg = float(input("Ingrese el valor en kilogramos: "))
        gramos = kg * 1000
        print("El resultado es:", gramos, "gramos")

def gramos_a_kilogramos():
        gramos = float(input("Ingrese el valor en gramos: "))
        kg = gramos / 1000
        print("El resultado es:", kg, "kilogramos")
        
def metros_a_centrimetro():
        metros = float(input("Ingrese el valor en metros: "))
        centimetros = metros * 100
        print("El resultado es:", centimetros, "centímetros")
        
def centrimetro_ametros():
        centimetros = float(input("Ingrese el valor en centímetros: "))
        metros = centimetros / 100
        print("El resultado es:", metros, "metros")
kilogramos()
gramos_a_kilogramos()
metros_a_centrimetro()
centrimetro_ametros()
