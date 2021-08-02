# CLASE 2 - CURSO DE 12HS
# IF, OPERADORES LÓGICOS, WHILE, FOR, FOR NEST Y LOOP CONTROL

# SENTINCIA IF
""" 
edad = int(input("Introduce tu edad: "))

if edad == 100:
    print("Sos persona de riesgo")
elif edad >= 18:
    print("Sos un adulto")
elif edad < 0:
    print("La edad es incorrecta")
else:
    print("Sos un menor")
 """

# OPERADORES LÓGICOS
""" 
temperatura = int(input("Indique la temperatura:"))

if temperatura >= 10 and temperatura <= 40:  # AND
    print("Está piola para salir")
elif temperatura > 40 or temperatura <= 9:  # OR
    print("Estas creisi, ni salgas")

agradable = not(True)  # NOT
print(agradable)
 """

# SENTENCIA WHILE LOOP
""" 
nombre = None

while not nombre:
    nombre = input("Ingrese su nombre:")

print("Hola", nombre)
 """

# SENTENCIA FOR
""" 
import time
for i in range(10):  # printear 0 al 9. Tambien sirve para strings
    print(i)

for i in range(50, 100):  # printear 50 al 99
    print(i)

for i in range(50, 80, 2):  # printear cada 2 valores
    print(i)

for seconds in range(10, 0, -1):  # printear cuenta regresiva
    print(seconds)
    time.sleep(1)  # delay en segundos
 """

# NESTED LOOPS
""" 
rows = int(input("how many rows?:"))
columns = int(input("how many columns?"))
symbol = input("enter a symol:")

for i in range(rows):
    for j in range(columns):
        # el end hace que el print salga al terminar el loop para printear todo en una misma linea
        print(symbol, end="")
    print()
 """

# LOOP CONTROL STATEMENTS
""" 
break: to terminate the loop
continue: to skip to the next iteration
pass: to act like a placeholder

while True:
    name = input("Enter your name: ")
    if name != "":
        break  # termina el while cuando pones el nombre

phone_number = "261 600-6018"
for i in phone_number:
    if i == "-" or i == " ":
        continue  # salta a la otra iteración y no codea lo que esta debajo de el, en este caso, el print
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass  # basicamente no hace nada -_-
    else:
        print(i)
 """