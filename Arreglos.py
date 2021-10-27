#Arreglos.
#Elaborado por Osorio Llerenas Zair.
#Martes 26 de octubre de 2021.
import math
interfaz = """
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
Ingresa 1 para el capturar los valores.
Ingresa 2 para el ordenar los valores.
Ingresa 3 para el imprimir los valores originales.
Ingresa 4 para imprimir los valores ordenados.
Ingresa 0 para salir del programa.

°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°
"""
valores = []
valores_ordenados=[]
print (interfaz)
opcion = int(input())
#Ciclo repetitivo del menú
while opcion !=0:
    #Instalo una estrucutra múltiple, para que el usuario pueda elegir libremente.
    if opcion == 1:
        #Defino la longitud del arreglo mediante la variable de valor entero TAMAÑO.
        print ("¿Cuántos valores desea ingresar?")
        tamaño = int(input())
        #Ingreso de valores mediante un blucle for.
        for i in range(tamaño):
            print("Ingrese el valor número %d: " %(i+1), end="")
            valores.append (input())
        print ("")
        print ("Tus valores han sido capturados")
        print ("")
    elif opcion == 2:
        if valores:
            valores_ordenados = sorted(valores)
            print ("")
            print ("Los valores han sido ordenados")
            print ("")
        else:
            print ("")
            print ("No hay valores que pueda ordenar")
            print ("")
    elif opcion == 3:
        if valores:
            print ("")
            print ("Tus valores originales son los siguientes \n:", valores)
            print ("")
        else:
            print ("")
            print ("No hay valores que pueda mostrar")
            print ("")
    elif opcion == 4:
        if valores_ordenados:
            print ("")
            print ("Tus valores ordenados son los siguientes \n:", valores_ordenados)
            print ("")
        else:
            print ("")
            print ("Tus valores aun no han sido ordenados")
            print ("")
    elif opcion == 5:
        print("¿Desea salir del programa?")
        print ("Sí: Presióne 1")
        print("No: Presione 2")
        salir=int(input())
        if salir <= 1:
            print("El programa está finalizandose")
        #Evita que el ciclo while sea infinito.
            break
#Evita que el usuario ingrese respuestas no apropiadas.
    else:
        print("Esa opción no es valida")
    print (interfaz)
    opcion = int(input())

print("Saliendo del programa.")
