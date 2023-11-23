from .producto import Producto

class Sueter(Producto):
    def __init__(self, estilo, espesor, cierre, codigo, marca, material, costo,existencia, tamano):
        super().__init__(codigo, marca, material, costo,existencia, tamano)
        self.estilo = estilo
        self.espesor = espesor
        self.cierre = cierre 
        