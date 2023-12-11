from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, codigo, marca, material, costo,existencia, tamano, existencia_carrito):
        self.codigo = codigo
        self.marca = marca 
        self.material = material
        self.costo = costo
        self.existencia = existencia
        self.tamano = tamano
        self.existencia_carrito = existencia_carrito

    @abstractmethod
    def descuento():
        pass

    @staticmethod 
    def impuesto(self):
        return 0.15 * self.costo 
        