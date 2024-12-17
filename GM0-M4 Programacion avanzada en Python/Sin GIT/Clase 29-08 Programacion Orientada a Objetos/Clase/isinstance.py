class Animal:
  pass


class Perro(Animal):
  pass


class Gato(Animal):
  pass


class Mascota(Perro):
  pass


gato = Gato()
firulais = Mascota()

print(isinstance(firulais, (Perro, int)))
print(isinstance(gato, (Perro, int)))
