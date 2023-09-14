'''2. Conversión de Temperatura: Crea un programa en pseudocódigo que permita convertir entre Celsius y Fahrenheit. Crea dos funciones modulares: una para convertir de Celsius a Fahrenheit y otra para convertir de Fahrenheit a Celsius.'''

#Definimos las funciones para las operaciones
def Celsius_a_Fahrenheit(Celsius):
    Fahrenheit = (Celsius * 9 // 5) + 32
    return Fahrenheit
def Fahrenheit_a_Celsius(Fahrenheit):
    Celsius = (Fahrenheit - 32) * 5 // 9
    return Celsius

#Establecemos el valor inicial para los datos
Celsius = 0
Fahrenheit = 0
opcion = 0

#Pedimos al usuario que ingrese una opción que determine la operación que quiera llevar a cabo con el valor ingresado a continuación
print("Elige una opción:")
print("1. Convertir Celsius a Fahrenheit.")
print("2. Convertir Fahrenheit a Celsius.")

#Llamamos a la función correspondiente para que realice su tarea y muestre en pantalla el resultado
opcion = int(input())
if opcion == 1:
    print("Ingrese la temperatura en Celsius:")
    Celsius = float(input())
    Fahrenheit = Celsius_a_Fahrenheit(Celsius)
    print("La temperatura en Fahrenheit es:", Fahrenheit)
elif opcion == 2:
    print("Ingrese la temperatura en Fahrenheit:")
    Fahrenheit = float(input())
    Celsius = Fahrenheit_a_Celsius(Fahrenheit)
    print("La temperatura en Celsius es:", Celsius)
else:
    print("Opción inválida. Intente nuevamente.")