def z ():
    a = 10
    b = 0
    aux = 0
    aux = a
    a = b
    b = aux
    return a,b,aux
R = z ()
print(R)