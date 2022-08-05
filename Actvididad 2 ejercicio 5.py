# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 21:16:46 2022

@author: sebas
"""

class Circulo:
    print("Ingrese el radio del circulo:\n")
    r=float(input())
    pi=3.1416
    a=pi*(r*r)
    p=2*r*pi
    
    def __init__(self,radio,area):
                self.radio = radio
                self.area = area
                
                def find_perimetro(self):
                    return self.perimetro 
                
                def find_area(self):
                    return self.area 
                
my_circulo = Circulo()

perimetro = my_circulo.find_perimetro()
print(perimetro)
area = my_circulo.find_area()
print(area)
    
 
