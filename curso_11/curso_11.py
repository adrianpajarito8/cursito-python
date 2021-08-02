# CLASE 11 - CURSO DE 12HS
# GUIA COMPLETA DE TKINTER

from tkinter import *
import os
from typing import DefaultDict, List, Sized
os.system("cls")

# INTERFAZ GRÁFICA DE USUARIO O GUI

window = Tk()  # inicia una instancia de una ventana

# window.geometry("480x480")  # tamaño de la ventana
window.title("Pajarito APP")  # nombre de la ventana
# para acceder a los archivos en carpetas dentro del workspace escribimos de la siguiente manera:
icon_window = PhotoImage(file=".\curso_11\\morfeo.png")  # transformación de foto a icono
window.iconphoto(True, icon_window)  # icono de ventana
window.config(background="white")  # configuración general
icon_window = icon_window.subsample(5)  # resize de imagen x3

# ETIQUETAS
label = Label(window,  # creamos una plantilla para agregar imagen o texto
              text="Adrián C",  # texto
              font=("Arial", 30, "bold"),  # fuente
              fg="#00FF00",  # color de fuente
              bg="black",  # sombreado de texto
              relief=SUNKEN,  # encuadre de label
              bd=10,  # grosor de encuadre
              padx=50,  # espaciado x del encuadre
              pady=50,  # espaciado y del encuadre
              image=icon_window,  # agregado de imagen
              compound="bottom")  # posición de imagen
label.pack()  # se agrega la etiqueta a la ventana window
# label.place(x=240,y=240) #sirve como pack pero con coordenadas para ubicacion

# BOTONES
boton_color = 0
# creamos una función para la acción del boton


def click():
    global boton_color  # avisamos que trabajamos con la variable global
    if boton_color == 0:
        window.config(background="black")
        label.config(bg="white")
        boton_color = 1
    elif boton_color == 1:
        window.config(background="white")
        label.config(bg="black")
        boton_color = 0


boton = Button(window,  # creamos un boton
               text="CAMBIAR COLOR",  # texto del boton
               command=click,  # llama a la función click
               font=("Comic Sans", 20),  # fuente del boton
               fg="#000000",  # color de la fuente
               bg="white",  # sombreado del texto
               activeforeground="#FFFFFF",  # color fuente con click
               activebackground="black",  # color sombreado con click
               state=ACTIVE)  # tambien se puede agregar imagen y demas...
boton.pack()  # se agrega el boton a la ventana window

# ENTRY WIDGET

# Una aclaración IMPORTANTE. cuando creamos un widget sea Entry, Label, Button, etc...
# debemos agregar el .pack(), .grid() o .place() en una nueva linea ya que
# si instaciamos estos métodos al momento de crear el widget (misma linea)
# no podremos acceder a los métodos como .get() o .delete() en funciones externas.
# De pasarlo en la misma línea, el tipo será un None ya que el return del
# Entry (por ejemplo) sería "entry" y no una instancia del "tkinter.entry"
# De querer hacerlo en la misma linea debemos crear una variable global como
# boton_global=StringVar() y agregar Entry(window,...,textvariable=entry_global)
# y luego llamar a los métodos en la "def" como entry_global.get() o entry_global.delete()

def print_entry():
    print(entry.get())  # print entry en terminal
    entry.delete(0, END)  # borra el texto en la casilla
    # los argumentos ndican que se borra desde el incio 0 hasta el final END


# Entry nos da una ventana de texto para escribir en window
entry = Entry(window,
              font=("Arial", 14),
              bg="Light Gray",
              relief=SUNKEN,
              bd=2)
# algunas otras configuraciones del entry:
# entry.config(show="*") # para ocultar caracteres como para contraseñas
# entry.insert(0,"Escribi aca:") # para poner texto por default
# entry.config(state=DISABLED) # desactiva la casilla
entry.pack()  # pack del entry

boton_entry = Button(window,
                     command=print_entry,
                     text="Print Entry")
boton_entry.pack()  # pack del boton para printear y borrar

# CHECK BOXES O CAJAS DE SELECCIÓN (SELECCIÓN MULTIPLE)

