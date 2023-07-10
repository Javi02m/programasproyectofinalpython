print("programa28")
def calificaciones():    
    calificacion = float(input("escriba la calificacion:"))

    if calificacion > 90 and calificacion <100:
    
        return "tu calificicacion es A"

    if calificacion > 80 and calificacion <89:
    
        return "tu calificicacion es B"

    if calificacion > 70 and calificacion <79:
        return "tu calificicacion es C"

    if calificacion > 60 and calificacion <69:
        return "tu calificicacion es D"
   
    if  calificacion < 60:
        return "tu calificicacion es F"
C = calificaciones()
print(C)