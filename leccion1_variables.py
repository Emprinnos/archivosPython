#Ejemplo de un comentario en Python

"""
Ejemplo de un comentario en Python
que tiene varias lineas.
"""

# Una VARIABLE es un contenedor en la memoria que guarda datos

# Reglas para Nombrar una Variable

# 1. No puede empezar con un digito
# 2. Puede empezar con una letra o guion bajo
# 3. Para nombres complejos se usa el guion bajo (user_name)
# 4. El tamaño de la letra tiene importancia (USUARIO es diferente a usuario)

#cadenas
nombre = "Juan"
print(type(nombre)) #str

#numero enteros
edad = 26 #int
#numeros decimales
puntaje_promedio = 85.3
print(type(puntaje_promedio))

#boolean
es_estudiante = True
print(type(es_estudiante))

#Asignacion multiple

nombre_cliente, venta, es_importante = ('Sergio', 2500.85, True)
print(nombre_cliente)


#Cambio de tipo de dato (CASTING)

x = str(8.1)
print(type(x))
print(x)

# Operaciones básicas

propina = (85 * 0.15)/3
print(propina)


#Uso de f-strings

print('Mi nombre es: ' + nombre_cliente + 'y mi venta es de: ' + str(venta))

print(f'Mi nombre es {nombre_cliente} y mi venta es de {venta}')