class cuchillo:
    def __init__(self, fuerza, filo):
        self.fuerza = fuerza
        self.filo = filo
        self.filo_maximo = 5 
    
    def atributos(self):
        print("Fuerza del cuchillo:", self.fuerza)
        print("Filo del cuchillo:", self.filo)
    
    def afilar(self):
        print(" Afilando cuchillo")
        self.filo = self.filo_maximo
        print("Filo del cuchillo restaurado a", self.filo)
    
    def daño(self, objetivo):
        if self.filo <= 0:
            print("cuchillo quedo inutil, sacar filo para seguir cortando")
            self.afilar()  

        daño = self.fuerza
   
        if objetivo.vida < daño:
            daño = objetivo.vida
        
        objetivo.vida -= daño
        self.filo -= 1
        
        print("El cuchillo hizo", daño)
        print("Vida restante:", objetivo.vida)
        print("Filo restante:", self.filo)
        
        return daño

class olla:
    def __init__(self, pasta):
        self.pasta = pasta
        self.coccion = 0  
    
    def cocinar(self):
        print("empezando la coccion de los ingredientes ")
        
        while self.coccion < 100 and input("Desea seguir cocinando? si o no: ") == "si":
            
            self.coccion += 10
            
            if self.coccion > 100:
                self.coccion = 100
            
            print("Nivel de cocción actual:", self.coccion, "%")
        
        if self.coccion == 100:
            print("combate culinario finalizado , la pasta ha sido servida con exito ")
        else:
            print("La cocción de la pasta quedo ", self.coccion, "%")



