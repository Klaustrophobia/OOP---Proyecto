from .producto import Producto

class Sueter(Producto):
    def __init__(self, estilo, espesor, cierre, codigo, marca, material, costo,existencia, tamano):
        super().__init__(codigo, marca, material, costo,existencia, tamano)
        self.estilo = estilo
        self.espesor = espesor
        self.cierre = cierre 

    ## Metodo abstracto para generar el descuento
    def descuento (self):
        if self.existencia > 3:
            return 0.25 * self.costo 
        elif 4 < self.existencia < 6:
            return 0.35 * self.costo 
        elif self.existencia > 6:
            return 0.45 * self.costo
    