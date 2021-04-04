#Python es un lenguaje de programacion orientado a objetos
#La clase es una categoria general que se usa para crear objetos (instancias especificas de esta clase)

class Empleado:
    #constructor
    #__init__ es un metodo que se invoca cuando se crea una clase y permite inicializar los atributos de la clase
    #self es una referencia a la instancia actual de la clase
    #el proposito es poder acceder a las variables de la clase

    def __init__(self, nombre, pago, horas): 
        self.nombre = nombre
        self.pago = pago
        self.horas = horas

    
    #metodos
    def calcula_sueldo(self):
        return self.pago * self.horas



    
#Extendemos la clase
class Interino(Empleado):
    # pass
    def __init__(self, nombre, pago, horas):
        Empleado.__init__(self, nombre, pago, horas)
        self.nombre = nombre
        self.pago = pago
        self.horas = horas
        self.ajuste = 0.75
    

    def ajusta_sueldo(self):
        return self.pago * self.horas * self.ajuste


#Creamos un objeto de tipo Empleado
empleado_01 = Empleado('Jose', 25, 40)

print(empleado_01.calcula_sueldo())

#Creamos un objeto de tipo Interino

empleado_02 = Interino('Sergio', 25, 20)
print(empleado_02.ajusta_sueldo())

