class Vehiculo:
    
    def __init__(self,Kilometraje,velocidad_Maxima):
        self.kilometraje = Kilometraje
        self.Velocidad_Maxima = velocidad_Maxima

MiCarro = Vehiculo
MiCarro.kilometraje = 1500
MiCarro.Velocidad_Maxima = "200 Km/h"

print(MiCarro.kilometraje)
print(MiCarro.Velocidad_Maxima)