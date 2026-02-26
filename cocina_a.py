
class cocina:
    def __init__(self, olla):
        self.mi_olla = olla
        

    def verificar_producto(self):
        if self.mi_olla == True:
            print("la olla esta lista")
            return True
        else:
            print("no puedes iniciar sin olla")
            return False
        
