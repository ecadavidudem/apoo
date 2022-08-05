class Circulo:

    def __init__(self,radio):
        self.radio = radio

    def calcular(self):
        PI = 3.1416
        self.area=PI*(radio*radio)
        self.perimetro=2*radio*PI
                
    def get_perimetro(self):
        return self.perimetro 
                
    def get_area(self):
        return self.area 

print("Ingrese el radio del circulo:\n")
radio=float(input())


my_circulo = Circulo(radio)
my_circulo.calcular()
perimetro = my_circulo.get_perimetro()
print(perimetro)
area = my_circulo.get_area()
print(area)
