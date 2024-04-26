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


 

def main():
#Funcion main para mandar a llamar todo, ordenado.

    print('EJEMPLAR DE ENTRADA')
    print('Conjunto: ' + conjunto + 'Valor de la suma: ' + t)


main()

