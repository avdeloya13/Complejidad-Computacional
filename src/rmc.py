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
num_ar = 0

#Leyendo el archivo a partir de la linea 3
for linea in archivo:
    aristas.append(linea.strip('\n'))
    num_ar += 1 #y va eliminando los \n


def aristas_y_vertices():
#ESPECIFICACIONES, revisamos que se cumpla las restricciones que pide la practica.

    especificaciones = False

    #Para almacenar la cantidad de vertices
    #Como la practica pide el formato de los vertices,
    #en la primer linea del .txt la cantidad de vertices es la cantidad de comas + 1
    num_vr = 1

    #Para eliminar espacios, simbolos *
    for i in vertices:

        if i == ',':
            num_vr += 1

    #Para las especificaciones para los vertices y aristas
    if 10 <= num_vr and num_vr <= 20 and num_ar > (2 * num_vr):
        especificaciones = True
    else:
        especificaciones = False

    return especificaciones


def trayectoria():
#FASE ADIVINADORA.
#Revisamos una a una las aristas de la grafica G, y por medio de la variable nd_choice que va
#a arrojar un valor aleatorio entre 0 y 1 es que vamos a decidir si incluir o no a la arista en la trayectoria.
#Si es 1 la incluye en la trayectoria y si es 0 no.

    trayect = []

    for i in aristas:

        nd_choice = random.randint(0,1)

        if nd_choice == 1:
            trayect.append(i)
    
    return trayect


def main(formula):
#Funcion main para mandar a llamar todo, ordenado.

    esp = aristas_y_vertices()

    if esp == True:
        print('wuu')

    else: 
        print('Grafica invalida')

print(str(vertices))
print(str(k))
print(aristas)
print(num_ar)
print(trayectoria())