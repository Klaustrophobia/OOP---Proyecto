## Toma informacion de archivos JSON
import json
## Hace invisible en el CMD las contrasenas
import getpass
## Proporciona una interfaz para interactuar con el OS en el que se está ejecutando el script.
import os

from Personal.personal import Personal
from Compra.OrdenCompra import OrdenCompra

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
                print(f'Inicio de sesión exitoso para {u["nombre"]}')
                return True 
        return False   

    def login(self): 
        vendedor = Login_Vendedor.cargar_credenciales()  ##Mandar a llamar al metodo estatico dentro de la clase
        numEmpleado = input("Numero de Empleado: ")
        password = getpass.getpass("Contrasena: ")

        if Login_Vendedor.verificar_credenciales(numEmpleado, password, vendedor):
            Menu.menu(self)
        else:
            print("Credenciales incorrectas. Inténtelo de nuevo.")
            return False


class Vendedor(Personal):
    def __init__(self, metas_ventas, ventas_netas, num_empleado, salario, nombre, apellido, identidad, telefono, correo):
        super().__init__(num_empleado, salario, nombre, apellido, identidad, telefono, correo)
        self.metas_ventas = metas_ventas
        self.ventas_netas = ventas_netas
        
    def realizar_cobro(self):
       # Obtener las órdenes pendientes
        ordenes_pendientes = OrdenCompra.obtener_ordenes_pendientes()

        if not ordenes_pendientes:
            print("No hay ordenes pendientes para cobrar.")
            return

        print("Ordenes pendientes:")
        for i, orden in enumerate(ordenes_pendientes, 1):
            print(f"{i}. Cliente: {orden.cliente.nombre} {orden.cliente.apellido}, Total: ${orden.calcular_total()}")

        try:
            seleccion = int(input("Seleccione el número de la orden a cobrar: "))
            orden_seleccionada = ordenes_pendientes[seleccion - 1]

            total = orden_seleccionada.calcular_total()
            print(f"Cobrando ${total} a {orden_seleccionada.cliente.nombre} {orden_seleccionada.cliente.apellido}...")
            print()
            print(f"Cobro realizado con exito a {orden_seleccionada.cliente.nombre}")

            # Eliminar el carrito que se pagó
            orden_seleccionada.cliente.carrito = []

            # Eliminar la orden de la lista de órdenes pendientes
            OrdenCompra._ordenes_pendientes.remove(orden_seleccionada)
        except (ValueError, IndexError):
            print("Selección no válida.")

    def metas_ventas(self):

        #Hacer que imprima el atributo de las metas del vendedor mensuales\

        pass

    def ventas_netas(self):

        #Hacer que imprima las ventas realizadas 
        
        pass

class Menu(): 

    def menu(self):
        print("Menú de Vendedor")
        print("1. Realizar venta")
        print("2. Ver metas de ventas")
        print("3. Ver ventas netas")
        print("4. Volver al menú principal")

        try:
            option = int(input("Ingrese la opción: "))
        except ValueError:
            print("Opción no válida, vuelva a intentar.")
        else:
            match option:
                case 1:
                    Vendedor.realizar_cobro(self)
                case 2:                
                    Vendedor.metas_netas(self)
                case 3:
                    Vendedor.ventas_netas(self)
                case 4:
                    return True
                case default:
                    print("Opción no válida.")
