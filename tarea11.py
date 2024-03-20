class Vehicle:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Seller:
    def __init__(self, name):
        self.name = name

class Carro(Vehicle):
    seller_class = Seller

    def __init__(self, marca, modelo, seller=None):
        super().__init__(marca, modelo)
        if seller is None:
            self.seller = self.seller_class("Concesionario XYZ")
        else:
            self.seller = seller

class Bote(Vehicle):
    seller_class = Seller

    def __init__(self, marca, modelo, num_pasajeros, seller=None):
        super().__init__(marca, modelo)
        self.num_pasajeros = num_pasajeros
        if seller is None:
            self.seller = self.seller_class("Concesionario Marino")
        else:
            self.seller = seller

class Avion(Vehicle):
    seller_class = Seller

    def __init__(self, marca, modelo, num_asientos, seller=None):
        super().__init__(marca, modelo)
        self.num_asientos = num_asientos
        if seller is None:
            self.seller = self.seller_class("Concesionario Aéreo")
        else:
            self.seller = seller

carro1 = Carro("Jeep", "Wrangler")
carro2 = Carro("Ford", "Explorer", Seller("Concesionario Ford"))

bote1 = Bote("Sea Ray", "Sundancer", 6)
bote2 = Bote("Boston Whaler", "Montauk", 4, Seller("Concesionario Whaler"))

avion1 = Avion("Boeing", "747", 400)
avion2 = Avion("Airbus", "A320", 180, Seller("Concesionario Airbus"))
