"""EXERCISE 10"""
a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))
prom = (a+b+c)/3
print(prom)

"""EXERCISE 20"""
def contar(cadena):
    contador = 0

    while cadena[contador:]:
        contador += 1

    return contador

frase = str(input("Ingrese una frase: "))
print(contar(frase))

