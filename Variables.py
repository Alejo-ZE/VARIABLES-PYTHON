from mailbox import NoSuchMailboxError
from unicodedata import decimal

#Mostrar valor de las variables
texto = "Master en python"
texto2 = "Alejandro Zapata"
numero = 45
decimal = 6.7

print (texto)
print (texto2)
print (numero)
print (decimal)

print("-------------------------------------------------------------")

#Sustituir el valor de algunas variables / reasignado de valores
numero = 77
decimal = 8.9
print (numero)
print (decimal)

print("-------------------------------------------------------------")

#Concatenar
nombre = "Alejandro"
apellidos = "Zapata"
web = "Ermita de las Aves"

print (nombre + " " + apellidos + " - " + web)
print (f"{nombre} {apellidos} - {web}")
print ("hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))


