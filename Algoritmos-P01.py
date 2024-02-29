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


def clausulas_limite(formula):
#Como deben ser de 3 a 10 clausulas, entonces esta funcion va a 
#contar el numero de parentesis que deben ser entre 6 y 20
    parentesis = 0

    for i in formula:
        if i == '(':
            parentesis += 1

        if i == ')':
            parentesis += 1

    if parentesis < 6 or parentesis > 20:
        return False
    else: 
        return True


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


#def variables_negativas(f):
##Auxiliar para la fase Verificadora
##Recorre la formula donde cada variable ya tiene un valor asginado,
##pero hay casos en los que podemos tener en nuestra clausula un "-x"
##donde si x es 1, entonces -x es 0, en esta funcion hacemos esa conversion
#
#    for i in range(len(f)):
#        if f[i] == '-':
#            if f[i+1] == 0:
#                f[i+1] = 1
#            else:
#                f[i+1] = 0
#    
#    return f


def main(formula):
    clausulas = clausulas_limite(formula)

    if clausulas == True:
        print('Fase Adivinadora')
        val = asignaValor(formula)
        print(val)

        print('Fase Verificadora')
       # print(variables_negativas(val))

    else: 
        print('Numero de clausulas invalido, deben ser de 3 a 10')
    

main(formula)