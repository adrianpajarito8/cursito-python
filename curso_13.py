# CLASE 13 - CURSO DE 12HS
# GUIA COMPLETA DE TKINTER

import os
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import time
import threading
os.system("cls")


window = Tk()
window.title("Pajarito APP 3")
height = "300"
width = "300"
# window.geometry(height + "x" + width)  # tamaño de la ventana
window.config(background="white")  # configuración general

# FRAMES EN TKINTER
""" 
frame = Frame(window,  # frame al window
              relief=SUNKEN,  # modo relieve
              width=200,
              height=200)  # grosor del relieve
frame.pack()
frame.update()
frame.place(x=int(width) / 2 - frame.winfo_width() / 2, y=100)  # posición del frame en window

# agregarmos los botones al frame
boton_w = Button(frame, text="W", width=3).pack(side=TOP)
boton_a = Button(frame, text="A", width=3).pack(side=LEFT)
boton_s = Button(frame, text="S", width=3).pack(side=LEFT)
boton_d = Button(frame, text="D", width=3).pack(side=LEFT)


# NUEVAS VENTANAS

def crear_top_window():  # crea ventana sobre otras ventanas
    new_top_window = Toplevel()  # crear ventana hijo. si se cierra la ventana padre se cierra esta tambien


def crear_individual_window():  # crea ventana sobre otras ventanas
    new_individual_window = Tk()  # crear ventana hijo. si se cierra la ventana padre se cierra esta tambien
    window.destroy()


b1 = Button(window,
            text="Crear nueva ventana top",
            command=crear_top_window).pack()
b2 = Button(window,
            text="Crear nueva ventana independiente",
            command=crear_individual_window).pack()


# PESTAÑAS

# importar from tkinter import ttk
# este módulo se debe importar antes que el from tkinter import *
# para no sumprimir los módulos tk con los ttk. De colocarlo luego
# los módulos tk se sobreescribiran con los ttk y deberemos usar
# comandos como ttk.style(). Si esto es lo que se desea, se debe
# importar tkinter y luego importar ttk.

notebook = ttk.Notebook(window)  # widget que administra pestañas

tab1 = Frame(notebook)  # crear un frame para tab 1
tab2 = Frame(notebook)  # crear un frame para tab 2
notebook.add(tab1, text="Tab 1")  # agregar el tab 1 a notebook
notebook.add(tab2, text="Tab 2")  # agregar el tab 1 a notebook
notebook.pack(expand=True,  # expandirse para usar todo el espacio no usado (centrarse)
              fill=BOTH)  # puede ser X,Y o BOTH. Es para rellenar toda la pantalla posible
label1 = Label(tab1, text="Este es el tab 1", height=20, width=50).pack()
label2 = Label(tab2, text="Este es el tab 2", height=20, width=50).pack()
 """

# GRID GEOMETRIA
""" 
# creamos una grilla donde colocaremos nuestros widgets


titulo_label = Label(window,
                     text="Ingresa tu información",
                     font=("Courier New", 20),
                     background="lightgreen")
                     
titulo_label.grid(row=0, column=0, columnspan=2)

primernombre_label = Label(window,
                           width=15,
                           text="Primer Nombre:",
                           background="white")
primernombre_label.grid(row=1, column=0)

segundonombre_label = Label(window,
                            text="Segundo Nombre:",
                            background="white")
segundonombre_label.grid(row=2, column=0)

apellido_label = Label(window,
                       text="Apellido:",
                       background="white")
apellido_label.grid(row=3, column=0)


def printear():
    print("Hola. Buen día", primernombre_entry_global.get(), segundonombre_entry.get(), apellido_entry.get())


primernombre_entry_global = StringVar()
primernombre_entry = Entry(window,
                           width=30,
                           textvariable=primernombre_entry_global).grid(row=1, column=1)
# textvariable nos permite asignar un valor a nuestro entrybox para
# obtener los métodos de este widget (como .get() o .delete() cuando
# instanciamos, en este caso el método .grid(), en la misma linea.
# si lo asignamos en la misma linea y queremos llamar al
# primernombre_entry.get() no dará error o type None.

segundonombre_entry = Entry(window,
                            width=30)
segundonombre_entry.grid(row=2, column=1)

apellido_entry = Entry(window,
                       width=30)
apellido_entry.grid(row=3, column=1)

submit_button = Button(window,
                       text="Saludar",
                       command=printear)
submit_button.grid(row=4, column=0, columnspan=2)

# Columnspan toma las siguientes "2" columnas desde su posición (incluida)
# y las une. De esta forma el boton queda centrado entre las 2 columnas
 """
