class usuario:
    def __init__(self,nombre, cedula):
        self.nombre= nombre
        self.cedula= cedula



    def get_nombre(self):
        return self.nombre
    def set_capturar_nombre(self,nuevo_nombre):
        nuevo_nombre=input("ingresar nombre:")
        self.nombre=nuevo_nombre
    
    def get_apellido(self):
        return self.apellido
    def set_capturar_apellido(self,nuevo_apellido):
        nuevo_apellido=input("ingrese apellido:")
        self.apellido=nuevo_apellido

    def get_cedula(self):
        return self.cedula
    def set_capturar_cedula(self,nueva_cedula):
        nueva_cedula=input("ingrese cedula:")
        self.cedula=nueva_cedula

    def mostrar_resultado(self):
        return f"Usuario: {self.nombre}, Cedula: {self.cedula}"
