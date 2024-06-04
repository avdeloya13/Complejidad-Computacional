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


def columnas():
#Funcion que cuenta la cantidad de reinas que se encuentran en cada fila en la configuracion inicial.
# Debido a que las reinas no pueden ir en una misma fila, a cada reina le corresponde una fila que se le asocia.

	#La configuración del tablero se describe con el vector R.
	vector_R = []

	for fila in tablero:
    	 if '1' in fila:
    		 apariciones = [i for i, x in enumerate(fila) if x == '1']


def diagonales():
#Siendo que a cada reina se le asigna una fila y una columna que no comparte con otra en la funcion anterior, 
# no existen colisiones entre reinas por filas o columnas; entonces debe analizarse la configuración para las diagonales.

	return 0

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

	columnas()

main()