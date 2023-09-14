'''5. Búsqueda: Escribe un programa en pseudocódigo que realice una búsqueda de un número dado, en un arreglo. Crea una función modular para llevar a cabo la búsqueda.'''

#Definimos la función para verificar si el número solicitado se encuentra en el arreglo creado
def buscarNumero(arreglo, numero):
    for elemento in arreglo:
        if elemento == numero:
            return True
    return False

#Establecemos el valor inicial para los datos
arreglo = [5, 2, 8, 10, 3]
numeroEncontrado = False

#Pedimos al usuario que ingrese el número que quiere buscar
print("Ingrese el número a buscar:")
numero = int(input())

#Llamamos a la función para que realice su tarea y muestre en pantalla el resultado
numeroEncontrado = buscarNumero(arreglo, numero)
if numeroEncontrado:
    print("El número", numero, "se encuentra en el arreglo.")
else:
    print("Disculpe. El número", numero, "no se encuentra en el arreglo.")