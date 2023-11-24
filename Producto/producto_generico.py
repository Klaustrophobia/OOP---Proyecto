from .producto import Producto

class Producto_Generico(Producto):
    def __init__(self, codigo, marca, material, costo,existencia, tamano):
        super().__init__(codigo, marca, material, costo,existencia, tamano)