from .producto import Producto
class Combo(Producto):
    def __init__(self, nombre, productos_incluidos, precio_total):
        self.nombre = nombre 
        self.productos_incluidos = productos_incluidos
        self.precio_total = precio_total
    
    