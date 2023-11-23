from .producto import Producto

class Camisa(Producto):
    def __init__(self, color, temporada, codigo, marca, material, costo,existencia, tamano):
        super().__init__(codigo, marca, material, costo,existencia, tamano)
        self.color = color
        self.temporada = temporada

        