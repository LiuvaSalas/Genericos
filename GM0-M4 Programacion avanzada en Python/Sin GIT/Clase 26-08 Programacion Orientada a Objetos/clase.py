class Dato:
    def __init__(self, dato1) -> None:
        self.dato1 = dato1

    def __str__(self) -> str:
        return f"{self.dato1}"

    def __add__(self, suma_datos):
        return Dato(self.dato1 + suma_datos.dato1)


primer_dato = Dato(10)
segundo_dato = Dato(30)

print(type(primer_dato.dato1))
print(primer_dato.dato1)
print(segundo_dato.dato1)

print(primer_dato + segundo_dato)
