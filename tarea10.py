class Vehicle: def init(self, marca, modelo): self.marca = marca self.modelo = modelo

class Carro(Vehicle): pass

class Bote(Vehicle): def init(self, marca, modelo, num_pasajeros): super().init(marca, modelo) self.num_pasajeros = num_pasajeros

class Avion(Vehicle): def init(self, marca, modelo, num_asientos): super().init(marca, modelo) self.num_asientos = num_asientos

carro1 = Carro("Jeep", "Wrangler") carro2 = Carro("Ford", "Explorer")

bote1 = Bote("Sea Ray", "Sundancer", 6) bote2 = Bote("Boston Whaler", "Montauk", 4)

avion1 = Avion("Boeing", "747", 400) avion2 = Avion("Airbus", "A320", 180)
