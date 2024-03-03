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
#FASE ADIVINADORA.
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

#Primera version de la funcion
#def variables_negativas(formula_con_val):
#Auxiliar para hacer la FASE VERIFICADORA
#Recorre la formula donde cada variable ya tiene un valor asignado,
#pero hay casos en los que podemos tener en nuestra clausula un "-x"
#donde si x es 1, entonces -x es 0, en esta funcion hacemos esa conversion.
#    
#    #split() puede usarse para pasar a lista una cadena
#    #lo pasamos a lista para que sea mas facil la conversion / sustitucion que queremos hacer
#    lista = formula_con_val.split() 
#
#    #Recorremos y hacemos la conversion.
#    for i in range(len(lista)):
#        if lista[i] == '-1':
#            lista[i] = 0
#
#        if lista[i] == '-0':
#            lista[i] = 1
#    
#    return lista

def variables_negativas(formula_con_val):
#Auxiliar para hacer la FASE VERIFICADORA
#Ya tiene un valor asignado, pero hay casos en los que podemos tener en nuestra clausula un "-x"
#donde si x es 1, entonces -x es 0, en esta funcion hacemos esa conversion.

    #Recorremos y hacemos la conversion / sustitucion
    #Lo que pasa en cada replace() es que recorre la cadena y hace la sustitucion a medida que va avanzando
    formula_con_val = formula_con_val.replace("-1", "0")

    #Aqui la cadena ya no tiene -1, fueron ya sustituidos por 0. Ahora recorre para sustituir los -0 con 1
    formula_con_val = formula_con_val.replace("-0", "1")

    return formula_con_val


def para_or(cadena):
#FASE VERIFICADORA, se encarga de los or de la formula.
#En la tabla de verdad de or, solo tenemos valores false cuando todas nuestras
#variables son false. En el resto de los casos es true. 

    nueva = ''

    #Para eliminar espacios, simbolos *
    for i in cadena:

        if i == '*':
            nueva += i 

        if i == '(':
            nueva += ' (' 

        elif i.isdigit():
            nueva += i 

        elif i == ')':
            nueva += ') '

    #replace() lo que hace es que recorrer la cadena nueva y hace la sustitucion conforme avanza
    nueva = nueva.replace("(000)", "0")
    nueva = nueva.replace("(001)", "1")
    nueva = nueva.replace("(010)", "1")
    nueva = nueva.replace("(011)", "1")
    nueva = nueva.replace("(101)", "1")
    nueva = nueva.replace("(100)", "1")
    nueva = nueva.replace("(110)", "1")
    nueva = nueva.replace("(111)", "1")

    return nueva


def para_and(cadena):
#FASE VERIFICADORA, se encarga de los and de la formula.
#En la tabla de verdad de and, solo tenemos valor true cuando todas nuestras
#variables son true. En el resto de los casos es false. 

    #La logica para esta operacion and es hacerla de dos en dos,es decir, si tienes por ejemplo v and v and f debes
    #hacer primero la operacion con dos variables y el valor que obtengas lo usas para hacer la operacion con 
    #la variable sobrante, v and v and f => v and f => f hasta que al final te quedas con un solo valor.
    #Entonces queremos que poco a poco se vayan reemplazando los valores hasta quedarnos con un valor, por eso el while
    #tiene esa condicion.
    while '1 * 1' in cadena or '1 * 0' in cadena or '0 * 1' in cadena or '0 * 0' in cadena:

        cadena = cadena.replace(" 1 * 1 ", " 1 ")
        cadena = cadena.replace(" 1 * 0 ", " 0 ")
        cadena = cadena.replace(" 0 * 1 ", " 0 ")
        cadena = cadena.replace(" 0 * 0 ", " 0 ")

    return cadena


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

        o = para_or(vn)
        print('Resolvemos los OR:')
        print(str(o))

        a = para_and(o)
        print('Y finalmente los AND:')
        print(str(a))

    else: 
        print('Numero de clausulas invalido, deben ser de 3 a 10')
    

main(formula)
