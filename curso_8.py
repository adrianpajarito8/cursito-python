# CLASE 8 - CURSO DE 12HS
# OPERADOR walrus, ASIGNAR FUNCIONES A VARIABLES, FUNCIONES DE ALTO ORDEN, FUNCIÓN LAMBDA

import functools
from abc import ABC, abstractmethod
import random
import time
import os
import shutil

os.system("cls")

# OPERADOR walrus
""" 
# es un operador de asignación para expresiones
# a continuación tenemos que asignar un valor a happy y luego hacer el print
happy = True
print(happy)
# ahora intentamos hacerlo en una linea (parte del try:) y nos
# salta la exception.
try:
    print(happy=True)
except Exception:
    print("NO PODES ASIGNAR VALORES A UNA VARIABLE DENTRO DE UNA EXPRESIÓN")
# con el ":=" podemos asignar
# un valor a una variable, dentro de una expresión
print(happy := True)
# esto nos permite ahorrarnos lieas de código
 """

# ASIGNACIÓN DE FUNCIONES A VARIABLES
""" 
# como conocemos la función print la asignamos a una variable
pr = print
# si no usamos parentesis se copia la dirección de memoria
# donde está alocada la función print en la variable pr
# ahora podemos usar la variable pr como una función print
pr("Esto funciona como un print")
# la llamada o asignación sin parentesis se refiere a la locación
# en la memoria de la función. Parecido a los apuntadores en C


def hola():
    print("Hola")

# Esto imprime la dirección de memoria donde se alojó
# la función hola. observar que se escribió "hola" y no "hola()"
print(hola)  
 """

# FUNCIONES DE ALTO ORDEN
""" 
# estas pueden recibir funciones como argumentos o también
# pueden retornar funciones


def mayuscula(texto):
    return texto.upper()


def minuscula(texto):
    return texto.lower()


def hola(funcion):  # Función de alto orden
    text = funcion("HoLa")
    print(text)


# Llamamos a la función hola con la función mayuscula como
# argumento. una vez en la función hola, se podrá utilizar la
# función mayuscula como si estuviese dentro de esta función.
# En este caso se le envía el texto HoLa, lo convierte en mayuscula,
# guarda el return en la variable "text" y lo printea.
hola(mayuscula)
# Lo mismo con minuscula
hola(minuscula)

# Ahora veremos lo de retornar funciones


def divisor(y):
    def dividendo(x):
        return x / y

    return dividendo


# Lo que hacemos es llamar a la función de alto orden "divisor(y)"
# y se asigna el valor 2 a la variable y. NO entra a la fucnión
# dividendo porque no la hemos llamado y retorna la función dividendo
# asignandola a la variable "divid". Ahora divid contiene la función
# dividendo la cual llamamos en el print con el valor 6, retonrnando
# el valor de la división
divid = divisor(2)
print(divid(6))
 """

# FUNCIÓN LAMBDA
""" 
# la función lambda sirve para armar una expresión asignando
# varios parametros a la vez

fun = lambda x, y, z: x * z / y  # el formato es lamda arg1,arg2,arg3 : expresión

print("El resultado es:", fun(5, 2, 3))

mayor_de_edad = lambda edad: True if edad >= 18 else False
print("Es mayor de edad?:", mayor_de_edad(23))

# también podemos pasar una lista
notas_examenes = [10, 8, 10, 8, 9]

promedio = lambda notas: sum(notas) / len(notas)
print("El promedio es:", promedio(notas_examenes))
 """

# SORTING TYPES
""" 
estudiantes = [("Adrián", "A", 27), ("Gabriel", "C", 21), ("Claudio", "F", 23)]

columna = lambda col: col[0]
# la función sort solo funciona con listas
# el key es un objeto FUNCIÓN. no puede recibir int
estudiantes.sort(key=columna, reverse=True)
for i in estudiantes:
    print(i)
print("")

# para una tupla debemos usar la fucnion sorted() que
# tambien viene con parametros key y reverse
estudiantes = (("Adrián", "A", 27), ("Gabriel", "C", 21), ("Claudio", "F", 23))
estudiantes_ordenada = sorted(estudiantes, key=columna, reverse=1)
for i in estudiantes_ordenada:
    print(i)
 """

# MAP
""" 
# sirve para aplicar una función a cualquier item en una lista o tupla
# armo una lista de tuplas
tienda = [("Remeras", 2150),
          ("Pantalones", 2530),
          ("Medias", 114),
          ("Zapatillas", 2980)]

ars_to_usd = 99.75
# escribo la función de conversión para la columna de precios [1]
cambio_dolares = lambda dato: (dato[0], round(dato[1] / ars_to_usd, 2))
# creo una lista. Llamo a la función map y le paso la
# función para conversión y la lista iterable "tienda"
tiendaenusd = list(map(cambio_dolares, tienda))
# se reescribe cada fila según indique la tupla de la función lambda ya que
# estamos reescribiendo una tupla por cada indice de la lista "tienda".
# Cada uno de los indices se printea a continuación

for i in tiendaenusd:
    print(i)
 """

# FUNCION filter PARA LISTAS
""" 
# para filtrar elementos en listas o tuplas

tienda = [("Remeras", 2150),
          ("Pantalones", 2530),
          ("Medias", 114),
          ("Zapatillas", 2980)]

# creamos función para detectar precios (indice [1] de las tuplas
# de la lista) mayores a 2000
precio = lambda data: data[1] >= 2000
# aplicamos este filtro a la lista
precios_elevados = list(filter(precio, tienda))

for i in precios_elevados:
    print(i)
 """

# FUNCIÓN reduce PARA LISTAS
""" 
# importo "functools"
factorial = [5, 4, 3, 2, 1]
# a continuación uso reduce que recibe una función y un iterable al
# que la aplicará. Lo que hace esta función es recibir los dos primeros
# valores de la lista [0] y [1], los reemplaza por x e y, y hace lo que dicta la
# función lambda, luego lo hace con los indices [1] y [2], [2] y [3]...y asi
# sucesivamente hasta el penúltimo y ultimo valor de la lista.
resultado = functools.reduce(lambda x, y: x * y, factorial)

print(resultado)  # printea 120 que es igual a 5! (5 factorial)
# también sirve para strings
 """

print("\n", end="")
