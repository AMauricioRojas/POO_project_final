# Practica 2. Clases, Objetos, métodos y atributos

class persona:
    # Constructor de la clase
    def __init__(self, nombre, apellido, edad):
        # Creación de atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        # Doble guion bajo antes del nombre del atributo es que es un atributo privado
        self.__cuenta = None

    def asignar_cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ahora tiene una cuenta bancaria ")

    def consultar_saldo(self):
        if self.__cuenta:
            # aquí faltaban los paréntesis en mostrar_saldo
            print(f"El saldo de {self.nombre} es $ {self.__cuenta.mostrar_saldo()}")
        else:
            print(f"{self.nombre} no tiene cuenta bancaria")

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre}, mi apellido es {self.apellido} y tengo {self.edad} años.")

    def cumpleaños(self):
        self.edad += 1
        print(f"Feliz cumpleaños {self.nombre}, ahora tienes {self.edad} años.")


class cuenta_bancaria:
    # Se llamaba __int__, debe ser __init__
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.__saldo = saldo  # atributo privado

    def mostrar_saldo(self):
        return self.__saldo

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Se ha depositado {monto}, el nuevo saldo es {self.__saldo}")
        else:
            print("El monto a depositar debe ser positivo")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se ha retirado {cantidad}, el nuevo saldo es {self.__saldo}")
        else:
            print("El monto a retirar debe ser positivo y no puede exceder el saldo disponible")


# Creación de un objeto o instancia de la clase persona
estudiante1 = persona("Angel", "Rojas", 19)

cuenta1 = cuenta_bancaria("123456789", 1000)

estudiante1.asignar_cuenta(cuenta1)
estudiante1.presentarse()
estudiante1.cumpleaños()
estudiante1.consultar_saldo()
cuenta1.depositar(3900)

# Ejercicio 1
# Crea una clase, objeto, mínimo 3 atributos y mínimo 3 métodos distintos, al menos uno con operación matemática

class banco:
    # Constructor de la clase
    def __init__(self, nombre, calle, capacidad):
        # Creación de atributos
        self.nombre = nombre
        self.calle = calle
        self.capacidad = capacidad

    def ubicacion(self):
        print(f"Hola, bienvenido a {self.nombre}, la calle donde nos encontramos es {self.calle} "
            f"y mi capacidad máxima es de {self.capacidad} personas.")

    def aumentar_capacidad(self, cantidad):
        self.capacidad += cantidad
        print(f"Se ha aumentado la capacidad de {self.nombre}, ahora tenemos capacidad total de {self.capacidad} personas.")

    def reducir_capacidad(self, cantidad):
        self.capacidad -= cantidad
        print(f"Han salido algunas personas de {self.nombre}, ahora tenemos capacidad de {self.capacidad} personas.")


# Creación de un objeto o instancia de la clase banco
banco1 = banco("BBVA", "Calle Nuevo Porvenir #221", 750)
banco1.ubicacion()
banco1.aumentar_capacidad(10)
banco1.reducir_capacidad(5)
