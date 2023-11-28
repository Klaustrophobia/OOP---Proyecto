from .producto import Producto

class Camisa(Producto):
    def __init__(self, color, temporada, codigo, marca, material, costo, existencia, tamano):
        super().__init__(codigo, marca, material, costo,existencia, tamano)
        self.color = color
        self.temporada = temporada

    def descuento (self):
        if self.existencia > 2:
            return 0.20 * self.costo 
        elif 3 < self.existencia < 5:
            return 0.25*self.costo 
        elif self.existencia > 5:
            return 0.35*self.costo

    