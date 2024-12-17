#Una tienda vende manzanas y naranjas. El precio de una manzana es de $1.20 y el precio de una naranja es de $0.80. Un cliente quiere comprar 10 manzanas y 15 naranjas. Queremos saber:
#1. ¿El cliente gasta más en manzanas que en naranjas?
#2. ¿Cuántas manzanas necesita comprar el cliente para gastar lo mismo que en 15 naranjas?
#3. ¿Es cierto que comprar 3 manzanas y 2 naranjas cuesta lo mismo que comprar 4 manzanas?
#4. ¿Es cierto que el costo de 10 manzanas es mayor que el de 8 manzanas y menor que el de 12 manzanas?
#5. ¿El costo de 10 manzanas o 15 naranjas es mayor que $20?
#6. ¿Es cierto que el costo de 10 manzanas es mayor que el de 15 naranjas o el costo de 5 manzanas es mayor que el de 10 naranjas pero no ambos?

# Precio
precio_manzana = 1.20
precio_naranja = 0.80

# Cantidad de naranjas y calculo del precio
cantidad_manzanas = 10
cantidad_naranjas = 15

costo_manzanas = precio_manzana * cantidad_manzanas
costo_naranjas = precio_naranja * cantidad_naranjas

#1. ¿El cliente gasta más en manzanas que en naranjas?
# Pregunta
print("#1. ¿El cliente gasta más en manzanas que en naranjas?:")
# Resultado
print(costo_manzanas > costo_naranjas)
print("________________________________________________________________________________________________________________________________________________________")

#2. ¿Cuántas manzanas necesita comprar el cliente para gastar lo mismo que en 15 naranjas?
# Cantidad de manzanas que se pueden comprar
cantidad_manzanas_compra = costo_naranjas / precio_manzana
# Pregunta
print("Nro.4 ¿Cuántas manzanas necesita comprar el cliente para gastar lo mismo que en 15 naranjas?")
# Resultado
print(f"El cliente necesita comprar: {cantidad_manzanas_compra}[manzanas]")
print("________________________________________________________________________________________________________________________________________________________")

#3. ¿Es cierto que comprar 3 manzanas y 2 naranjas cuesta lo mismo que comprar 4 manzanas?
costo_3man_2nar = (3 * precio_manzana) + (2 * precio_naranja)
costo_4man = 4 * precio_manzana
comparacion = costo_3man_2nar == costo_4man
print(comparacion)

print("________________________________________________________________________________________________________________________________________________________")
#4. ¿Es cierto que el costo de 10 manzanas es mayor que el de 8 manzanas y menor que el de 12 manzanas?
# Cálculo
costo_8_manzanas = 8 * precio_manzana
costo_10_manzanas = 10 * precio_manzana
costo_12_manzanas = 12 * precio_manzana
# Verificación
es_mayor_que_8_manzanas = costo_10_manzanas > costo_8_manzanas
es_menor_que_12_manzanas = costo_10_manzanas < costo_12_manzanas
#Pregunta
print("Nro.4¿Es cierto que el costo de 10 manzanas es mayor que el de 8 manzanas y menor que el de 12 manzanas?")
# Resultados
print("El costo de 10 manzanas es mayor que el de 8 manzanas:", es_mayor_que_8_manzanas)
print("El costo de 10 manzanas es menor que el de 12 manzanas:", es_menor_que_12_manzanas)
# Verificar ambas condiciones
resultado_final = es_mayor_que_8_manzanas and es_menor_que_12_manzanas
print("Es cierto que el costo de 10 manzanas es mayor que el de 8 manzanas y menor que el de 12 manzanas:", resultado_final)

print("________________________________________________________________________________________________________________________________________________________")
#5. ¿El costo de 10 manzanas o 15 naranjas es mayor que $20?
costo_mayor_or = costo_manzanas > 20 or costo_naranjas > 20
print(costo_mayor_or)

print("________________________________________________________________________________________________________________________________________________________")
#6. ¿Es cierto que el costo de 10 manzanas es mayor que el de 15 naranjas o el costo de 5 manzanas es mayor que el de 10 naranjas pero no ambos?
costo_manzanas_5 = precio_manzana * 5
costo_naranjas_10 = precio_naranja * 10
# Pregunta
print("#6. ¿Parte 1: Es cierto que el costo de 10 manzanas es mayor que el de 15 naranjas o el costo de 5 manzanas es mayor que el de 10 naranjas:")
# Resultado
print((costo_manzanas > costo_naranjas) or (costo_manzanas_5 > costo_naranjas_10))
print("__________________________________________")
# Pregunta
print("#6. ¿Parte 2: Pero es cierto que el costo de 10 manzanas es mayor que el de 15 naranjas y el costo de 5 manzanas es mayor que el de 10 naranjas:")
# Resultado
print((costo_manzanas > costo_naranjas) ^ (costo_manzanas_5 > costo_naranjas_10))
print("__________________________________________")
# Pregunta
print("#6. ¿Es cierto que el costo de 10 manzanas es mayor que el de 15 naranjas o el costo de 5 manzanas es mayor que el de 10 naranjas pero no ambos?")
# Resultado
print(((costo_manzanas > costo_naranjas) or (costo_manzanas_5 > costo_naranjas_10)) or ((costo_manzanas > costo_naranjas) ^ (costo_manzanas_5 > costo_naranjas_10)))

