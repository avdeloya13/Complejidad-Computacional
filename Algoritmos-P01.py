import sys
import random

"""
Algoritmos No Deterministicos
3 - SAT
Author: Ana Valeria Deloya Andrade
"""

archivo = sys.argv[1]
#Abrimos el archivo que contiene la formula booleana.
archivo = open(archivo)

#Leemos el archivo y lo asignamos a una variable formula.
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

    #Si pasa sus cotas minimas y maximas devuelve false, si no true.
    if parentesis < 6 or parentesis > 20:
        return False
    else: 
        return True


def asignaValor(formula):
#Fase Adivinadora.
#Recorre la formula para asignar un valor a cada variable.

    #L valores random que tendran las variables.
    var_x = random.randint(0,1)
    var_y = random.randint(0,1)
    var_z = random.randint(0,1)

    #Nueva cadena que al final va a contener la formula con sus valores random asignados.
    con_valores = ''

    #Recorremos la formula y asignamos los valores.
    for i in formula:
        if i == 'x':
            con_valores += str(var_x)
        elif i == 'y':
            con_valores += str(var_y)
        elif i == 'z':
            con_valores += str(var_z)
        else:
            con_valores += i 
    
    #Regresa la cadena con los valores asignados.
    return con_valores


def variables_negativas(formula_con_val):
#Auxiliar para hacer la Fase Verificadora
#Recorre la formula donde cada variable ya tiene un valor asignado,
#pero hay casos en los que podemos tener en nuestra clausula un "-x"
#donde si x es 1, entonces -x es 0, en esta funcion hacemos esa conversion.

    #Convertimos a lista porque asi es mas facil hacer la conversion que queremos.
    lista = formula_con_val.split()

    #Recorremos y hacemos la conversion.
    for i in range(len(lista)):
        if lista[i] == '-1':
            lista[i] = 0

        elif lista[i] == '-0':
            lista[i] = 1
    
    #Lo siguiente es mas que nada para que se vea bonito al imprimirlo en terminal.
    #Vamos a ir convirtiendo los elementos de la lista de nuevo a string.

    #Iterando en join, convirtiendo a str y agregando un espacio en blanco ' ' entre los elementos.
    cadena = ' '.join(str(j) for j in lista) 
    return cadena

def para_or(cadena):
#Fase Verificadora, para los or de la formula.
#En la tabla de verdad de or, solo tenemos valores false cuando todas nuestras
#variables son false. En el resto de los casos es true. 

    #Vamos a dejar de lado el and *
    bye_simbolo_and = ' '.join(str(j) for j in (cadena.split(' * ')))

    #Haremos el or pero ya no necesitamos el simbolo +
    bye_simbolo_or = ' '.join(str(j) for j in (bye_simbolo_and.split(' + ')))

    return bye_simbolo_or

def main(formula):
#Funcion main para mandar a llamar todo, ordenado.

    clausulas = clausulas_limite(formula)

    if clausulas == True:
        print('Fase Adivinadora')
        av = asignaValor(formula)
        print(av)

        print('Fase Verificadora')
        vn = variables_negativas(av)
        print('Nos encargamos de los NOT:')
        print(str(vn))

    else: 
        print('Numero de clausulas invalido, deben ser de 3 a 10')
    

main(formula)

p = para_or('( 0 + 1 + 0 ) * ( 1 + 0 + 1 ) * ( 1 + 0 + 0 ) * ( 0 + 0 + 1 )')
print(str(p))