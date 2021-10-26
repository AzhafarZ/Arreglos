#Arreglos.
#Elaborado por Osorio Llerenas Zair.
#Martes 26 de octubre de 2021.
import math

print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
print ("Ingresa 1 para el capturar los valores.")
print ("Ingresa 2 para el ordenar los valores.")
print ("Ingresa 3 para el imprimir los valores originales.")
print ("Ingresa 4 para imprimir los valores ordenados.")
print ("Ingresa 5 para salir del programa.")
print("")
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°")
opcion = int(input())
while opcion <= 5:
    if opcion == 1:
        #Defino la longitud del arreglo mediante la variable de valor entero TAMAÑO.
        print ("¿Cuántos valores desea ingresar?")
        TAMAÑO = int(input())
        longitud = [0 for i in range(TAMAÑO)]
        #Ingreso de valores mediante un blucle for.
        for i in range(len(longitud)):
            print("Ingrese el valor número %d: " %(i+1), end="")
            longitud[i] = input()
#Termina el blucle while.
print("¿Desea salir del programa?")
print ("Sí: Presióne 1")
print("No: Presione 2")
salir=int(input())
while salir <= 1:
    print("El programa está finalizandose")
