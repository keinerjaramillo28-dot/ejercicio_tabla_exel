class usuario:  
    def __init__(self, nombre, cedula, rango):
        self.nombre = nombre
        self.cedula = cedula
        self.rango = rango
    def get_nombre(self):
        return self.nombre
    def set_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def get_cedula(self):
        return self.cedula
    def set_cedula(self, nueva_cedula):
        self.cedula = nueva_cedula
    def get_rango(self):
        return self.rango
    def set_rango(self, nuevo_rango):
        self.rango = nuevo_rango
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cédula: {self.cedula}")
        print(f"Rango: {self.rango}")
