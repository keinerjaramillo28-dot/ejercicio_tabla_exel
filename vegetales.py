from herramientas import cuchillo, olla

class tomate:
    def __init__(self, vida, cuchillo):
        self.vida = vida
        self.cuchillo = cuchillo
        
        print(" proceso de corte tomate")
        
        while self.vida > 0:
            cuchillo.daño(self)
        
        print("esta listo para meter a la olla")


class cebolla:
    def __init__(self, vida, cuchillo):
        self.vida = vida
        self.cuchillo = cuchillo
        
        print("proceso de corte cebolla")
        
        while self.vida > 0:
            cuchillo.daño(self)
        
        print(" esta listo para meter a la olla")


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



# zona de los objetos
mi_cuchillo = cuchillo(30, 5)

mi_cuchillo.atributos()

print("Estado del cuchillo después de los cortes=")
mi_cuchillo.atributos()

mi_tomate = tomate(80, mi_cuchillo)
mi_cebolla = cebolla(100, mi_cuchillo)

mi_olla = olla("pasta")
mi_olla.cocinar()

