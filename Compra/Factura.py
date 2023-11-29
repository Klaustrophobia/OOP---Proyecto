from datetime import datetime

class Factura:
    _facturas_cobradas = []  # Lista para almacenar facturas cobradas
    
    def __init__(self, id_factura, fecha_emision, cliente, detalles, total):
        self.id_factura = id_factura
        self.fecha_emision = fecha_emision
        self.cliente = cliente
        self.detalles = detalles
        self.total = total

    @classmethod
    def agregar_factura(cls, orden):
        id_factura = len(cls._facturas_cobradas) + 1  # Generar un nuevo ID de factura
        fecha_emision = datetime.now()
        detalles = orden.carrito  # Detalles de la factura obtenidos del carrito
        total = orden.calcular_total()  # Calcular el total de la factura

        factura = cls(id_factura, fecha_emision, orden.cliente, detalles, total)
        cls._facturas_cobradas.append(factura)

    @classmethod
    def imprimir_factura(cls, factura):
        print("----- Factura -----")
        print(f"ID de Factura: {factura.id_factura}")
        print(f"Fecha de Emisión: {factura.fecha_emision}")
        print(f"Cliente: {factura.cliente.nombre} {factura.cliente.apellido}")
        print("\nDetalles:")
        for producto in factura.detalles:
            print(f"  - Marca: {producto['marca']}, Precio: {producto['costo']}, Cantidad: {producto['existencia_carrito']}")
        print(f"\nTotal: ${factura.total}")
        print("-------------------")