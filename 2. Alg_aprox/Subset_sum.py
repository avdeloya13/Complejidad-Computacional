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

#Del libro
#Recorta una lista L = (y1,y2,...,ym)
#TRIM (L,δ)
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

    m = len(conjunto)
    conjunto_recortado = [conjunto[0]]
    ultimo = int(conjunto[0])
    i = 2

    for i in range(1,m):
        if int(conjunto[i]) > ultimo*(1+delta):
            conjunto_recortado.append(conjunto[i])
            ultimo = int(conjunto[i])

    return conjunto_recortado

#APPROX-SUBSET-SUM (S,t,ε)
#1 n = |S|
#2 L0 = (0)
#3 for i = 1 to n
#4 	Li = MERGE-LISTS(Li-1; Li-1 + xi)
#5 	Li = TRIM(Li, ε/2n)
#6 	remove from Li every element that is greater than t
#7 let z* be the largest value in Ln
#8 return z*


def main():
#Funcion main para mandar a llamar todo, ordenado.

    verif = verificacion()

    if verif == True:
        print('EJEMPLAR DE ENTRADA')
        print('Conjunto: ')
        print(conjunto)
        print('Valor de la suma: ' + t + 'Epsilon: ' + epsilon)
    else:
        print('EJEMPLAR DE INTRADA INVALIDO')

main()

print(TRIM(conjunto, 0.1))


