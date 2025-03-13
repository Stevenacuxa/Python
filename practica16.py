class Calculadora:
    #atributos
    historial = None
    #constructor
    def __init__(self):
        self.historial = []
        self.numero1 = 0 
        self.numero2 = 0 

    def setNumeros(self, x:float, y:float):
        self.numero1 = x
        self.numero2 = y

    def sumar(self):
        self.historial.append(f"{self.numero1} + {self.numero2} = {self.numero1 + self.numero2}")
        return self.numero1 + self.numero2

    def restar(self):
        self.historial.append(f"{self.numero1} - {self.numero2} = {self.numero1 - self.numero2}")
        return self.numero1 - self.numero2

    def multiplicación(self):
        self.historial.append(f"{self.numero1} * {self.numero2} = {self.numero1 * self.numero2}")
        return self.numero1 * self.numero2

    def división(self):
        self.historial.append(f"{self.numero1} / {self.numero2} = {self.numero1 / self.numero2}")
        return self.numero1 / self.numero2

    def verHistorial (self):
        return self.historial

if __name__ == "__main__":
    casio = Calculadora()
    casio.setNumeros(5,3)
    casio.setNumeros(8,4)
    print("La suma es ",casio.sumar())
    print("La resta es ",casio.restar())
    print("La multiplicacion es ",casio.multiplicación())
    print("La division es ",casio.división())

    print("Historial De Calculos")
    print(casio.verHistorial())

        