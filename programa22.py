print("programa22")
def nivel_temperatura():

    temperatura= float(input("escriba la temperatura:"))
    if temperatura < 20:
        if temperatura < 10:
            return "nivel azul"
        else:
            return"nivel verde"
        
    else:
        if temperatura < 30:
            return"nivel naranja"
        else:
            return"nivel rojo"
N = nivel_temperatura()
print(N)
    