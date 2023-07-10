print("programa 7.programa  que calcula el trapesio de un triangulo\n")
def tra():
    i1= input("escriba el valor de largo: ")
    i2= input("escriba el valor de ancho: ")
    i3= input("escriba el valor de la altura: ")

    largo = float(i1)
    ancho = float(i2)
    altura = float(i3)

    vol = largo* ancho * altura

    vplR = round(vol, 4)

    print(" el volumen de umn prisma rectangular",vplR)
tra()