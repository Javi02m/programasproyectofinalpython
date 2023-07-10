print("programa38")
def sumar_numeros_pares(numero):   
    suma = 0
  
    for x in range(2,numero+1,2):
        suma +=x
    
    return suma
   
numero = 10
r = sumar_numeros_pares(numero)

print(r)
      
     