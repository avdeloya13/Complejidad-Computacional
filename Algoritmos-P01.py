import sys
import random

"""
Complejidad Computacional.
Algoritmos No Deterministicos.
Alumna: Ana Valeria Deloya Andrade
"""

archivo = sys.argv[1]
#Abrimos el archivo que contiene la formula booleana
archivo = open(archivo)

#Leemos el archivo y lo asignamos a una variable formula
formula = archivo.readline()


def asignaValor(formula):
#Fase Adivinadora
#Recorre la formula para asignar un valor a cada variable

    var_x = random.randint(0,1)
    var_y = random.randint(0,1)
    var_z = random.randint(0,1)
    con_valores = ''

    for i in formula:
        if i == 'x':
            con_valores += str(var_x)
        elif i == 'y':
            con_valores += str(var_y)
        elif i == 'z':
            con_valores += str(var_z)
        else:
            con_valores += i 
    
    return con_valores

print(asignaValor(formula))

#def variables_negativas(formula):
#Auxiliar para la fase Verificadora
#Recorre la formula donde cada variable ya tiene un valor asginado,
#pero hay casos en los que podemos tener en nuestra clausula un "-x"
#donde si x es 1, entonces -x es 0, en esta funcion hacemos esa conversion
#    conversion = ''
#
#    for i in formula:
#        if i == -:
#
#            if i+1 == 1:
#                i+1 = 0
#                conversion + i 
#                #conversion + i+1
#            else: 
#                i+1 = 1
#                conversion + i 
#                #conversion + i+1
#
#        else:
#            conversion + i 
#    
#    return conversion




