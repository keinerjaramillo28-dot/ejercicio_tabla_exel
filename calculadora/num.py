class numeros:
    def __init__(self, valor):
        self.valor = valor

        
    def get_num_1(self):
        return self.num_1
    def set_num1(self,num_1):
        num_1=input("ingrese un  numero:")
        self.num_1=num_1
    
    def get_num_2(self):
        return self.num_2
    def set_num_2(self,num_2):
        num_2=input("ingrese un numero:")
        self.num_2=num_2

    def mostrar_resultado(self):
        return f"Numero: {self.valor}"

    