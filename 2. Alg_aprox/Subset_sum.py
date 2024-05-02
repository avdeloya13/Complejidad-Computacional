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
t = int(archivo.readline())

#Almacena la linea 2, que contiene el valor de epsilon
epsilon = float(archivo.readline())

#Almacena la linea 3, que contiene el conjunto
conjunto = []

for linea in archivo:
    #Utilizamos extend() para agregar elementos a la lista conjunto, pues utilizando append() se imprime una lista de la lista
    conjunto.extend([int(elem) for elem in linea.split(',')])  


def verificacion():
#Funcion que verifica que epsilon se encuentre dentro de los parametros establecidos
# con 0 < epsilon < 1
    if 0 < epsilon and epsilon < 1:
        return True

    return False


# ----------- Pseudocodigo del libro --------------
#TRIM (L,δ)
#1 let m be the length of L
#2 L' = (y1)
#3 last = y1
#4 for i = 2 to m
#5     if yi > last*(1 + δ) 		 // yi ≥ last porque L está ordenada
#6         añadir yi al final de L'
#7         last = yi
#8 return L'


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


#def MERGE_LISTS(lista1, lista2):
##Devuelve una lista ordenada, siendo esta la fusión de sus dos listas de entrada ordenadas,
## con valores duplicados eliminados.
#
##El pseudocodigo de esta funcion fue omitido en el libro.
#
#    l1 = len(lista1)
#    l2 = len(lista2)
#    
#    i = 0
#    j = 0
#
#    if l1 >= l2:
#
#        for i in range(1,l1):
#
#            if lista1[i] == lista2[j]:
#                i += 1
#                j += 1
#
#            if lista1[i] > lista2[j]:
#                lista1.insert(i,lista2[j])
#                j += 1
#                i += 1
#            else:
#                i += 1
#        
#        return lista1
#
#
#    if l1 < l2:
#
#        for i in range(1,l2):
#
#            if lista2[i] == lista1[j]:
#                i += 1
#                j += 1
#
#            if lista2[i] > lista1[j]:
#                lista2.insert(j,lista1[i])
#                i += 1
#                j += 1
#            else:
#                j += 1
#
#        return lista2

def MERGE_LISTS(L1, L2):

    merged_list = []
    i = 0
    j = 0

    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged_list.append(L1[i])
            i += 1
        elif L1[i] > L2[j]:
            merged_list.append(L2[j])
            j += 1
        else:
            merged_list.append(L1[i])
            i += 1
            j += 1
    while i < len(L1):
        merged_list.append(L1[i])
        i += 1
    while j < len(L2):
        merged_list.append(L2[j])
        j += 1
    return merged_list


# ----------- Pseudocodigo del libro --------------
#APPROX-SUBSET-SUM (S,t,ε)
#1 n = |S|
#2 L0 = (0)
#3 for i = 1 to n
#4 	Li = MERGE-LISTS(Li-1; Li-1 + xi)
#5 	Li = TRIM(Li, ε/2n)
#6 	remueve de Li cada elemento mayor que t
#7 sea z* el valor mas grande de Ln
#8 return z*


def APPROX_SUBSET_SUM(conjunto, t, epsilon):
#Algoritmo de aproximacion en tiempo polinomial para el problema subset sum.
#Devuelve un valor z cuyo valor esta dentro de un factor de 1 + ε de la solucion optima.

    n = len(conjunto)
    L = [[0]]  
    i = 1

    for i in range(1, n):
        Li = MERGE_LISTS(L[i-1], [elem + conjunto[i] for elem in L[i - 1]])
        Li = TRIM(Li, epsilon/(2*n))
        
        #Remueve de Li cada elemento mayor que t
        Li = [elem for elem in Li if elem <= t] 
        L.append(Li)
    
    #Para obtener z, que es el valor mas grande de Ln
    Ln = L[-1] #Como L es una lista de listas, obtenemos la ultima lista con L[-1] y esa es nuestra Ln
    z = max(Ln)

    return z


def main():
#Funcion main para mandar a llamar todo, ordenado.

    verif = verificacion()

    if verif == True:
        print('-------------------------')
        print('EJEMPLAR DE ENTRADA')

        print('Conjunto: ')
        print(conjunto)

        print('Valor de la suma: ')
        print(t) 

        print('Epsilon: ')
        print(epsilon)
        print('-------------------------')
        print('El Algoritmo regresa: ')
        AA = APPROX_SUBSET_SUM(conjunto, t, epsilon)
        print(AA)
        print('-------------------------')

    else:
        print('EJEMPLAR DE INTRADA INVALIDO')

main()


#Esta parte fue para probar como hacer en python lo que se nos explica en el libro,
# sumar un entero x a una lista de enteros. Si L = (1, 2, 3, 5, 9), entonces L + 2 = (3, 4, 5, 7, 11)
#L = [1, 2, 3, 5, 9]
#print([elem + 2 for elem in L])
#Esto es utilizado para la funcion APPROX_SUBSET_SUM, linea AGREGAR LINEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

#L1 = [1, 2, 3, 5, 7, 9, 12, 13, 22, 67]
#L2 = [2, 3, 4, 6, 8, 10,11, 14, 17, 19]
#print(MERGE_LISTS(L1,L2))

