# CLASE 4 - CURSO DE 12HS
# FUNCIONES, SCOPE DE VARIABLES,PARAMETRO *args, PARÁMETRO **kwargs, STRING FORMAT, RANDOM
print("\n")

# FUNCIONES Y RETURN
""" 
def hello(nombre="Julieta", apellido="Farina"):
    print("Hola", nombre, apellido)
    print("Bienvenido")


# esta llamada sin argumentos está permitida ya que definimos valores por default
hello()
# ...de no ser así se deben ingresar los argumentos si o si
# Establezco argumentos nuevos:
mi_nombre = "Adrián"
mi_apellido = "Cantaloube"
hello(mi_nombre, mi_apellido)
#se pueden usar los nombres de los argumentos para evitar ponerlos en orden
hello(nombre = mi_nombre, apellido = mi_apellido) 


def division(numerador, denominador):
    return float(numerador/denominador)


print(division(10, 2))
 """

# VARIABLE SCOPE
""" 
# las diferencias entre las variables globales y locales
nombre = "Adrián"


def display_name():
    nombre = "Pajarito"
    return nombre

# No podemos hacer "print(nombre)" afuera de la...
# función porque "nombre" solo existe dentro de esa función
print(nombre)  # Esto devuelve "adrián"
display_name()
print(nombre)  # Esto devuelve "adrián" ya que nombre se modificó solo de forma local"
nombre = display_name()
print(nombre)  # Esto devuelve "Pajarito" ya que se asignó el nuevo nombre devuelto por return
 """

# PARAMETRO *args
""" 
# es un parámetro que almacena todos los argumentos en una tupla
# esto permite que la cantidad de argumentos que le pasemos a una
# función pueda cambiar. Por ejemplo, para una sumatoria de n números


def suma_tupla(*args):
    sum = 0  # se inicializa la variable sum
    for i in args:  # toma toda la tupla
        sum += i  # suma todos los valores
    return sum  # devuelve la suma


print(suma_tupla(1, 2, 3, 4, 5, 6, 7, 40))


def suma_list(*args):
    sum = 0  # se inicializa la variable sum
    args = list(args)  # casteamos para que sea una lista y podamos modificarla
    args[-1] = 0  # podemos modificar la lista de argumentos que pasamos
    for i in args:  # toma toda la tupla
        sum += i  # suma todos los valores
    return sum  # devuelve la suma


print(suma_list(1, 2, 3, 4, 50))
 """

# PARÁMETRO **kwargs
""" 
# similar al anterior pero los guarda como diccionario
# para que una función pueda recibir una indefinida cantidad de claves


def hola(**kwargs):
    print("Hello", kwargs["titulo"], kwargs["nombre"], kwargs["apellido"])
    # O de otra forma para longitud indefinida...
    print("Hola", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hola(titulo="Ingeniero", nombre="Adrián", apellido="Cantaloube")
# entonces definimos el diccionario con claves y valores
# y la función reemplaza las claves por sus respectivos valores
# sin importar la cantidad de argumentos
 """

# MÉTODO FORMAT PARA STRINGS
""" 
# es un método opcional para strings
# se usan las llaves {} para indicar un placeholder
# parecido a el %s, %d, %f en C

mozo = "Adrián"
cliente = "Gabi"

print("El mozo {} derramó fernet sobre {}".format(mozo, cliente))
# se pueden alternar usando los índices entre las llaves...
print("El mozo {1} derramó fernet sobre {0}".format(mozo, cliente))
# o también con nombres calves
print("El mozo {mozo} derramó fernet sobre {cliente}".format(mozo="Claudio", cliente="Fabrizio"))
# podemos almacenar espacio también
print("El mozo {mozo:<9} derramó fernet sobre {cliente:>7}. Bajon para la {ella:^7} me amor".format(mozo="Claudio", cliente="Fabrizio", ella="Noe"))
# también podemos usar {:b},{:f},{:o},{:X} para binario, flotante, octo y hex respectivamente
 """

# RANDOM
""" 
import random
print(random.randint(1, 100))  # random entre 1 y 100
print(random.random())  # random entre 0 y 1

print(random.choice(["Vino", "Cerveza", "Fernet"]))

# para "barajar" una lista se deben hacer estos 3 por separado
digitos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
random.shuffle(digitos)
print(digitos)
 """