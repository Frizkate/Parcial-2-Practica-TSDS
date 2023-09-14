'''3. Números Primos en un Rango: Escribe un programa en pseudocódigo que encuentre y muestre todos los números primos dentro de un rango dado. Utiliza una función modular para determinar si un número es primo.'''

#Definimos la función para verificar si los números en el rango solicitado son primos
def esPrimo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

#Definimos la función para armar la lista con los números primos hallados en el rango
def numerosPrimosEnRango(inicio, fin):
    numerosPrimos = []
    for numero in range(inicio, fin+1):
        if esPrimo(numero):
            numerosPrimos.append(numero)
    return numerosPrimos

#Establecemos el valor inicial para los datos
inicio = 0
fin = 0

#Pedimos al usuario que ingrese los valores inicial y final para el rango de números de donde quiera que se busquen números primos
print("Ingrese el rango inicial:")
inicio = int(input())
print("Ingrese el rango final:")
fin = int(input())

#Llamamos a la función para que realice su tarea y muestre en pantalla el resultado
numerosPrimos = numerosPrimosEnRango(inicio, fin)
print("Los números primos en el rango", inicio, "a", fin, "son:", numerosPrimos)