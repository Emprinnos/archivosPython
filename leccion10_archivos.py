import os

#Crear un archivo
archivo = open('ejemplo.txt', 'w')
#'x' create--> crea un archivo, genera un error si ya existe
#'w' write--> crea un archivo si no existe
#'a' append --> crea un archivo si no existe


#Escribir en un archivo
archivo.write('Estamos aprendiendo como manejar los archivos en Python3.')
archivo.close()


#Editar un archivo
archivo = open('ejemplo.txt', 'a')
archivo.write(' Estamos en la ultima leccion del Python3.')
archivo.close()

#Leer del archivo
archivo = open('ejemplo.txt', 'r')
print(archivo.read())
archivo.close()

#Borrar un archivo
# os.remove('ejemplo.txt')