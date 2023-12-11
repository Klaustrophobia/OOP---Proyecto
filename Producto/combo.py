from .producto import Producto
class Combo(Producto):
    def __init__(self, codigo, marca, material, costo, existencia, tamano, nombre, existencia_carrito, productos):
        super().__init__(codigo, marca, material, costo, existencia, tamano, existencia_carrito)
        self.nombre = nombre
        self.productos = productos
    
    