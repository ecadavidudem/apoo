#Punto 1 'Imprima Hola Mundo'
def hola():
    print("")
    print("Hola Mundo :D")
    print("")

hola()

#punto 11 ' Calcular la potencia de un número '
def potencia():
    print("Calculo de potencia")
    num = int(input("Ingrese el numero y le digo..."))
    potencia = int(input("Ingrese el valor de la potencia..."))
    resultado = num**potencia
    
    print("Resultado: ", resultado)
print("---------------------------------------")
potencia()