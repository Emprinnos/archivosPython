#Un módulo es un archivo que contiene un set de definiciones y declaraciones que se pueden incluir en la aplicacion


#ejemplo Modulo math
# import math
from math import floor


# x = math.floor(3.257)
y = floor(3.257)
# print(x)
print(y)


#El manejador de paquetes en Python se llama Pip

from email_validator import validate_email, EmailNotValidError


email = 'pruebaemail@yahoo.com'

try:
  valid = validate_email(email)
  email = valid.email
except EmailNotValidError as e:
  print(str(e))
