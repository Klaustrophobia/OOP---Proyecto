from datetime import datetime


class OrdenCompra:
    _ordenes_pendientes = [] ## Variable de clase

    def __init__(self, cliente, carrito, envio_opcion, direccion_envio, estado_envio):
        self.cliente = cliente
        self.carrito = carrito
        self.envio_opcion = envio_opcion
        self.direccion_envio = direccion_envio
        self.estado_envio = estado_envio
        self.fecha_pedido = datetime.now()
        self.estado = "Pendiente"

    @classmethod
    def agregar_orden(cls, self):
        cls._ordenes_pendientes.append(self)

    @classmethod
    def obtener_ordenes_pendientes(cls):
        return cls._ordenes_pendientes
    
    def calcular_total(self):
        return sum(producto["costo"] * producto["existencia_carrito"] for producto in self.carrito)
