class Auto:  # siempre empiezan con mayúscula

    ruedas = 4  # variable por default de una clase. Se puede ver y modificarse 

    def __init__(self, marca, modelo, año, color):  # constructor de la clase
        # atributos con variabes instanciadas al crear el objeto:
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color

    def drive(self):
        print("El auto", self.modelo, "está manejando")

    def stop(self):
        print("El auto", self.modelo, "está detenido")
