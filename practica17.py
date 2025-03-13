from practica16 import Calculadora
#CalculadoraCientifica hereda de Calculadora
class CalculadoraCientifica(Calculadora):
    
    def __init__(self):
        super()

    def factorial(self):
        factorial = 1
        for x in range (1, self.numero1 + 1):
            factorial= factorial * x
        return factorial
    
if __name__ == "__main__":
    casiofx = CalculadoraCientifica()
    casiofx.setNumeros(5,2)
    print(casiofx.factorial())
