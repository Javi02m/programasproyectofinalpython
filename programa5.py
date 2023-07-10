def calcu():
    i1= input("escriba el valor de la AB: ")
    i2= input("escriba el valor de la BC: ")
    i3= input("escriba el valor de la CD: ")
    i4= input("escriba el valor de la DA: ")

    AB = float(i1)
    BC = float(i2)
    CD = float(i3)
    DA = float(i4)

    P= (AB + BC + CD + DA)/2
    area = round(P, 2)
    
    print("el area del triangulo es de:",area)

calcu()