#Librerias
import math


#Solicitar informacion al usuario
proteina = float(input("Ingrese los gr de proteina:\n>"))
carboidratos = float(input("Ingrese los gr de carboidratos:\n>"))
grasa = float(input("Ingrese los gr de grasa:\n>"))

#Operaciones
calorias = 4 * (proteina + carboidratos) + 9 * grasa

#Resultados
print(f"Las calorias totales del producto son: {math.ceil(calorias)}")