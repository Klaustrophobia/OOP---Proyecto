## Toma informacion de archivos JSON
import json
## Hace invisible en el CMD las contrasenas
import getpass
## Proporciona una interfaz para interactuar con el OS en el que se está ejecutando el script.
import os

from Personal.personal import Personal
from Compra.OrdenCompra import OrdenCompra
from Compra.Factura import Factura

class Login_Vendedor():
    @staticmethod
    def cargar_credenciales():
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "../Credenciales/vendedor.json")
        
        with open(file_path, "r") as archivo:
            data = json.load(archivo)
            return data["users"]

    @staticmethod
    def verificar_credenciales(numEmpleado, password, vendedor):
        for u in vendedor:
            if u["numEmpleado"] == numEmpleado and u["password"] == password :
                print(f'\n--Inicio de sesión exitoso. Bienvenido {u["nombre"]}.--')
                Vendedor.set_vendedor_actual(u)  # Establecer el vendedor actual
                return True 
        return False  

    def login(self): 
        vendedor = Login_Vendedor.cargar_credenciales()  ##Mandar a llamar al metodo estatico dentro de la clase
        print("\n**** --Login de Vendedor-- ****")
        numEmpleado = input("Numero de Empleado: ")
        password = getpass.getpass("Contrasena: ")

        if Login_Vendedor.verificar_credenciales(numEmpleado, password, vendedor):
            Menu.menu(self)
        else:
            print("\n--Credenciales incorrectas. Inténtelo de nuevo.--")
            return False

class Vendedor(Personal):
    vendedor_actual = None  # Variable de clase para almacenar la información del vendedor actual

    def __init__(self, metas_ventas, ventas_netas, num_empleado, salario, nombre, apellido, identidad, telefono, correo):
        super().__init__(num_empleado, salario, nombre, apellido, identidad, telefono, correo)
        self.metas_ventas = metas_ventas
        self.ventas_netas = ventas_netas
        
    @classmethod
    def set_vendedor_actual(cls, vendedor):
        cls.vendedor_actual = vendedor

    @classmethod
    def get_vendedor_actual_metas_ventas(cls):
        if cls.vendedor_actual:
            return cls.vendedor_actual["metas_ventas"]
        else:
            print("\n--No se pudo obtener las metas de ventas.--")
            return None
        
    def realizar_cobro(self):
       # Obtener las órdenes pendientes
        ordenes_pendientes = OrdenCompra.obtener_ordenes_pendientes()

        if not ordenes_pendientes:
            print("\n--No hay ordenes pendientes para cobrar.--")
            return

        print("\n**** --Ordenes pendientes-- ****")
        for i, orden in enumerate(ordenes_pendientes, 1):
            print(f"{i}. Cliente: {orden.cliente.nombre} {orden.cliente.apellido}, Total: ${orden.calcular_total()}")

        try:
            seleccion = int(input("Seleccione el número de la orden a cobrar: "))
            orden_seleccionada = ordenes_pendientes[seleccion - 1]
            total = orden_seleccionada.calcular_total()
        except (ValueError, IndexError):
            print("\n--Opción No Válida. Inténtelo de nuevo.--")
        else:
            
            print(f"\nCobrando ${total} a {orden_seleccionada.cliente.nombre} {orden_seleccionada.cliente.apellido}...")
            print(f"\nCobro realizado con exito a {orden_seleccionada.cliente.nombre}")

            # Eliminar el carrito que se pagó
            orden_seleccionada.cliente.carrito = []
            
            # Agrega la factura en ordenes de facturas
            Factura.agregar_factura(orden_seleccionada)

            # Para imprimir las facturas almacenadas
            for factura in Factura._facturas_cobradas:
                Factura.imprimir_factura(factura)

            # Eliminar la orden de la lista de órdenes pendientes
            OrdenCompra._ordenes_pendientes.remove(orden_seleccionada)
    
    def metas_ventas(self): 
        metas_ventas = Vendedor.get_vendedor_actual_metas_ventas()
        if metas_ventas is not None:
            print(f"\nLas metas de ventas son: ${metas_ventas}")
        else:
            print("\nNo hay metas de ventas disponibles.")

        
    def ventas_netas(self):
        pass


class Menu(): 

    def menu(self):
        seguir = True
        while (seguir):
            
            print("\n**** --Menú de Vendedor-- ****")
            print("1. Realizar venta")
            print("2. Ver metas de ventas")
            print("3. Ver ventas netas")
            print("4. Volver al menú principal")

            try:
                option = int(input("Ingrese la opción: "))
            except ValueError:
                print("\n--Opción No Válida. Inténtelo de nuevo.--")
            else:
                
                match option:
                    
                    case 1:
                        Vendedor.realizar_cobro(self)
                    
                    case 2:                
                        print("\n**** --Meta de ventas-- ****")
                        Vendedor.metas_ventas(self)
                    
                    case 3:
                        print("\n**** --Ventas Netas-- ****")
                    
                    case 4:
                        print("\n--Saliendo... Hasta Pronto.--")
                        seguir = False
                    
                    case default:
                        print("\n--Opción No Válida. Inténtelo de nuevo.--")
