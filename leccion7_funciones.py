# Funcion --> bloque de código que tiene un nombre y se ejecuta cuando se invoca

#Ejemplo-1 

# def anima_usuario(nombre = 'Amigo'):
#     print(f'Hola {nombre}, ¡Que lindo día!')

# anima_usuario('Sergio')
# anima_usuario()

#Ejemplo-2
# def calcula_propina(cuenta):
#     propina = round(cuenta * 0.15, 2)
#     return print(f'La propina es {propina} dolares')

# calcula_propina(259.1)

#Ejemplo-3
calcula_propina2 = lambda cuenta: round(cuenta * 0.15) 
print(calcula_propina2(258))

