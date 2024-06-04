import sys

"""
Meta Heuristicas
N-Reinas
Author: Ana Valeria Deloya Andrade
"""
#PARA LA LECTURA DEL ARCHIVO:

archivo = sys.argv[1]
#Abrimos el archivo que contiene al ejemplar
archivo = open('Ejemplares/' + archivo)

#Almacena la linea 1, que contiene el costo
costo = archivo.readline()

#Para almacenar el tablero/configuracion inicial
tablero = []


#Leyendo la configuracion inicial
for linea in archivo:
	tablero.append(linea.strip('\n')) #va eliminando los \n


def main():
#Funcion main para mandar a llamar todo, ordenado.

	print('EJEMPLAR DE ENTRADA')
	print('-------------------------')

	print('CONFIGURACION INICIAL: ')

	for i in tablero:
    	 print(i)

	print('COSTO:') #Nuestro costo van a ser las colisiones
	print(costo)

	print('SALIDA')
	print('-------------------------')

main()
