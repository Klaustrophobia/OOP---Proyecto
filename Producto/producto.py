from abc import ABC, abstractmethod

class Producto(ABC):
    def __init__(self, codigo, marca, material, costo,existencia, tamano):
        self.codigo = codigo
        self.marca = marca 
        self.material = material
        self.costo = costo
        self.existencia = existencia
        self.tamano = tamano

        @abstractmethod
        def descuento():
            pass

        @staticmethod 
        def impuesto():
            pass