def ar():
    i1= input("escriba el valor de la 1: ")
    i2= input("escriba el valor de la 2: ")
    i3= input("escriba el valor de la altura: ")

    base1 = float(i1)
    base2 = float(i2)
    altura = float(i3)

    A = ((base1 + base2)*altura)/2
    AR = round( A,2)

    print(" El area de un trapecio es:",AR)

ar()
