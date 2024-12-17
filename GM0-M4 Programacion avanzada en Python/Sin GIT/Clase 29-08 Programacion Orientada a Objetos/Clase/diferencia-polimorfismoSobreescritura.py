class Animal:
    def hacer_sonido(self):
        return "Algun sonido"

class Perro(Animal):
    def hacer_sonido(self):
        return "Ladrido"

class Gato(Animal):
    def hacer_sonido(self):
        return "Maullido"




if __name__ == "__main__":
  # Sobreescritura
  animal = Animal()
  print(animal.hacer_sonido())

  perro = Perro()
  print(perro.hacer_sonido())

  gato = Gato()
  print(gato.hacer_sonido())

  animales = [Perro(), Gato(), Animal()]

  # Polimorfismo
  for animal in animales:
      print(animal.hacer_sonido())
  