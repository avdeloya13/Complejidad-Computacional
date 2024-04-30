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


def MERGE_LISTS(lista1, lista2):
#Devuelve una lista ordenada, siendo esta la fusión de sus dos listas de entrada ordenadas,
# con valores duplicados eliminados.

#El pseudocodigo de esta funcion fue omitido en el libro.

    l1 = len(lista1)
    l2 = len(lista2)

    fusion = []

    i = 0
    j = 0

    while i < l1 and j < l2:
        
        if lista1[i] < lista2[j]:
            fusion.append(lista1[i])
            i += 1

        elif lista2[j] < lista1[i]:
            fusion.append(lista2[j])
            j += 1
        
        elif lista1[i] == lista2[j]:
            fusion.append(lista1[i])
            i += 1
            j += 1

    while i < l1:
        fusion.append(lista1[i])
        i += 1

    while j < l2:
        fusion.append(lista2[j])
        j += 1

    return fusion


#APPROX-SUBSET-SUM (S,t,ε)
#1 n = |S|
#2 L0 = (0)
#3 for i = 1 to n
#4 	Li = MERGE-LISTS(Li-1; Li-1 + xi)
#5 	Li = TRIM(Li, ε/2n)
#6 	remove from Li every element that is greater than t
#7 let z* be the largest value in Ln
#8 return z*

#def APPROX_SUBSET_SUM(conjunto, t, epsilon):
##
#
#    return 0


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

L = [1, 2, 3, 5, 9]
print([elem + 2 for elem in L])

L1 = [1, 3, 5, 7, 9, 12, 13,22,67]
L2 = [2, 4, 3,6, 8, 10, 11,14,17,19,78]
print(MERGE_LISTS(L1,L2))
