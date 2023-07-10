print("programa 8.programa  que resulve ecuaciones lineales y muestre el resultado\n")
def t(x):
    a = 20-(7*x)
    b = (-7*x) + 2 - (10*x) + 5
    c = (4*x) + 4 + (9*x) + 18
    d = (6*x) - 5-(8*x) + 2
    e = ((5*x) + 78) / 28
    f = (((6*x) - 7) / 4) + (((3*7) - 5)/7)
    R_A = round(a,2)
    R_B = round(b,2)
    R_C = round(c,2)
    R_D = round(d,2)
    R_E = round(e,2)
    R_F = round(f,2)

    return R_A,R_B,R_C,R_D,R_E,R_F 

x1= input("escriba el valor de x: ")

x = int(x1)

R_A,R_B,R_C,R_D,R_E,R_F = t(x)


print ("el resultado de A:",R_A)
print ("el resultado de B:",R_B)
print ("el resultado de C:",R_C)
print ("el resultado de D:",R_D)
print ("el resultado de E:",R_E)
print ("el resultado de F:",R_F)

