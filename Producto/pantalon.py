from Producto.producto import Producto

class Pantalon(Producto):
    def __init__(self, codigo, marca, material, costo, existencia, tamano, estilo, color):
        super().__init__(codigo, marca, material, costo, existencia, tamano)
        self.estilo = estilo
        self.color = color
        