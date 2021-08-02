# CLASE 9 - CURSO DE 12HS
#

import functools
from abc import ABC, abstractmethod
import random
import time
import shutil

import os
from typing import List
os.system("cls")

# COMPRENSIÓN DE LISTAS
""" 
# metodo para crear una nueva lista con poca sintaxis. El formato es:
# lista=[expresion for item in iterable]

# podemos usar las siquientes lineas de código:
# cuadrados=[]
# for i in range(1,11):
#     cuadrados.append(i*i)
# print(cuadrados)

# y reemplazarlas por esta unica linea:
print("Sin if:", cuadrados := [i * i for i in range(1, 11)])

# otro ejemplo agregando un condicional if
estudiantes = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
estudiantes_aprobados = [i for i in estudiantes if i >= 60]
print("Con if:", estudiantes_aprobados)
# tambien podemos agregar un else. En este caso debemos mover
# el condicional antes del for
estudiantes_aprobados = [i if i >= 60 else "FAIL" for i in estudiantes]
print("Con else:", estudiantes_aprobados)
 """

# COMPRENSIÓN DE DICCIONARIOS
""" 
# metodo para crear un nuevo diccionario con poca sintaxis. El formato es:
# diccionario = {key: expresion for (key, value) in iterable}

ciudades_en_F = {"New York": int(40), "Boston": int(85),
                 "Los Angeles": int(100), "Chicago": int(50)}

ciudades_en_C = {key: int(((value - 32) * (5 / 9)))
                 for (key, value) in ciudades_en_F.items()}
print("En Farenheit:", ciudades_en_F)
print("En Celsius:", ciudades_en_C)

# para usar condicionales if se usa la formula:
# diccionario = {key: expresion for (key, value) in iterable if condicional}

# si queremos incluir un else en el if usamos:
# diccionario = {key: expresion if/else condition for (key, value) in iterable}
ciudades_calidas = {key: "Cálida" if temp >= 25 else "Fría" for (key, temp) in ciudades_en_C.items()}
print("Ciudades cálidas condicional:", ciudades_calidas)


def check_temp(temperatura):
    if temperatura >= 25:
        return "Cálido"
    else:
        return "Frío"


# por ultimo podemos usar funciones como expresiones
ciudades_calidas = {key: check_temp(temp) for (key, temp) in ciudades_en_C.items()}
print("Ciudades cálidas con función:", ciudades_calidas)
 """

# FUNCION ZIP
""" 
# agrega elementos desde dos o mas iterables(listas,tuplas,sets,etc)
# crea un conjunto con elementos paralelos separados en tuplas
# similar a unir los valores de varias columnas en una
usuarios = ["Adrián", "Gabriel", "Sebastian", "Claudio"]
contraseñas = ["pass123", "gabo31", "sebcol2", "claudio00"]
# queremos unir la lista como pares para que cada usuario esté
# con su contraseña
users = list(zip(usuarios, contraseñas))
zip_list = users[:]
# zip() crea un objeto de una clase
users_list = users  # casteamos para que sea lista de tuplas
print(users_list)
users_dict = dict(users)  # casteamos para que sea diccionario
print(users_dict)
# de usar mas iterables, no será posible castear a diccionario.
 """

# VARIABLES ESPECIALES DEL INTERPRETADOR DE PYTHON
""" 
# __name__=='__main__"

# para los archivos (o módulos) de python, usando esta función
# se puede correr un archivo como un programa único o como un módulo "A"
# que se importa a otro módulo "B". Cuando el archivo "B" interpreta
# el 'import modulo "A"' este lo ejecuta lo cual normalmente no se
# desea. Solo lo importamos para usarlo cuando lo necesitemos


def hello():
    print("hello")


# se debe usar siempre que sea posible
if __name__ == "__main__":
    hello()
    # si ejecutamos este archivo se imprimirá hello pero si
    # lo ejecutamos desde otro archivo que importó este código
    # no veremos el mensaje hello ya que name!=main en el otro
    print("Corriendo este modulo directamente")
    # podriamos definir una función main si quisieramos
else:
    # el archivo curso_9_main.py solo hará esto cuando importe
    # este script:
    print("Corriendo indirectamente")
 """

# MODULO TIME
""" 
# debemos poner 'import time'

# string con fecha desde el primer  epoch del pc pasados 'x' segundos:
print(time.ctime(1000000))
# segundos pasados desde la primer epoch del pc
print(time.time())
#uniendo las 2 anteriores podemos obtener la fecha y hora actual
print(time.ctime(time.time()))
#o también se crea como un objeto:
time_object=time.localtime()
print(time_object)
#para acceder al objeto usamos:
time_formated=time.strftime("%b %H:%M:%S - %d/%m/%Y",time_object) #ver documentación
print(time_formated)
#para dar un string y obtener un objeto usamos strptime():
time_string="20 april, 2020"
time_object_2=time.strptime(time_string,"%d %B, %Y")
print(time_object_2)
 """


print("\n", end="")
