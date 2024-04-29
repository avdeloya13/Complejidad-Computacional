import sys
import random

"""
Algoritmos De Aproximación
Subset Sum
Author: Ana Valeria Deloya Andrade
"""
#PARA LA LECTURA DEL ARCHIVO:

archivo = sys.argv[1]
#Abrimos el archivo que contiene al ejemplar
archivo = open(archivo)

#Almacena la linea 1, que contiene el valor de la suma
t = archivo.readline()

#Almacena la linea 2, que contiene el valor de epsilon
epsilon = archivo.readline()

#Almacena la linea 3, que contiene el conjunto
conjunto = []

for linea in archivo:
    #Utilizamos extend() para agregar elementos a la lista conjunto
    conjunto.extend(linea.split(','))


def verificacion():
#Funcion que verifica que epsilon se encuentre dentro de los parametros establecidos
# con 0 < epsilon < 1
    if 0 < float(epsilon) and float(epsilon) < 1:
        return True

    return False

#El siguiente procedimiento recorta la lista L = (y1,y2,...,ym)
#TRIM (RECORTAR) (L,δ)
# let m be the length of L
# L' = (y1)
# last = y1
# for i = 2 to m
#     if yi > last*(1 + δ) 		 // yi ≥ last porque L está ordenada
#         añadir yi al final de L'
#         last = yi
# return L'

def TRIM(conjunto, delta):
#Dado el conjunto de enteros y un valor para delta, la salida de la funcion es el conjunto recortado y ordenado.

    conjunto_recortado = conjunto[0]
    ultimo = conjunto[0]
    m = len(conjunto)
    i = 2

    for i in m:
        if conjunto[0] > ultimo*(1+delta)
            conjunto_recortado.append(conjunto[i])
            ultimo = conjunto[i]

    return conjunto_recortado


def main():
#Funcion main para mandar a llamar todo, ordenado.

    verif = verificacion()

    if verif == True:
        print('EJEMPLAR DE ENTRADA')
        print('Conjunto: ')
        print(conjunto)
        print('Valor de la suma: ' + t + 'Epsilon: ' + epsilon)
        #print(TRIM(conjunto, 0.05))
    else:
        print('EJEMPLAR DE INTRADA INVALIDO')

main()
