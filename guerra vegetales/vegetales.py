class Vegetal:
    def __init__(self, nombre, vida):  
        self.nombre = nombre
        self.vida = vida

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, "está completamente picado")


class cebolla:
    def __init__(self):
        self.nombre = "Cebolla"
        self.vida = 100  

    def esta_muerta(self):
        return self.vida <= 0  

    def mostrar_vida(self):
        print(f"{self.nombre} tiene {self.vida} de vida")

    def morir(self):
        self.vida = 0
        print(self.nombre, "está completamente picada")


class tomate:
    def __init__(self):
        self.nombre = "Tomate"
        self.vida = 100  

    def esta_muerta(self):
        return self.vida <= 0  

    def mostrar_vida(self):
        print(f"{self.nombre} tiene {self.vida} de vida")

    def morir(self):
        self.vida = 0
        print(self.nombre, "está completamente picado")


class pasta:
    def __init__(self):
        self.vida = 0  

    def hervir(self):
        self.vida += 20
        print("nivel de cocción =", self.vida)

    def get_vida(self):
        return self.vida

    def lista(self):
        return self.vida >= 100