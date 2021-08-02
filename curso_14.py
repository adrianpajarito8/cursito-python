# CLASE 14 - CURSO DE 12HS
# RELOJ, crear ejecutable

import os
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import time
os.system("cls")


window = Tk()
window.title("Pajarito APP 4")
height = "300"
width = "300"
# window.geometry(height + "x" + width)  # tamaño de la ventana
window.config(background="white")  # configuración general

# RELOJ Y FUNCION AFTER DE WIDGETS


def update():
    time_string = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    time_label.after(1000, update)


# con la función .after del widget lo actualizamos cada 1000ms
# y llamamos a una función deseada. En este caso es recursiva
time_label = Label(window, font=("Arial", 40), text="Hora actual", fg="Green", bg="Black")
time_label.pack(fill=X)

time_label = Label(window, font=("Arial", 40), fg="Green", bg="Black")
time_label.pack()

update()  # llamamos a la función update

#CREAR EJECUTABLE:

# para crear el ejecutable necesitamos tener instalados pip y pyinstaller.
# movemos todos los archivos competentes a una carpeta comun
# vamos a una terminal y navegamos hasta esa carpeta
# en la carpeta ejecutamos: pyinstaller -F -w *nombredelmain.py*    (sin los asteriscos)
# pyinstaller para llamar al instalador, -F para guardar todo lo de la carpeta,
# -w si no necesitamos una terminal para usarlo, nombre del archivo principal
# se crean unas carpetas en el directorio y en la carpeta "dist" estará nuestro .exe para
# abrir la aplicación

window.mainloop()

print("\n", end="")
