# CLASE 5 - CURSO DE 12HS
# EXCEPCIONES, MANEJO DE ARCHIVOS

import time
import os
import shutil
print("\n", end="")

# MANEJO DE EXCEPCIONES
""" 
# son eventos detectados durante la ejecución que alteran
# el flujo normal del programa y evitan que terminen.

try:  # El try se agrega cuando estamos ante un posible fallo por input
    numerador = int(input("Ingrese el numerador "))
    denominador = int(input("Ingrese el denominador "))
    resultado = numerador/denominador
except ZeroDivisionError as e:  # esto capta el error de dividir por 0 y ejecuta lo que le sigue
    print("No podes dividir por cero pelotudo")
    print(e)  # capta el titulo real de la excepción. No es obligatorio.
except ValueError as e:  # esto capta la división de caracteres y no numeros
    print("No podes dividir palabras huevón. Usá números !=0")
    print(e)
except Exception as e:  # capta todas las demás excepciones
    print("En algo te la mandaste, anda a saber en que...")
    print(e)
else: #se ejecuta si no capta ninguna excepción
    print("El resultado es:",resultado)  # solo printeamos si no hay errores
finally: #siempre se ejecuta al final. Es opcional
    print("Terminaste el try prro")
 """

# DETECCIÓN DE ARCHIVOS
""" 
# si buscamos un archivo se coloca doble barra invertida
path = "D:\\Documents\\VS Code Scripts\\curso_python_12hs\\curso_5_texto.txt"

if os.path.exists(path):  # verifica si el directorio y el archivo existen
    print("La ubicación si existe existe")
    if os.path.isfile(path):  # verifica si es un archivo
        print("Es un archivo")
    elif os.path.isdir(path):  # verifica si es un directorio o carpeta
        print("Es un directorio")
else:
    print("No existe")
 """

# LECTURA DE ARCHIVOS

# revisar que el archivo esté en la misma carpeta que el .py y que en la terminal
# se ejecuta el código en dicha carpeta.
with open("curso_5_texto.txt") as file:  # abre el archivo.
    print(file.read())  # lee el archivo y lo printea

print(file.closed)  # es un flag para saber si el archivo esta abierto o no


# ESCRIBIR ARCHIVO
""" 
print(os.getcwd())  # printea el directorio de trabajo actual o cwd
text = "Acabo de escribir este archivo :Dooo"  # el texto a escribir
with open("curso_5_writetest.txt", "w") as file:  # abre el archivo y lo guarda en la variable file
    file.write(text)  # escribe el archivo
    print("Se creó y escribió el archivo")
 """

# COPIAR ARCHIVOS
""" 
#copyfile() : copia el contenido de un archivo
#copy() : igual que el anterior pero con permisos y con directorio específico
#copy2() : igual que el anterior con metadata

#creamos un archivo copia
shutil.copyfile("curso_5_writetest.txt","curso_5_writetest_copia.txt")
 """

# MOVER ARCHIVOS
""" 
source = "curso_5_writetest_copia.txt"
destination = "D:\\curso_5_writetest_copia.txt"

try:
    if os.path.exists(destination):  # verifica que no exista un archivo igual
        print("Ya hay un archivo", source, "en la carpeta destino")
    else:
        # método para mover la carpeta o archivo
        os.replace(source, destination)
        print("Se movió el archivo")
except FileNotFoundError:
    print("El archivo no existe")
 """

# BORRAR ARCHIVO
""" 
path = "curso_5_autodestruccion.txt"
text = "Este archivo se borrará en 3 segundos"  # el texto a escribir
with open(path, "w") as file:  # abre el archivo y lo guarda en la variable file
    file.write(text)  # escribe el archivo
    print("Se creó el archivo y se eliminará en 3 segundos")

time.sleep(3)  # espera 3 segundos
os.remove(path)  # borra el archivo
# os.rmdir(path)  # para borrar directorios o carpetas vacias
# shutil.rmtree(path) # para borrar directorios o carpetas no vacías
print("El archivo", path, "se borró")
 """