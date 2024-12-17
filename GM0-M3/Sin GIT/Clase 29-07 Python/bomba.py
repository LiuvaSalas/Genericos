import time
i = 5
print(i) # Muestra el valor 5
time.sleep(1) # espera un segundo
i = 4 # Descuenta 1 al valor de i.
print(i) # Muestra el valor 4
time.sleep(1) # espera un segundo
i = 3 # Descuenta 1 al valor de i.
print(i) # Muestra el valor 3
time.sleep(1) # espera un segundo
i = 2 # Descuenta 1 al valor de i.
print(i) # Muestra el valor 2
time.sleep(1) # espera un segundo
i = 1 # Descuenta 1 al valor de i.
print(i) # Muestra el valor de i
time.sleep(1) # espera un segundo
i = 0
# En este punto se evalúa el fin de ciclo ya que i es cero.
print("BOOM!") # al salir del ciclo la bomba explota!!