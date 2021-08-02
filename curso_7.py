# CLASE 7 - CURSO DE 12HS
# OVERRIDE DE METODOS, CADENA DE METODOS, FUNCIÓN SUPER, CLASES ABSTRACTAS,FUNCIONES CON ARGUMENTOS OBJETO

from abc import ABC, abstractmethod
import random
import time
import os
import shutil
os.system("cls")

# OVERRIDE DE MÉTODOS
""" 
# permite que una clase hijo provea un override
# de un método que ya le fue dado por su padre


class Animal:
    def eat(self):
        print("This animal is eating")


class Conejo(Animal):
    def eat(self):  # este "eat()" reemplaza al "eat()" heredado
        print("This rabbit is eating a carrot")


conejo = Conejo()
conejo.eat()
 """

# CADENA DE MÉTODOS
""" 
# sirve para llamar multiples métodos de forma secuencial
class Auto:
    def encender(self):
        print("El auto está encendido")
        return self  # El return self es para poder llamar a la cadena de acciones

    def freno(self):
        print("El auto está con el freno")
        return self

    def sinfreno(self):
        print("El auto está sin freno")
        return self

    def primera(self):
        print("Pusiste primera")
        return self


# gracias al return self:
auto = Auto()
auto.encender().freno().sinfreno().primera()  # llamamos a todos con una linea
# si es muy largo podemos usar la barra invertida
# para indicar una continuación de linea
auto.encender()\
    .freno()\
    .sinfreno()\
    .primera()
 """

# FUNCION super()
""" 
# sirve para dar acceso a los métodos de las clases padre

class Rectangulo:

    def __init__(self, ancho, alto) -> None:
        self.ancho = ancho
        self.alto = alto


class Cuadrado(Rectangulo):

    def __init__(self, ancho, alto) -> None:
        # con la función super llamo a los métodos del padre
        # en este caso llamo al metodo __init__
        super().__init__(ancho, alto)

    def area(self):
        return self.alto*self.ancho


class Cubo(Rectangulo):

    def __init__(self, ancho, alto, largo) -> None:
        # con la función super llamo a los métodos del padre
        # y no los tengo que andar reescribiendo
        super().__init__(ancho, alto)
        self.largo = largo

    def volumen(self):
        return self.alto*self.ancho*self.largo


cuadrado1 = Cuadrado(3, 3)
cubo1 = Cubo(3, 3, 3)

print(cuadrado1.area())
print(cubo1.volumen())
 """

# CLASES ABSTRACTAS
""" 
# las clases abstractas sirver para evitar que los usuarios puedan
# crear, en este caso, una clase "Vehiculo", ya que tiene declaraciones
# pero no implementaciones. Solo necesitamos sus clases hijo que
# son Auto o Moto

# importamos el "from abc import ABC,abstractmethod"
# y escribimos la clase padre Vehículo como se ve a continuación:


class Vehiculo(ABC):  # notar el ABC como parámetro de clase
    # debe haber al menos 1 @abstractmethod para que sea clase abstracta

    @abstractmethod
    def inicio(self):
        pass

    def fin(self):
        print("Fin de clase Vehiculo")

# al inicial las clases hijo de la clase padre con métodos abstractos,
# se debe hacer un override los métodos abstractos del padre. En este
# caso solo debemos hacer override de la función inicio(self)


class Auto(Vehiculo):
    def inicio(self):
        print("Inicio Automovil")


class Moto(Vehiculo):
    def inicio(self):
        print("Inicio Motocicleta")


# ahora podemos crear objetos con las clases Auto y Moto pero no con Vehiculo
try:
    vehiculo = Vehiculo()
    # no se imprmirá porque es una clase abstracta
    print("OBJETO VEHICULO CREADO")
except TypeError:
    print("NO PUEDES INSTANCIAR UN OBJETO DE CLASE ABSTRACTA")

auto = Auto()
moto = Moto()
auto.inicio()
moto.inicio()
# como vemos también se importa el metodo fin sin instanciarlo en
# la clase Auto y Moto porque no es un método abstracto de Vehiculo
auto.fin()
moto.fin()
 """

# PASAR OBJETOS COMO ARGUMENTOS
""" 
class Auto:
    color = None

# observar que la función no esta dentro de la clase
def cambiar_color(automovil, color):
    automovil.color = color


auto1 = Auto()
auto2 = Auto()
auto3 = Auto()
# auto1, auto2 y auto3 son objetos y estos son pasados a la función
# cambiar_color junto con el color a cambiar. La función recibe
# el objeto y es capaz de modificar la variable "color" de la clase
print(auto1.color, auto2.color, auto3.color)
cambiar_color(auto1, "Rojo")
cambiar_color(auto2, "Azul")
cambiar_color(auto3, "Gris")
print(auto1.color, auto2.color, auto3.color)
 """

print("\n", end="")
