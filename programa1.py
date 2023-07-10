def I_V():
    A = 7
    B = 0
    C = 0
    B = A
    C = B
    A = A
    return(A,B,C)
A,B,C = I_V()
print(A,B,C)