x = BooleanVar()  # inicializar la variable para el Check Button
# x = StringVar() # otra opción. Lo mejor es booleano


def display():
    if(x.get()):
        print("Estas de acuerdo")
    elif(not x.get()):
        print("No estas de acuerdo")


caja_check = Checkbutton(window,  # ventana donde insertarlo
                         text="Estoy de acuerdo",  # texto de la casilla
                         variable=x,  # variable a modificar
                         onvalue=True,  # estado de x cuando se marca la casilla
                         offvalue=False,  # estado de x cuando se desmarca
                         bg="white",
                         command=display,
                         pady=10)
caja_check.pack()

# RADIO BUTTON O BOTONES RADIALES (SELECCIÓN UNICA)


comida = ["Pizza", "Hamburguesa", "Pancho"]
y = IntVar()


def seleccion():
    print("Presionaste:", comida[y.get()])


for index in range(len(comida)):
    caja_radial = Radiobutton(window,  # ventana donde insertarlo
                              text=comida[index],  # añade texto a cada boton
                              bg="lightblue",  # color de fondo
                              variable=y,  # variable a modificar con selección
                              value=index,  # valor de la variable segun selección
                              command=seleccion,  # acción a realizar
                              indicatoron=0,  # cambia los circulos por botones (probar =0)
                              font=("Impact", 14),  # fuente
                              width=20,
                              pady=5)  # ancho del fondo
    caja_radial.pack()

# SCALE PARA SLIDER O FADER


def temperatura():
    print("La temperatura es:", fader.get(), "°C")


fader = Scale(window,
              from_=0,  # valor desde (fijarse en el guion bajo)
              to=50,  # valor hasta
              length=400,  # longiutd del fader
              tickinterval=10,  # cada cuando mostrar la escala
              orient=HORIZONTAL,  # orientación del fader
              resolution=0.2,  # resolución del fader
              troughcolor="lightblue")  # color de fondo del fader
fader.set(23)  # set inicial a 23
fader.pack()  # hacer aparecer el fader
# print(fader["length"])  # obtener información del fader con palabras clave

# boton para mostrar la temperatura
boton_temperatura = Button(window,
                           command=temperatura,
                           text="Display Temp")
boton_temperatura.pack()

# LISTBOX


def submit_lista():  # función para printear item seleccionado en listbox
    food = []  # inicializo food
    if listbox.curselection():  # detecta si hay elemento/s seleccionados
        for index in listbox.curselection():  # recorro la lista
            food.insert(index, listbox.get(index))  # inserto en el auxilar food
        print("Ordenaste las siguientes comidas:")
        for index in food:
            print(index)  # print food
    else:
        print("No seleccionaste nada")


def add_lista():  # función para añadir item a la listbox
    if entry.get():
        listbox.insert(listbox.size(), entry.get())
    # listbox.config(height=listbox.size()) #la altura se ajusta a la cantidad de itemos


listbox = Listbox(window,  # agrego una listbox a window
                  bg="#f7ffde",  # color de fondo
                  font=("Constantia", 20),
                  selectmode=MULTIPLE)  # fuente y tamaño

scrollbar = Scrollbar(window)  # creo scrollbar para listbox
scrollbar.pack(side=RIGHT, fill=Y)  # lo pongo a la derecha y el tamaño del alto de la listbox
scrollbar.config(command=listbox.yview)  # lo configuro para que mueva la listbox como command
listbox.pack()  # muestro la lista

listbox.insert(1, "Pizza")  # items de la lista
listbox.insert(2, "Milanesa")
listbox.insert(3, "Asado")
listbox.insert(4, "Hamburguesa")
listbox.insert(5, "Pan de ajo")

listbox.config(height=listbox.size(), yscrollcommand=scrollbar.set)  # la altura se ajusta a la cantidad de items y linkeo el scrolly a la scrollbar

boton_lista = Button(window, text="Print", command=submit_lista)  # boton submit seleccion
boton_lista.pack()
boton_agregar = Button(window, text="Agregar", command=add_lista)  # boton add item
boton_agregar.pack()


window.mainloop()  # hace aparecer la ventana. siempre al final de la config

print("\n", end="")
