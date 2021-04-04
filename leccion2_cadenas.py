
#Una cadena es una secuencia de carácteres incluidos entre comillas (simple o doble)

cadena = 'estamos aprendiendo python3'

#1 len() se usa para determinar la longitud de una cadena


# print(len(cadena))


#2 replace() se usa para reemplazar una cadena

# print(cadena.replace('aprendiendo', 'practicando'))

#3 upper() cambia las letras a mayuscula

# print(cadena.upper())

#4 lower() cambia las letras a minuscula

# print(cadena.lower())

#5 capitalize() cambia la primera letra a mayuscula

# print(cadena.capitalize())

#6 isnumeric() chequea si la cadena es numerica
# cadena_numerica = '256'
# print(cadena_numerica.isnumeric())

#7 isalpha() chequea si la cadena tiene solamente letras

# print(cadena.isalpha())

#8 isalnum() chequea si la cadena tiene letras y digitos

# print(cadena.isalnum())

#9 split() separa la cadena en una lista

# print(cadena.split())

#10 count() cuenta cuantas veces aparece una cadena

# print(cadena.count('e'))

#11 startswith() endswith() retorna true o false si la cadena empieza (termina)
#con la cadena especificada

# print(cadena.endswith('e'))

#12 find() encuentra la posicion del caracter especificado

# print(cadena.find('python3'))