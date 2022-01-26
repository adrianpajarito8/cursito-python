# CLASE 10 - CURSO DE 12HS
# MULTITHREADING, HILOS DAEMON, MULTIPROCESSING

#import functools
#from abc import ABC, abstractmethod
#import random
import multiprocessing
import time
#import shutil
import threading
import os
from typing import AnyStr
from multiprocessing import Process, cpu_count
os.system("cls")

# THREADS O HILOS
""" 
# Es un hilo de ejecucción que ejecutará su propio set de instrucciones
# el multithread se usa para hacer varias tareas con cuasiparalelismo
# y se ordenan por flags
# Si el programa o tarea espera basicamente entradas internas como
# llamadas o interrupciones del CPU, es mejor usar multiprocessing.
# Si la tarea aguarda por entradas externas como entradas
# de usuario, se usa multithreading

# importamos 'import threading'
# para saber cuanto hilos tenemos activos escribimos:
print("Hilos activos:", threading.active_count())
# para ver la lista de hilos:
print("Lista de hilos:", threading.enumerate())
# Ahora creamos un hilo nuevo


def eat_breakfast():
    time.sleep(3)
    print("Terminaste de comer")


def drink_coffee():
    time.sleep(4)
    print("Terminaste de tomar café")


def study():
    time.sleep(5)
    print("Terminaste de estudiar")


# eat_breakfast()
# drink_coffee()
# study()
# estas 3 funciones se ejecutan de forma secuencial y tardaría
# aproximadamente 12 segundos en terminarlas ya que se ejecutan
# sobre un unico hilo de eventos. En realidad nosotros podemos
# hacer esas 3 tareas a la vez. Entonces necesitaríamos un hilo
# para realizar cada tarea

# creamos cada hilo asociando a las funciones y los iniciamos
# con la función start()
x = threading.Thread(target=eat_breakfast, args=(), name="eat")
x.start()
y = threading.Thread(target=drink_coffee, args=(), name="drink")
y.start()
z = threading.Thread(target=study, args=(), name="estudiar")
z.start()
# En este caso, el mainthread continua ejecutando los dos print
# siguientes, mientras estos 3 hilos ejecutan concurrentemente,
# las funciones que se les asignaron.
print("Lista de hilos:", threading.enumerate())

# también podemos sincronizar los hilos
x.join()
y.join()
z.join()
# con la función join, le decimos al main que espere que los
# hilos x, y, z terminen de ejecutarse antes de seguir.

print("Tiempo de ejecucción de main:", time.perf_counter(), "seg")
 """

# DAEMON THREADS
""" 
# un Daemon thread es un hilo que corre en segundo plano
# el programa no esperará a que un hilo daemon termine para hacer exit
# los hilos no daemon no pueden matarse normalmente y se mantienen
# corriendo hasta que terminen. En este caso, al tener un while True
# sin ninugna opcion de break, el hilo para esta función debe ser
# daemon para que el programa o el main puedan hacer un exit al terminar


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Logeado por:", count, "seg")


# se hace un hilo daemon agregando daemon=True:
x = threading.Thread(target=timer, daemon=True)
x.start()

respuesta = input("Queres salir?:\n")
 """

# MULTIPROCESSING O MULTIPROCESAMIENTO
""" 
# el multiprocessing nos permite obtener paralelismo real ya que
# aprovechamos los multinucleos de nuestros procesadores
#agregamos: 'from multiprocessing import Process,cpu_count'

print("Este PC tiene un procesador con " + str(multiprocessing.cpu_count()) + " núcleos disponibles") #vemos la cantidad de nucleos
# creamos un contador hasta x numero


def counter(num):
    count = 0
    while count < num:
        count += 1

# en este main creamos un proceso que cuenta hasta cien millones
# usando solo un proceso.


def main():
    # creamos el proceso. debemos pasar una tupla por lo que agregamos
    # la coma luego del numero para indicar que es un solo argumento
    # y no una expresión
    '''
    a=Process(target=counter,args=(100000000,))

    a.start()
    a.join()
    print("1 core finished in:",time.perf_counter(),"seg")
    '''
    # esto a mi me toma aprox 3.2 segundos. Ahora contamos hasta el mismo
    # número pero usando 2 procesos o nucleos distintos y que cada uno cuente
    # la mitad de cien millones
    b = Process(target=counter, args=(50000000,))
    c = Process(target=counter, args=(50000000,))
    b.start()
    c.start()
    b.join()
    c.join()
    print("2 cores finished in:", time.perf_counter(), "seg")
    # veremos que se tarda aprox la mitad de tiempo en llegar
    # al mismo valor


# debemos incorporar la variable de entorno name=main y este
# ejecutará el main()
if __name__ == "__main__":
    main()
 """

print("\n", end="")
