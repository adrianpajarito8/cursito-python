# CLASE 6 - CURSO DE 12HS
# MODULOS, POO, VARIABLES INSTANCIADAS Y DE CLASES, HERENCIA

import random
import time
import os
import shutil
os.system("cls")


# MODULOS
""" 
# Es un archivo que contiene código de python con funciones,
# variables, clases, etc. usado en programación modular

import curso_6_mensajes as mens #si queremos importar con alias
mens.hola()
mens.chau()
print("\n",end="")

from curso_6_mensajes import hola #importo solo funciones específicas
hola()
try: #intentamos imprimir chau()
    chau()
except Exception:
    print("No podes imprimir la función 'chau()' porque no la importaste en el 'from'")

# podemos consultar una lista de módulos disponibles usando:
# help("modules")
 """

# JUEGO DE PIEDRA, PAPEL O TIJERA
""" 
while 1:
    opciones = ["piedra", "papel", "tijera"]
    print("Bienvenido al juego\n")
    computadora = random.choice(opciones)
    jugador = None

    while jugador not in opciones:
        jugador = input("Elige piedra, papel o tijera: ").lower()

    print("Jugador:", jugador)
    print("Computadora:", computadora)

    if jugador == computadora:
        print("Es un empate!")
    elif jugador == "piedra":
        if computadora == "papel":
            print("COMPUTADORA GANA")
        elif computadora == "tijera":
            print("JUGADOR GANA")
    elif jugador == "tijera":
        if computadora == "piedra":
            print("COMPUTADORA GANA")
        elif computadora == "papel":
            print("JUGADOR GANA")
    elif jugador == "papel":
        if computadora == "tijera":
            print("COMPUTADORA GANA")
        elif computadora == "piedra":
            print("JUGADOR GANA")

    jugar_de_nuevo = input("Quiere volver a jugar? Si o No: ").lower()
    if jugar_de_nuevo != "si":
        break
 """

# PROGRAMACIÓN CON OBJETOS
""" 
# un objeto es una instancia de una clase
# cada clase tiene atributos(que y como es) y métodos(que puede hacer)
# revisar el archivo "curso_6_class.py"

# no hace falta pasar el self
auto1 = Auto("Volkswagen", "Gol Trend", 2016, "Gris")

print(auto1.marca)
print(auto1.modelo)
print(auto1.año)
print(auto1.color)

auto1.drive()
auto1.stop()
 """

# INSTANCIACIÓN DE VARIABLES DE LAS CLASES
""" 
from curso_6_class import Auto
# revisar el archivo "curso_6_class.py"
# ahora se usa el nro de ruedas como una variable de clase
auto1 = Auto("Volkswagen", "Gol Trend", 2016, "Gris")
auto2 = Auto("Citroen", "Picasso", 2013, "Verde")

print(auto1.ruedas)  # printea "4"
print(auto2.ruedas)  # printea "4"
auto1.ruedas = 3
print(auto1.ruedas)  # printea "3"
# cambia las ruedas de todos los objetos Auto a "6" 
# excepto los que ya fueron modificados manualmente
Auto.ruedas = 6  
print(Auto.ruedas)
print(auto1.ruedas)  # printea "3" porque fue modificado anteriormente
print(auto2.ruedas)  # printea "6"
 """

# HERENCIA
""" 
class Animal:  # Creo la clase padre "Animal"

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):  # Rabbit hereda todo lo que tiene la clase Animal
    def run(self):
        print("The rabbit is running")


class Fish(Animal):
    def swim(self):
        print("The rabbit is swimming")


class Hawk(Animal):
    def fly(self):
        print("The rabbit is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
rabbit.run()
 """

# HERENCIA MULTINIVEL
""" 
class Organismos:
    alive = True


class Animal(Organismos):

    def eat(self):
        print("This animal is eating")


class Dog(Animal):

    def bark(self):
        print("This dog is barking")


frodo = Dog()
print(frodo.alive)  # frodo de la clase Dog tiene herencia de Animal y Organismos
 """

# HERENCIA MULTIPLE
""" 
# cuando una clase hijo es heredada de 2 o mas clases padre


class Papa:
    def genes_p(self):
        print("Tiene genes de el padre")


class Mama:
    def genes_m(self):
        print("Tiene genes de la madre")


class Hijo(Papa, Mama):
    pass


juan = Hijo()
juan.genes_m()
juan.genes_p()
 """

print("\n", end="")
