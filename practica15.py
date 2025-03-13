class Pokemon:
    #Definicion de pokemon
    #atributos
    nombre = None
    habilidad = None
    tipo= None

    #constructor
    def __init__(self, n, h, t):
        self.nombre = n
        self.habilidad = h
        self.tipo = t
    
    #metodos
    def verNombres(self):
        return self.nombre
    
    def atacar(self):
        print(f"{self.nombre} atacó")
    
    def defenderse(self):
        print(f"{self.nombre} se defendió")

if __name__ == "__main__":
    picachu1 = Pokemon ("Picachu", "Trueno", "Electrico")
    picachu1.atacar()
    picachu1.defenderse()


        
    ramayer1 =Pokemon ("Ramayer", "Fogata", "Fuego")
    ramayer1.atacar()
    ramayer1.defenderse()