# CLASE 3 - CURSO DE 12HS
# LISTAS, LISTAS +1D, TUPLAS, SETS, DICCIONARIOS, INDEXADOR

# LISTAS
""" 
# Los corchetes indican que es una lista
food = ["pizza", "hamburgesa", "asado", "pasta"]
print(food)  # imprime la lista
print(food[0])  # imprime el primer elemento de la lista
food[0] = "milanesa"  # reemplazo pizza por milanesa
print(food[0])

print("\nLa comida de la lista es:")
for x in food:
    print(x)

food.append("helado")  # Agrega al final de la lista
food.remove("pasta")  # Remueve de la lista
food.pop()  # elimina el ultimo elemento de la lista
# inserta un elemento en la posición indicada y desplaza los demás a la derecha desde esa posición
food.insert(1, "pizza")
food.sort(reverse=0)  # ordena de mayor a menor, con reverse=1 de mayor a menor
print(food)
food.clear()  # limpia la lista
 """

# LISTAS MULTIDIMENSIONALES
""" 
drinks = ["agua", "café", "vino", "cerveza"]
cena = ["milanesa", "fideos", "panchos"]
postre = ["helado", "flan", "fruta"]

food = [drinks, cena, postre]  # Esta es una lista 2D
print(food) # el primer 1 indica "cena" y el segundo 1 indica el indice 1 de cena que es "fideos"
print(food[1][1]) 
"""

# TUPLAS Y SUS MÉTODOS
""" 
# Se diferencia de las listas ya que es una lista ordenada e inmodificable. Se usa para agrupar datos constantes y consultarlos
estudiante = ("Adrián", 21, "hombre")

print(estudiante.count(Nombre))
print(estudiante.index("hombre"))
 """

# SET
""" 
# Colección como lista o tuplas pero no está indexada y tampoco ordenada. Los elementos duplicados solo se ver una sola vez en un print

herramientas = {"martillo", "serrucho", "pala", "destornillador", "martillo"}

for x in herramientas:  # cada print tira el set en distinto orden
    print(x)  # observar que martillo se printea solo una vez

herramientas.add("zapa")  # agrega zapa
herramientas.remove("serrucho")  # elimina serrucho
herramientas.clear()  # elimina todo

maquinas = {"taladro", "moladora", "caladora"}
# update agrega todos los items de máquinas en el set de herramientas
herramientas.update(maquinas)
# union crea un nuevo set con los otros dos unidos
todo_junto = herramientas.union(maquinas)
# difference muestra elementos que "herramientas" NO tiene en común con "máquinas"
print("\n", herramientas.difference(maquinas))
# intersection muestra elementos que "herramientas" SI tiene en común con "máquinas"
print("\n", herramientas.intersection(maquinas))
 """

# DICCIONARIOS
""" 
# Los diccionarios se diferencian de los sets ya que cada elemento está asociado a un nombre clave

capitales = {"Argentina": "Buenos Aires",
             "Rusia": "Moscú",
             "China": "Beijing"}

# Usando get e indicando la clave, se printea el valor asociado
# Se usa get para poder devolver None en caso de que la clave no exista y el programa no tire error
print(capitales.get("China"))
print(capitales.keys())  # solo las claves
print(capitales.values())  # solo los valores
print(capitales.items())  # el diccionario entero
# agrega un para clave:valor nuevo. Si exite, lo reemplaza
capitales.update({"Alemania": "Berlin"})

for key, value in capitales.items():
    print(key+":", value)

capitales.pop("China")  # para eliminar una clave con su valor
capitales.clear()  # elimina todo dentro pero no el diccionario 
"""

# OPERADOR INDEXADOR O INDICADOR
""" 
nombre = "adrian nicolas cantaloube"
if(nombre[0].islower()):  # pregunta si el índice 0 del string es minúscula
    nombre = nombre.capitalize()  # capitaliza el índice 0 del string
    nombre = nombre.title()  # capitaliza todas las palabras del string
print(nombre)

# vuelvo minúscula el primer nombre y lo guardo
primer_nombre = nombre[:6].lower()
print(primer_nombre)
 """