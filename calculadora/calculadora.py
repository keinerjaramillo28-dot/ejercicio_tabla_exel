class calculadora:
    from num import numeros
    from usuary import usuario
 
    
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.registro = []

    def suma(self):
        return self.num1.valor + self.num2.valor

    def resta(self):
        return self.num1.valor - self.num2.valor

    def multiplicacion(self):
        return self.num1.valor * self.num2.valor

    def division(self):
        return self.num1.valor / self.num2.valor
        