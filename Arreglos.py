#Arreglos.
#Elaborado por Osorio Llerenas Zair.
#Martes 26 de octubre de 2021.
import math

#Valores string en una variable
interfaz = """
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
Ingresa 1 para el capturar los valores.
Ingresa 2 para el ordenar los valores.
Ingresa 3 para el imprimir los valores originales.
Ingresa 4 para imprimir los valores ordenados.
Ingresa 5 para salir del programa.

°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
"""

valores = [] #Declaración de arreglos
valores_ordenados=[] #Declaración de arreglos


print (interfaz) #Imprime en pantalla los valores string
opcion = int(input())

while opcion != 0: #Permite que los distintos procesos se ejecuten mientras se cumpla la condición

#Instalo una estrucutra múltiple
    if opcion == 1: #Ejecuta el proceso número 3

        print ("¿Cuántos valores desea ingresar?") #Datos de entrada.

        tamaño = int(input()) #Tamaño del arreglo

        for i in range(tamaño):  #Entrada de valores por el usuario.
            print("Ingrese el valor número %d: " %(i+1), end="") #Enumera el número de valores que son ingresados
            valores.append(input()) #Agrega un valor al final de la lista

        print ("") #salto de linea
        print ("Tus valores han sido capturados") #Datos de salida
        print ("") #salto de linea

    elif opcion == 2: #Ejecuta el proceso número 2
        if valores:
            valores_ordenados = sorted(valores)

            print ("") #salto de linea
            print ("Los valores han sido ordenados") #Datos de salida
            print ("-"*30) #salto de linea

        else: #Evita que los usuarios excpetúen el proceso número 1

            print ("") #salto de linea
            print ("No hay valores que pueda ordenar") #Datos de salida
            print ("-"*30) #salto de linea

    elif opcion == 3: #Ejecuta el proceso número 3
        if valores:
            print ("") #salto de linea
            print ("Tus valores originales son los siguientes:  \n", valores) #Datos de salida
            print ("-"*30) #salto de linea

        else: #Evita que los usuarios excpetúen el proceso número 1

            print ("") #salto de linea
            print ("No hay valores que pueda mostrar") #Datos de salida
            print ("-"*30) #salto de linea

    elif opcion == 4: #Ejecuta el proceso número 4
        if valores_ordenados:
            print ("") #salto de linea
            print ("Tus valores ordenados son los siguientes:  \n", valores_ordenados) #Datos de salida
            print ("-"*30) #salto de linea

        else: #Evita que los usuarios excpetúen el proceso número 1 y 2
            print ("") #salto de linea
            print ("Tus valores aun no han sido ordenados") #Datos de salida
            print ("-"*30) #salto de linea

    elif opcion == 5: #Ejecuta el proceso número 5
        print("¿Desea salir del programa?")
        print ("Sí: Presióne 1")
        print("No: Presione 2")
        salir=int(input()) #Dato de entrada
        
        if salir == 1: #Si la condición se cumple permite que programa finalice
            opcion = 0
            print ("-"*30) #salto de linea
            print("El programa está finalizandose") #Datos de salida

            continue #Evita que el ciclo while sea infinito y lo cierra.

    else: #Evita que el usuario ingrese respuestas no apropiadas.
        print("Esa opción no es valida") #Dato de salida

    print (interfaz) #Se reinicia el ciclo while
print("Saliendo del programa.")
