# Clase base Vehiculo
class Vehiculo:

    def __init__(self, marca):
        """
        Inicializa un vehículo con su marca.

        :param marca: Marca del vehículo.
        """
        self.marca = marca

    def describir_vehiculo(self):
        """
        Imprime una descripción básica del vehículo.
        """
        print(f"Marca del vehículo: {self.marca}")


# Clase Coche que hereda de Vehiculo
class Coche(Vehiculo):

    def __init__(self, marca, num_puertas):
        """
        Inicializa un coche con su marca y número de puertas.

        :param marca: Marca del coche.
        :param num_puertas: Número de puertas del coche.
        """
        super().__init__(marca)
        self.num_puertas = num_puertas

    def describir_vehiculo(self):
        """
        Imprime una descripción detallada del coche, incluyendo el número de puertas.
        """
        print(
            f"Marca del coche: {self.marca}, Número de puertas: {self.num_puertas}"
        )


# Clase Bicicleta que hereda de Vehiculo
class Bicicleta(Vehiculo):

    def __init__(self, marca, tipo):
        """
        Inicializa una bicicleta con su marca y tipo.

        :param marca: Marca de la bicicleta.
        :param tipo: Tipo de bicicleta (e.g., montaña, carretera).
        """
        super().__init__(marca)
        self.tipo = tipo

    def describir_vehiculo(self):
        """
        Imprime una descripción detallada de la bicicleta, incluyendo su tipo.
        """
        print(f"Marca de la bicicleta: {self.marca}, Tipo: {self.tipo}")


# Clase Electrico
class Electrico:

    def __init__(self, bateria):
        """
        Inicializa un dispositivo eléctrico con una capacidad de batería.

        :param bateria: Capacidad de la batería en kWh.
        """
        self.bateria = bateria

    def mostrar_bateria(self):
        """
        Imprime la capacidad de la batería.
        """
        print(f"Capacidad de la batería: {self.bateria} kWh")


# Clase BicicletaElectrica que hereda de Bicicleta y Electrico (herencia múltiple)
class BicicletaElectrica(Bicicleta, Electrico):

    def __init__(self, marca, tipo, bateria):
        """
        Inicializa una bicicleta eléctrica con su marca, tipo y capacidad de batería.

        :param marca: Marca de la bicicleta eléctrica.
        :param tipo: Tipo de bicicleta.
        :param bateria: Capacidad de la batería en kWh.
        """
        Bicicleta.__init__(self, marca, tipo)
        Electrico.__init__(self, bateria)

    def describir_vehiculo(self):
        """
        Imprime una descripción detallada de la bicicleta eléctrica, incluyendo su tipo y capacidad de batería.
        """
        print(
            f"Marca de la bicicleta eléctrica: {self.marca}, Tipo: {self.tipo}, "
            f"Capacidad de la batería: {self.bateria} kWh")


# Ejemplo de uso
if __name__ == "__main__":
    coche = Coche("Toyota", 4)
    coche.describir_vehiculo()

    bicicleta = Bicicleta("Giant", "Montaña")
    bicicleta.describir_vehiculo()

    bicicleta_electrica = BicicletaElectrica("Trek", "Carretera", 10.5)
    bicicleta_electrica.describir_vehiculo()
