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

#Almacenamos las aristas en una cadena
aristas = ''

#Para almacenar el numero de aristas
num_ar = 0

#Leyendo el archivo a partir de la linea 3
for linea in archivo:
    aristas += linea.strip('\n').replace(',', '') #va eliminando los \n y reemplazando las , por espacios
    num_ar += 1 


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
#FASE ADIVINADORA, regresa una trayectoria como propuesta a solucion del problema.
#Revisamos una a una las aristas de la grafica G, y por medio de la variable nd_choice que va
#a arrojar un valor aleatorio entre 0 y 1 es que vamos a decidir si incluir o no a la arista en la trayectoria.
#Si es 1 la incluye en la trayectoria y si es 0 no.

    trayect = []

    #Seleccionamos las aristas para la trayectoria
    for i in aristas:
        #Para que la seleccion sea aleatoria
        nd_choice = random.randint(0,1)
        #Agregamos el elemento a la trayectoria
        if nd_choice == 1:
            trayect.append(i)
    
    return trayect


def arreglo(trayectoria):
#FASE VERIFICADORA, compara los vertices de la trayectoria y verifica que la distancia de la trayectoria sea menor que k.

#La logica para la fase verificadora es la siguiente, tenemos una trayectoria que nos dio la fase adivinadora
#por ejemplo '5,1', '1,2', '2,6' que en el codigo la tendriamos como: trayectoria = ['5','1','1','2','2','6'] 
#En general lo que queremos es comparar el segundo y tercer elemento de la lista, de ahi seguir con el cuarto y quinto
#y asi sucesivamente. Por lo que el primer elemento no lo vamos a ocupar para esta comparacion y tampoco el ultimo, asi que
#los eliminamos de la lista para facilitar la comparacion. 

#Si al comparar dos vertices resultan ser iguales, contamos esas dos aristas y por eso a distancia se le va sumando de dos en dos.
#Una vez que se hizo la comparacion que ha resultado exitosa, eliminamos esos vertices de la lista y comparamos los que siguen.
#Vamos comparando y eliminando de dos en dos, ese es el motivo de la condicion en el while.

#Si la comparacion no resulta ser exitosa entonces salimos del while.

#Ahora, en el aspecto de la distancia, nos piden que la distancia de la uv-trayectoria sea el numero de vertices sin contar u pero si v.
#Como eliminamos v de la lista trayectoria para facilitar el conteo, jamas va a contarla por lo que inicializamos a la variable distancia = 1

#Como puede pasar que nuestra primera comparacion no sea exitosa, distancia va a ser 1 entonces ese es el porque de esa parte en la condicion del if

    #Se elimina el primer y el ultimo vector de la trayectoria
    trayectoria.remove(trayectoria[0])
    trayectoria.pop()

    #Para contar la distancia
    distancia = 1

    #El ciclo while para verificar la trayectoria
    while len(trayectoria) >= 2:
 
        #Comparacion entre vectores
        if trayectoria[0] == trayectoria[1]:
            #La eliminacion de los elementos que comparamos
            del trayectoria[0]
            del trayectoria[0]
            #Aumenta la distancia si la comparacion es exitosa
            distancia += 2

        else:
            #Si no es exitosa la comparacion no tiene caso seguir y nos salimos del while
            break

    #Verifica la distancia una vez terminada la ejecucion del while
    if distancia < int(k) and distancia != 1:
        return True     
    else: 
        return False
 

def main():
#Funcion main para mandar a llamar todo, ordenado.

    esp = aristas_y_vertices()

    if esp == True:
        print('Buscamos una uv-trayectoria de distancia menor a : ' + k)
        print('Fase Adivinadora')
        t = trayectoria()
        print(t)

        print('\nFase Verificadora')
        print(arreglo(t))
    else: 
        print('Grafica invalida')


#Ejemplo de una trayectoria que devuelve False en la fase verificadora
f = ['8','9','7','8','6','7','7','4','5','3','10','9','3','6','1','2']
#print(arreglo(f))

#Ejemplo de una trayectoria que devuelve True en la fase verificadora
v = ['5','1','1','2','2','6']
#print(arreglo(v))

main()

