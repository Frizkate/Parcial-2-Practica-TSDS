'''6. Calculadora Modular: Crea un programa que permita realizar operaciones matemáticas básicas (suma, resta, multiplicación y división) utilizando funciones modulares para cada operación.'''

#Definimos las funciones para las operaciones
def suma(a, b):
    resultado = a + b
    return resultado
def resta(a, b):
    resultado = a - b
    return resultado
def multiplicacion(a, b):
    resultado = a * b
    return resultado
def division(a, b):
    resultado = a / b
    return resultado

#Establecemos el valor inicial para los datos
a = 0
b = 0
resultadoSuma = 0
resultadoResta = 0
resultadoMultiplicacion = 0
resultadoDivision = 0
opcion = 0

#Pedimos al usuario que ingrese los valores que quiere que sean puestos en una operación
print("Ingrese el primer número:")
a = float(input())
print("Ingrese el segundo número:")
b = float(input())

#Pedimos al usuario que ingrese una opción que determine la operación que quiera llevar a cabo con los valores ingresados previamente
print("Elige una opción:")
print("1. Sumar.")
print("2. Restar.")
print("3. Multiplicar.")
print("4. Dividir.")

#Llamamos a la función correspondiente para que realize la operación solicitada y muestre el resultado en pantalla
opcion = int(input())
if opcion == 1:
    resultadoSuma = suma(a, b)
    print("La suma es:", resultadoSuma)
elif opcion == 2:
    resultadoResta = resta(a, b)
    print("La resta es:", resultadoResta)
elif opcion == 3:
    resultadoMultiplicacion = multiplicacion(a, b)
    print("La multiplicación es:", resultadoMultiplicacion)
elif opcion == 4:
    resultadoDivision = division(a, b)
    print("La división es:", resultadoDivision)
else:
    print("Opción inválida. Intente nuevamente.")