import math
#valor que ingresara el usuario
r = float(input("Ingrese el radio del circulo: "))
#area del circulo
a = math.pi * (r*r)
print("El area del circulo con radio",r,"Es: ",a)
#perimetro del ciculo
p = 2 * r * math.pi
print("El perimetro del circulo con radio",r,"Es: ",p)
