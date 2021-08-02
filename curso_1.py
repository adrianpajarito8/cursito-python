# CLASE 1 - CURSO DE 12HS
# VARIABLES, ASIGNACIÓN MÚLTIPLE, MÉTODOS PARA STRINGS, CASTEOS, INPUTS, FUNCIONES MATEMÁTICAS Y RECORTE DE STRINGS

# VARIABLES
""" 
# String
nombre = "Adrián"
apellido = "Cantaloube"
print(type(nombre))
print("Soy " + nombre+" "+apellido)

# Int
edad = 26
edad += 1
print(type(edad))
print("Forma 1: Mi edad es", edad)
print("Forma 2: Mi edad es "+str(edad))

# Float
altura = 1.72
print(type(altura))
print("Mi altura es:", altura, "metros")

# Boolean
Humano = True
print(type(Humano))
print("¿Es humano?: ", Humano)
 """

# ASIGNACIÓN MÚLTIPLE
""" 
nombre, apellido, edad = "Adrián", "Cantaloube", 27
print(nombre)
print(apellido)
print(edad)
 """

# MÉTODOS PARA STRINGS
""" 
nombre = "adrián"
print(len(nombre))
# devuelve posición de la primera coincidencia en el string
print(nombre.find("a"))
print(nombre.capitalize())
print(nombre.upper())
print(nombre.count("a"))  # Cuenta cuantas "a" hay en la palabra
print(nombre.isalpha())
print(nombre.replace("a", "A"))
print(nombre*3)
 """

# CASTEO DE VARIABLES
""" 
x = 1
y = 2.0
z = "3"
print("Originales:")
print(x)
print(y)
print(z)

print("\nInt:")
print(int(x))
print(int(y))
print(int(z))

print("\nFloat:")
print(float(x))
print(float(y))
print(float(z))

print("\nString:")
print(str(x))
print(str(y))
print(str(z))
 """

# ENTRADAS DE USUARIO
""" 
nombre = input("Cual es tu nombre?:")
print("Hola", nombre)
edad = int(input("Cual es tu edad?:"))
print("Tienes", edad, "años!")
 """

# FUNCIONES MATEMÁTICAS
""" 
import math
pi = 3.14
x = 1
y = 2
z = 3
print(round(pi))
print(math.ceil(pi))  # redondea para arriba
print(math.floor(pi))  # redondea para abajo
print(abs(-pi))
print(pow(pi, 2))
print(math.sqrt(pi))
print(max(x, y, z))
print(min(x, y, z))
 """

# RECORTE DE STRINGS
""" 
nombre = "Adrián Nicolás Cantaloube"
nombre_letra = nombre[1]  # Indicando el índice extraemos el valor del indice
nombre_serie = nombre[0:6]
nombre_recortado = nombre[0:15:3]  # inicio,final,step(minimo step es 1)
# los valores pueden dejarse en blanco si se quiere indicar el inicio o final del string automaticamente
nombre_reversa = nombre[::-1]  # String n reversa
print(nombre_letra)
print(nombre_serie)
print(nombre_recortado)
print(nombre_reversa)
 """