#Practica 4. Herencia

class ticket:
    def __init__(self,id,tipo,prioridad):
        self.id=id
        self.tipo=tipo
        self.prioridad=prioridad
        self.estado="Pendiente"

ticket1=ticket(1,"Incidente","Alta")
print(f"El ticket {ticket1.id} es de tipo {ticket1.tipo} con prioridad {ticket1.prioridad} y su estado es {ticket1.estado}")

ticket2=ticket(2,"Requerimiento","Media")
print(f"El ticket {ticket2.id} es de tipo {ticket2.tipo} con prioridad {ticket2.prioridad} y su estado es {ticket2.estado}")



class empleado:
    def __init__(self,nombre):
        self.nombre=nombre
    def trabajar_in_ticket(self,ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")

class desarrollador(empleado):
    def trabajar_in_ticket(self,ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")
        if ticket.tipo=="Software":
            ticket.estado="resuelto"
            print(f"El ticket {ticket.id} ha sido resuelto por el desarrollador {self.nombre}")
        else:
            print(f"El ticket {ticket.id} no puede ser resuelto por el desarrollador {self.nombre}")

class tester(empleado):
    def trabajar_in_ticket(self,ticket):
        print(f"El empleado {self.nombre} revisa el ticket {ticket.id}")
        if ticket.tipo=="Prueba":
            ticket.estado="resuelto"
            print(f"El ticket {ticket.id} ha sido resuelto por el tester {self.nombre}")
        else:
            print(f"El ticket {ticket.id} no puede ser resuelto por el tester {self.nombre}")
