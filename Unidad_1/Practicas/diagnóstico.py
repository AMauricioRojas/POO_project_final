#PRACTICA DE PRUEBA
#Practica diagnostico_Angel_Mauricio
#Simulador de ticket de venta 
#Objetivo: Aplica funciones, bucles, condiciones, listas y variables

#Ferretería que vende productos
import os
os.system("cls")
productos = ["Dado 1/4", "Llave", "Tuerca 1/2"]
precios   = [80, 70, 20]

def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] * precios[i]
    return total

print("Bienvenido a la ferretería")
nombre = input("Ingrese su nombre: ")

cantidades = []
print("Ingrese la cantidad de productos que desea comprar:")
for i in range(len(productos)):
    print(f"{i+1}. {productos[i]} - ${precios[i]}")
    cantidad = int(input("Cantidad: "))
    cantidades.append(cantidad)

total = calcular_total(cantidades, precios)

# Imprimir ticket
print("\n-----ICKET DE COMPRA ------")
print(f"Cliente: {nombre}\n")
for i in range(len(productos)):
    if cantidades[i] > 0:
        print(f"{productos[i]} x{cantidades[i]}  = ${cantidades[i]*precios[i]}")

print(f"TOTAL: ${total}")
print("¡Gracias por su compra!")
