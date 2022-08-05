# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 14:40:09 2022

@author: Johao
"""

class Punto:
    def __init__ (self, X, Y):
        self._X = X
        self._Y = Y
        

My_Coordenada = Punto(2,7)

print("Ubicacion en X:")
print(My_Coordenada._X)

print("Ubicacion en Y:")
print(My_Coordenada._Y)