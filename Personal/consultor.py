from .persona import Persona 

class Consultor(Persona):
    def __init__(self,  nombre, apellido, identidad, telefono, correo):
        super().__init__(nombre, apellido, identidad, telefono, correo)
        self.nombre = nombre
        self.apellido = apellido
        self.identidad = identidad
        self.telefono = telefono
        self.correo = correo

    
    def ver_productos():
        pass