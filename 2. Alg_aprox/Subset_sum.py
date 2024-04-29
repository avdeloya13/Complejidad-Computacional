import sys
import random

"""
Algoritmos De Aproximación
Subset Sum
Author: Ana Valeria Deloya Andrade
"""
#PARA LA LECTURA DEL ARCHIVO:

archivo = sys.argv[1]
#Abrimos el archivo que contiene la grafica
archivo = open(archivo)

#Almacena la linea 1, que contiene el conjunto
conjunto = archivo.readline()

#Almacena la linea 2, que contiene el valor de la suma
t = archivo.readline()

#Almacena la linea 3, que contiene el valor de epsilon
epsilon = archivo.readline()

def verificacion():
#Funcion que verifica que epsilon se encuentre dentro de los parametros establecidos
# con 0 < epsilon < 1
    if 0 < float(epsilon) and float(epsilon) < 1:
        return True

    return False


def main():
#Funcion main para mandar a llamar todo, ordenado.

    verif = verificacion()

    if verif == True:
        print('EJEMPLAR DE ENTRADA')
        print('Conjunto: ' + conjunto + 'Valor de la suma: ' + t + 'Epsilon: ' + epsilon)
    else:
        print('EJEMPLAR DE INTRADA INVALIDO')


main()

