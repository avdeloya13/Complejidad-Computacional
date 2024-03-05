import sys
import random

"""
Algoritmos No Deterministicos
Ruta Mas Corta
Author: Ana Valeria Deloya Andrade
"""
#PARA LA LECTURA DEL ARCHIVO:

archivo = sys.argv[1]
#Abrimos el archivo que contiene la grafica
archivo = open(archivo)

#Almacena la linea 1, que contiene los vertices
vertices = archivo.readline()

#Almacena la linea 2, que contiene el valor de k
k = archivo.readline()

#Almacenamos las aristas en una lista
aristas = []
#Para almacenar el numero de aristas
num = 0

#Leyendo el archivo a partir de la linea 3
for linea in archivo:
    aristas.append(linea.strip('\n'))
    num += 1 #y va eliminando los \n


def aristas_y_vertices():
#ESPECIFICACIONES, revisamos que se cumpla las restricciones que pide la practica.

    return 0

def trayectoria():
#FASE ADIVINADORA.
#Revisamos una a una las aristas de la grafica G, y por medio de la variable nd_choice que va
#a arrojar un valor aleatorio entre 0 y 1 es que vamos a decidir si incluir o no a la arista en la trayectoria.
#Si es 1 la incluye en la trayectoria y si es 0 no.

    nd_choice = random.randint(0,1)
    trayect = []

    for i in range(len(aristas)):
        
        if nd_choice == 1:
            trayect.append(i)
    
    return trayect

print(str(vertices))
print(str(k))
print(aristas)
print(num)