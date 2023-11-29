from .producto import Producto
class Combo(Producto):
    def __init__(self, codigo, marca, material, costo, existencia, tamano, nombre, productos):
        super().__init__(codigo, marca, material, costo, existencia, tamano)
        self.nombre = nombre
        self.productos = productos
    
    