# PROGRESSBAR
""" 
# importar from tkinter.ttk import *
# importar import time

porcentaje = StringVar()
porcentaje.set("0%")


def download():
    tareas = 100
    x = 0
    speed=1
    while(x < tareas):
        time.sleep(0.05)
        bar['value'] += (speed/tareas)*100
        x += speed
        porcentaje.set(str(int((x / tareas) * 100)) + "%")
        window.update_idletasks()
    porcentaje.set("Finish")
    time.sleep(1)
    print("Se terminó de descargar. Programa terminado")
    window.destroy()


bar = Progressbar(window,
                  orient=HORIZONTAL,
                  length=300)
bar.grid(pady=10, padx=10)

porcentaje_label = Label(window, textvariable=porcentaje).grid()

# creo un hilo para la carga de la progressbar asi puedo mover la window
# o interactuar con ella mientras se carga la barra
a = threading.Thread(target=download, args=(), name="download", daemon=True)

boton_progressbar = Button(window,
                           text="Download",
                           command=lambda: a.start())
boton_progressbar.grid()

# probar apretar el boton hola mientras se carga la barra. Sería imposible
# de no haber cargado la barra el el thread extra
boton_extra = Button(window,
                     text="Extra",
                     command=lambda: print("Hola"))
boton_extra.grid()
 """

# CANVAS
""" 
# un canvas es una zona creadoa especificamente para gráfico y dibujos
canvas = Canvas(window,
                height=500,
                width=500,
                bg="white")
canvas.pack()
# escribimos el update para que se escriban los valores canvas.winfo_width()
# y canvas.winfo_height(). El update debe ir siempre luego del pack()
canvas.update()
# creamos una linea desde 0,0 hasta el width,height del canvas
linea_azul = canvas.create_line(0,
                                0,
                                canvas.winfo_width(),
                                canvas.winfo_height(),
                                fill="blue",
                                width=4)
# creamos otra linea cruzada
linea_roja = canvas.create_line(0,
                                canvas.winfo_height(),
                                canvas.winfo_width(),
                                0,
                                fill="red",
                                width=4)
# creamos un rectangulo desde 50,50 hasta 250,250
cuadrado_verde = canvas.create_rectangle(50,
                                         50,
                                         250,
                                         250,
                                         fill="green")
# creamos un poligono con coordenadas (x1,y1,x2,y2,x3,y3,...)
points = [250, 500, 375, 250, 500, 500]
poligono_rosado = canvas.create_polygon(points,
                                        fill="pink",  # relleno vacío significa transparente
                                        outline="black",  # linea contorno
                                        width=3)  # grosor del contorno
# creamos un arco como (x1,y1,x2,y2,...)
# que son las coordenadas de los puntos superior izquierdo
# e inferior derecho del cuadrado que circunscribe al circulo del cual
# se dibuja el arco
arco_negro = canvas.create_arc(0,
                               0,
                               500,
                               500,
                               fill="black",
                               style=PIESLICE, #PIESLICE, CHORD o ARC
                               start=200, #inicio antihorario
                               extent=30) #extender luego del inicio
 """

# EVENTOS ACTIVADOS POR TECLADO
""" 
# creamos la función para capturar los eventos


def printear_escape(event):
    if event.keysym == "Escape":
        print("Terminaste el programa (Esc)")  # event.keysym obtiene la letra que activó el evento
        window.destroy()


def printear_cualquier_tecla(event):
    if event.keysym is not "Escape":
        print("Apretaste:", event.keysym)


# bind sirve para unir un evento a una acción o función
# siempre colocar los simbolos <*> entre el nombre de la tecla
# que especifiquemos
window.bind("<Escape>", printear_escape)
# Si queremos capturar cualquier tecla, escribimos "<Key>"
window.bind("<Key>", printear_cualquier_tecla)
 """

# EVENTOS ACTIVADOS POR MOUSE
""" 

def movimiento_mouse1(event):
    # capturamos la coordenada x e y del mouse en la ventana
    print("Hiciste un click en coord:", str(event.x) + "," + str(event.x))


window.bind("<Button-1>",movimiento_mouse1) #Boton izquierdo
window.bind("<Button-2>", movimiento_mouse1)  # Boton de rueda del mouse
window.bind("<Button-3>", movimiento_mouse1)  # Boton derecho
window.bind("<ButtonRelease>", movimiento_mouse1)  # Soltar boton
window.bind("<Enter>", movimiento_mouse1)  # Meter el puntero en la ventana
window.bind("<Leave>", movimiento_mouse1)  # Sacar el puntero de la ventana
window.bind("<B1-Motion>", movimiento_mouse1)  # Movimiento del mouse con click apretado
#window.bind("<Motion>", movimiento_mouse1)  # Activa evento cada vez que movemos el mouse dentro de la ventana
 """

# MOVER FIGURAS EN EL CANVAS

""" 
def drag_start(event):
    widget=event.widget
    #guardamos las coordenadas de inicio
    widget.startX = event.x
    widget.startY = event.y


def drag_motion(event):
    widget=event.widget
    #x=posición superior izquierda del cuadrado-posición del click+posición del movimiento del mouse
    x = widget.winfo_x() + event.x - widget.startX 
    y = widget.winfo_y() + event.y - widget.startY 
    widget.place(x=x,y=y)

#la función event.widget nos permite referenciarnos al widget
#del evento con el que estamos tratando. Muy util cuando tenemos
#mas de un widget como en este caso.

#label 1
label1 = Label(window, bg="red", width=10, height=5)
label1.place(x=0, y=0)

label1.bind("<Button-1>", drag_start)
label1.bind("<B1-Motion>", drag_motion)

#label 2
label2 = Button(window, bg="blue", width=10, height=5)
label2.place(x=100, y=100)
label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)
 """


window.mainloop()
print("\n", end="")
