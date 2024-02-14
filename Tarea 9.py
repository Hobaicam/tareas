class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Bote:
    def __init__(self, marca, modelo, num_pasajeros):
        self.marca = marca
        self.modelo = modelo
        self.num_pasajeros = num_pasajeros

class Avion:
    def __init__(self, marca, modelo, num_asientos):
        self.marca = marca
        self.modelo = modelo
        self.num_asientos = num_asientos

#Inicialización
carro1 = Carro("Toyota", "Camry")
carro2 = Carro("Honda", "Accord")

bote1 = Bote("Sea Ray", "Sundancer", 6)
bote2 = Bote("Boston Whaler", "Montauk", 4)

avion1 = Avion("Boeing", "747", 400)
avion2 = Avion("Airbus", "A320", 180)