class Carro:
    def __init__(self, marca, placa, color):
        self.marca = marca
        self.placa = placa
        self.color = color
    
    def get_marca(self):
        return self.marca
    def set_marca(self, nueva_marca):
        self.marca = nueva_marca
    def get_placa(self):
        return self.placa
    def set_placa(self, nueva_placa):
        self.placa = nueva_placa
    def get_color(self):
        return self.color
    def set_color(self, nuevo_color):
        self.color = nuevo_color
    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Placa: {self.placa}")
        print(f"Color: {self.color}")

    
