# En Python una lista es una coleccion de valores
# ordenada que se puede cambiar (parecido a los ARRAYS en otros lenguajes de programacion)

#Ejemplo de Lista
carros = ['Ford Mustang', 'Toyota Corolla', 'Honda Accord', 'Fiat 500']

# Otra forma de crear una lista
menu = list(('Pollo a la braza', 'Lomo saltado', 'Anticuchos'))


# Acceder un elemento de la lista
# print(carros[0])
# print(carros[1])
# print(carros[-1])


#append() agrega al final de la lista
# carros.append('Mini Cooper')
# print(carros)


#insert() agrega en una posicion especificada
# carros.insert(1, 'Dodge Charger')
# print(carros)

#cambiar el valor
# carros[0] = 'Camaro'
# print(carros)

# remove() saca el elemento
# carros.remove('Camaro')

#pop() retorna el elemento sacado
# print(carros)
# print(carros.pop(1))
# print(carros)


#ordenar la lista
# carros.sort()
# print(carros)
# #ordenar al reves
# carros.sort(reverse=True)
# print(carros)



#TUPLES

#Un tuple es una colleccion de valores ordenada que NO SE PUEDE CAMBIAR (puede tener elementos REPETIDOS)

#Crear un tuple
distribuciones = ('Manjaro', 'Ubuntu', 'Pop OS')

#Otra forma de crear un tuple
lenguajes = tuple(('JS', 'Python', 'C++'))
# print(lenguajes)
#Acceder a un elemento

# print(distribuciones[1])

# len() longitud del tuple
# print(len(distribuciones))
# print(len(carros))

# del se usa para borrar un tuple
# del lenguajes



#Set es una coleccion de valores desordenados, SIN INDICE Y SIN VALORES REPETIDOS

frameworks = {'Vue', 'Angular', 'Svelte'}


#add() agrega un elemento al set
frameworks.add('React')
print(frameworks)

#remove() saca un elemento del set
frameworks.remove('React')
print(frameworks)

#clear()
# frameworks.clear()
# print(frameworks)
# del para borrar el set
del frameworks



