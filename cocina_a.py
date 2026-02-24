
class cocina:
    def __init__(self, tomate, cebolla, olla, pasta, agua):
        self.tomate = tomate
        self.cebolla = cebolla
        self.olla = olla
        self.pasta = pasta
        self.agua = agua

    def verificar_ingredientes(self):
        if self.tomate and self.cebolla and self.olla and self.pasta and self.agua:
            return "Los ingredientes están listos para cocinar"
        else:
            return "Los ingredientes no están listos"