class Vehiculo:
    def __init__(self, tipo, marca, modelo, año):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return f"Tipo: {self.tipo}\nMarca: {self.marca}\nModelo: {self.modelo}\nAño: {self.año}"

class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__("Carro", marca, modelo, año)
        self.num_puertas = num_puertas

    def __str__(self):
        return super().__str__() + f"\nNúmero de puertas: {self.num_puertas}"

class Barco(Vehiculo):
    def __init__(self, marca, modelo, año, eslora):
        super().__init__("Barco", marca, modelo, año)
        self.eslora = eslora

    def __str__(self):
        return super().__str__() + f"\nEslora: {self.eslora}"

class Avion(Vehiculo):
    def __init__(self, marca, modelo, año, autonomia):
        super().__init__("Avión", marca, modelo, año)
        self.autonomia = autonomia

    def __str__(self):
        return super().__str__() + f"\nAutonomía: {self.autonomia}"





carro1 = Carro("Toyota", "Fortuner", 2004, 4)


barco1 = Barco("Beneteau", "Oceanis 46.1", 2020, 14)

avion1 = Avion("Boeing", "737", 1968, 2580 )



print(carro1)
print("\n")
print(barco1)
print("\n")
print(avion1)
print("\n")
