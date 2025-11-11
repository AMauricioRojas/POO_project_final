#Practica 3. Introducion al poliformismo
#Simular unn sistema de cobro de al menoa 4 opciones de pago

class pago_tarjeta:
    def procesar_pago(self,cantidad):
        return f"Procesando pago de ${cantidad} con tarjeta de debito/credito"

class pago_efectivo:
    def procesar_pago(self,cantidad):
        return f"Procesando pago de ${cantidad} en efectivo"

class pago_paypal:
    def procesar_pago(self,cantidad):
        nombre=input("ingresa tu nombre por favor para efectuar la operacion")

        return f"Procesando pago de{nombre}por la cantidad ${cantidad} con paypal"

class pago_transferencia:
    def procesar_pago(self,cantidad):
        comision=20
        cantidad=cantidad+comision
        return f"Procesando pago de ${cantidad} (20 comision) con transferencia"

metodos_pago =[pago_tarjeta(),pago_efectivo(),pago_paypal(),pago_transferencia()]

for m in metodos_pago:
    print(m.procesar_pago(500))

#ACTIVIDAD 1
#Procesar difrentes cantidades en cada opcon de pago:100 con tarjeta,400 con paypal,600con deposito y 5000 con...

Pago1=pago_efectivo()
pago2=pago_paypal()
pago3=pago_transferencia()
pago4=pago_tarjeta()

print(Pago1.procesar_pago(100))
print(pago2.procesar_pago(400))
print(pago3.procesar_pago(600))
print(pago4.procesar_pago(5000))

#Actividad 2. agregar funcionalidad adiccional a metodo proesar_pago( ) cuando sea deposito sumar 20 (comision) a cantidad
#caundo sea paypal, pedirle al usuario su nombre
print(pago2.procesar_pago(400))
print(pago3.procesar_pago(600))