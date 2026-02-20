class parqueadero:
    def __init__(self, usuario, carro):
        self.usuario = usuario
        self.carro = carro
        self.fecha_entrada = ""
        self.hora_entrada = ""
        self.hora_salida = ""
        self.estado = ""

    def registrar_entrada(self, fecha, hora):
        self.fecha_entrada = input("Ingrese la fecha de entrada (DD/MM/AAAA): ")
        self.hora_entrada = input("Ingrese la hora de entrada (HH:MM): ")
        self.estado = "ADENTRO"
        print("entrada registrada exitosamente.")

    def registrar_salida(self):
        self.hora_salida = input("Ingrese la hora de salida (HH:MM): ")
        self.estado = "FUERA"
        print("salida registrada exitosamente.")
    def mostrar_informacion(self):
        print(f"Fecha de entrada: {self.fecha_entrada}")
        print(f"Hora de entrada: {self.hora_entrada}")
        print(f"Hora de salida: {self.hora_salida}")
        print(f"Estado: {self.estado}")
