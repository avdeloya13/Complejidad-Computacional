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
    conjunto.extend([int(elem) for elem in linea.split(',')]) #Convierte a int los elementos del conjunto dado en el .txt y los agrega a la lista


def VERIFICA():
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
    ultimo = conjunto[0]
    #i = 2

    for i in range(1,m):
        if conjunto[i] > ultimo*(1+delta):
            conjunto_recortado.append(conjunto[i]) #Agregamos elemento a conjunto_recortado
            ultimo = conjunto[i] #Establecemos nuevo valor para ultimo

    return conjunto_recortado


#----------- El pseudocodigo de esta funcion fue omitido en el libro --------------

def MERGE_LISTS(lista1, lista2):
#Devuelve una lista ordenada, siendo esta la fusión de sus dos listas de entrada ordenadas,
# con valores duplicados eliminados.

    listas_fusionadas = []

    l = len(listas_fusionadas)
    l2 = len(lista2)

    #Comenzamos por agregar los elementos de la primer lista a listas_fusionadas
    for i in lista1:
        listas_fusionadas.append(i) #Agregamos el elemento i de lista1

    #Ahora los elementos de la segunda lista a listas_fusionadas
    lf = 0 
    for j in lista2:
        while lf < l and listas_fusionadas[lf] < j:
            lf += 1

        listas_fusionadas.insert(lf, j) #Agregamos el elemento j de lista2
        lf += 1

    #Eliminamos los elementos duplicados, no_dup no tiene elementos duplicados pero usar set() lo hizo conjunto
    no_dup = set(listas_fusionadas)
    
    return list(no_dup) #Convertimos de nuevo a lista y regresamos no_dup


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
    Listas = [[0]]  #Lista de listas, iniciando con L0
    #i = 1

    for i in range(1, n):
        Li = MERGE_LISTS(Listas[i-1], [elem + conjunto[i] for elem in Listas[i - 1]])
        Li = TRIM(Li, epsilon/(2*n))
        
        Li = [elem for elem in Li if elem <= t] #Para no tener en Li elementos mayores que t
        Listas.append(Li) #Se agrega Li a la lista de listas Listas
    
    Ln = Listas[-1] #Como "Listas" es una lista de listas, obtenemos la ultima lista con Listas[-1] y esa es nuestra Ln
    print(Ln)  #Para mostrar en terminal el subconjunto de numeros resultante

    z = Ln[-1] #Obtenemos z, que es el valor mas grande de Ln
    return z  


def main():
#Funcion main para mandar a llamar todo, ordenado.

    verif = VERIFICA()

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
        print('EL ALGORITMO REGRESA ')
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
#Esto es utilizado para la funcion APPROX_SUBSET_SUM, linea 115


#Para probar la funcion MERGE_LISTS
#L1 = [1, 2, 3, 5, 7, 9, 12, 13, 22, 67, 68,70]
#L2 = [2, 3, 4, 6, 8, 10,11, 14, 17, 19,69]
#print(MERGE_LISTS(L1,L2))

#L3 = [1, 2, 3, 4, 5]
#L4 = [4, 5, 6, 7, 8]
#print(MERGE_LISTS(L3,L4))
