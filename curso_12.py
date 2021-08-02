# CLASE 12 - CURSO DE 12HS
# GUIA COMPLETA DE TKINTER

from tkinter import *
import os
from typing import DefaultDict, List, Sized
from tkinter import messagebox  # se agrega porque es un submodulo
from tkinter import filedialog
os.system("cls")


window = Tk()  # inicia una instancia de una ventana
window.title("Pajarito APP 2")
# window.geometry("400x400")  # tamaño de la ventana
window.config(background="white")  # configuración general

# VENTANA DE INFORMACIÓN, AVISO, ERROR, SELECCIÓN Y PREGUNTA

# se debe importar: from tkinter import messagebox


def click():
    messagebox.showinfo(title="Info", message="Hiciste click")
    messagebox.showwarning(title="Warning", message="Hiciste click")
    messagebox.showerror(title="Error", message="Hiciste click")
    respuesta = messagebox.askyesnocancel(title="Si o No?", message="Elegí uno", icon="warning")
    if respuesta is None:
        print("Cancelado")
    elif respuesta is True:
        print("YES BITCH!")
    elif respuesta is False:
        print("¿Porqué no?")
    # revisar los otros messagebox.ask
    pregunta = messagebox.askquestion(title="Pregunta", message="Estas bien?", icon="question")
    if pregunta == "yes":
        print("Yo tambien")
    else:
        print("Why not?")


boton_mensajes = Button(window,
                        command=click,
                        text="Click aquí para mostrar mensajes")
boton_mensajes.pack()

# TEXT WIDGET

# a diferencia del textbox, aqui se pueden escribir multiples lineas


def cantidad_letras():
    count = 0  # inicio count
    for index in texto.get("1.0", END):  # llamo al texto y lo recorro
        if index == entry_letra.get():  # si hay una letra coincidente con la puesta en entry_letra count suma 1
            count += 1
    print(count)


texto = Text(window,
             font=("Courier New", 15),
             relief=SUNKEN,
             bd=2,
             height=20,
             width=50,
             bg="light yellow",
             padx=2,
             pady=2)
texto.pack()
entry_letra = Entry(window,
                    relief=SUNKEN,
                    bd=2)
entry_letra.pack()
boton_texto = Button(window,
                     text="Imprimir count de letras a",
                     command=cantidad_letras)
boton_texto.pack()

# ABRIR ARCHIVOS

# se debe importar: from tkinter import filedialog


def openfile():
    filepath = filedialog.askopenfilename(title="Abrir archivito",  # nombre de la ventana para abrir archivo
                                          initialdir=".\\",  # directorio actual
                                          filetypes=(("Archivo de texto", "*.txt"),
                                                     ("Power BI", "*.pbix"),
                                                     ("All files", "*.*")))  # filtro para extensión de archivos
    try:
        texto.delete("0.0", END)  # Borro el contenido de la ventana texto
        file = open(filepath, "r")  # "r" para leer, "w" para escribir
        texto.insert("0.0", str(file.read()))  # leer el contenido del archivo y pegarlo en la caja de texto
        file.close()  # cerrar el archivo
    except FileNotFoundError:  # si cerraste la ventana o diste en cancelar
        print("No abriste ningun archivo")

# GUARDAR Y CREAR ARCHIVOS


def savefile():
    file = filedialog.asksaveasfile(title="Guardar archivo",  # abre ventana para crear/guardar el archivo
                                    defaultextension=".txt",  # extensión por default
                                    filetypes=[("Archivo de texto", "*.txt"),  # otras extensiones
                                               ("Archivo HTML", "*.html"),
                                               ("All files", "*.*")],
                                    initialdir=".\\")  # directorio del archivo actual
    try:
        file.write(str(texto.get("1.0", END)))  # obtengo el string de la ventana de texto y lo escribo en el archivo
        file.close()  # cierro el archivo
    except AttributeError:  # si cerraste la ventana o diste en cancelar
        print("No guardaste ningun archivo")


boton_abrir_archivo = Button(window,  # boton abrir archivo
                             text="Abrir archivo",
                             command=openfile)
boton_abrir_archivo.pack()

boton_guardar_archivo = Button(window,  # boton guardar archivo
                               text="Guardar texto en archivo",
                               command=savefile)
boton_guardar_archivo.pack()

# MENU DE PESTAÑAS SUPERIOR


def limpiartexto():
    texto.delete("0.0", END)  # Borro el contenido de la ventana texto


def copiartodo():
    messagebox.showinfo(title="Info", message="Texto copiado al portapapeles")


menubarra = Menu(window)
window.config(menu=menubarra)  # agrego el menu a la configuración de window
fileMenu = Menu(menubarra,  # creo la pestaña File y la asocio a menubarra (no a window)
                tearoff=False,
                font=("Tahoma", 10))  # tearoff es para sacar un separador inicial que me permite sacar la pestaña en una ventana nueva
menubarra.add_cascade(label="Inicio", menu=fileMenu)  # creo la cascada de File para poder acceder a el
fileMenu.add_command(label="Abrir archivo", command=openfile)  # creo el item Abrir archivo de la pestaña
fileMenu.add_command(label="Guardar archivo", command=savefile)  # creo el item Guardar archivo de la pestaña
fileMenu.add_separator()  # agrego un separador en la lista
exit_icon = PhotoImage(file=".\curso_12_exit.png").subsample(12)  # agrego un icono de Salir y lo achico x12 veces su tamaño
fileMenu.add_command(label="Salir",  # nombre
                     command=quit,  # comando quit
                     image=exit_icon,  # asocio un icono
                     compound="left")  # coloco el icono a la izquierda del texto

editMenu = Menu(menubarra,  # creo la pestaña File y la asocio a menubarra (no a window)
                tearoff=False,  # tearoff es para sacar un separador inicial que me permite sacar la pestaña en una ventana nueva
                font=("Tahoma", 10))  # fuente del texto
menubarra.add_cascade(label="Editar", menu=editMenu)  # creo la cascada de File para poder acceder a el
editMenu.add_command(label="Limpiar texto", command=limpiartexto)  # creo el item Abrir archivo de la pestaña
editMenu.add_separator()  # agrego un separador en la lista
editMenu.add_command(label="Copiar todo", command=copiartodo)  # creo el item Salir de la pestaña

window.mainloop()  # hace aparecer la ventana. siempre al final de la config

print("\n", end="")
