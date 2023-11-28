class Factura():
    def __init__(self, id_factura, fecha_emision, cliente, detalles, total):
        self.id_factura = id_factura
        self.fecha_emision = fecha_emision
        self.cliente = cliente
        self.detalles = detalles
        self.total = total

    def generar_factura(self):
        pass
    