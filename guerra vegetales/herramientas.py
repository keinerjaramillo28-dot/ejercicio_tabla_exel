class cuchillo:
    def __init__(self,filo):
        self.filo = filo
         
    
    def atributos(self):
        print("Filo del cuchillo:", self.filo)
    
    def usar(self,vegetales):
        if self.filo<= 0:
            print("el cuchillo no tiene filo")
        else:
            daño=20
            vegetales.vida = vegetales.vida - daño
            self.filo = self.filo -10
            print("se hizo",daño,"de daño a",vegetales.nombre, "=", vegetales.vida)
            print("filo actual=",self.filo)

    def afilar(self):
        self.filo = 100
        print("cuchillo afilado a 100")

    def esta_inutil(self):
        return self.filo <= 0
    

class olla:
    def __init__(self):
        self.cebolla = False
        self.tomate = False

    def colocar_cebolla(self):
        self.cebolla = True
        print("cebolla agregada")
    
    def colocar_tomate(self):
        self.tomate = True
        print("tomate agragado")
    
    def servir(self):
        print("la pasta se sirvio con existo en el plato")

        