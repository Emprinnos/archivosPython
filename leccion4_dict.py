# Dict se usan para guardar datos de tipo clave-valor
# Coleccion ordenada, cambiable, sin valores repitidos 

# Ejemplo de dict

carro = {
    'modelo': 'Ford Mustang',
    'potencia': 300,
    'produccion': '2014'
}

#Acceder a los valores del dict

print(carro['modelo'])
print(carro['produccion'])

# keys() para acceder a las claves
# print(carro.keys())

# items() para acceder a los datos
# print(carro.items())

# len() 
print(len(carro))

#sacar un elemento

# print(carro.pop('produccion'))
# print(carro)
# del carro['produccion']
# print(carro)

#copy() para copiar un dict

carro_nuevo = carro.copy()
print(carro_nuevo)

#sacar todos los datos
carro.clear()
print(carro)