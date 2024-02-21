class Seller:
    def __init__(self, nombre):
        self.nombre = nombre
        

    def __str__(self):
        return f"Vendedor: {self.nombre}"
class Vehiculo:
    def __init__(self, tipo, marca, modelo, año):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.seller = None  
    def __str__(self):
        return f"Tipo: {self.tipo}\nMarca: {self.marca}\nModelo: {self.modelo}\nAño: {self.año}\nVendedor: {self.seller.nombre if self.seller else 'Sin vendedor'}"


class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__("Carro", marca, modelo, año)
        self.num_puertas = num_puertas


class Barco(Vehiculo):
    def __init__(self, marca, modelo, año, eslora):
        super().__init__("Barco", marca, modelo, año)
        self.eslora = eslora


class Avion(Vehiculo):
    def __init__(self, marca, modelo, año, autonomia):
        super().__init__("Avión", marca, modelo, año)
        self.autonomia = autonomia
seller1 = Seller("Multimarca")
seller2 = Seller("Fountaine Pajot")
seller3 = Seller("CFS Jets")


carro1 = Carro("Toyota", "Fortuner", 2004, 4)
barco1 = Barco("Beneteau", "Oceanis 46.1", 2020, 14)
avion1 = Avion("Boeing", "737", 1968, 2580)

carro1.seller = seller1
barco1.seller = seller2
avion1.seller = seller3


print(carro1)
print("\n")
print(barco1)
print("\n")
print(avion1)
print("\n")