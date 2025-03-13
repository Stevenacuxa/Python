from abc import ABC, abstractmethod

class Persona(ABC):
    '''Clase que representa una persona'''
    
    @abstractmethod
    def __init__(self, cedula, nombre, apellido):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
    
    @abstractmethod
    def __str__(self):
        return "%s:%s, %s" % (str(self.cedula), self.apellido, self.nombre)
    
class Alumno (Persona):
    '''Clase que representa a un alumno'''
    def __init__(self, cedula, nombre, apellido,carrera):
        super().__init__(cedula, nombre, apellido)
        Persona .__init__(self, cedula, nombre, apellido)
        # agregamos nuevo atributo
        self.carrera = carrera

    def __str__(self):
        return f" {Persona.__str__(self)} , Carrera: {self.carrera}"
    
if __name__ == '__main__':
    #crear un objeto tipo alumno
    alu = Alumno("12345","Steve", "A", "Programacion")

    print(alu.__str__())