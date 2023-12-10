## Proporciona una interfaz para interactuar con el OS en el que se está ejecutando el script.
import os
import json

from .persona import Persona
from Compra.OrdenCompra import OrdenCompra

class Cliente(Persona):
    def __init__(self, nombre, apellido, identidad, telefono, correo):
        super().__init__(nombre, apellido, identidad, telefono, correo)
        self.lista_productos_original = {}  # Inicializa el catálogo original

    def realizar_compra(self):
        
        try:
            script_dir = os.path.dirname(__file__)
            file_path = os.path.join(script_dir, "../Credenciales/productos.json")

            with open(file_path, 'r') as file:
                lista_productos = json.load(file)
                
            categorias_disponibles = list(lista_productos.keys())
        
        except FileNotFoundError:
                print("\n--No se encontró el archivo JSON de productos.--")
        except json.JSONDecodeError:
                print("\n--Error al recorrer el archivo JSON de productos.--")
        else:
            
            seguir = True        
            while (seguir):

                print("\n**** --Categorias Disponibles-- ****")
                for i, categoria in enumerate(categorias_disponibles, 1):
                    print(f"{i}. {categoria}")
                print(f"{len(categorias_disponibles) + 1}. salir")
                
                try:
                    opcion_categoria = int(input("Ingrese el número de la categoría: "))
                except ValueError:
                    print("\n--Opción No Válida. Inténtelo de nuevo.--")
                else:
                    
                    if opcion_categoria == (len(categorias_disponibles) + 1):
                        seguir = False
                    
                    elif 1 <= opcion_categoria <= len(categorias_disponibles):
                        categoria_seleccionada = categorias_disponibles[opcion_categoria - 1]
                        print(categoria_seleccionada)
                        productos_categoria = lista_productos[categoria_seleccionada]

                        # Imprimir los productos de la categoría seleccionada
                        print(f"\n**** --Lista de productos ({categoria_seleccionada})-- ****")
                        
                        if categoria_seleccionada != "combo":
                            for j, producto in enumerate(productos_categoria, 1):
                                print(f'{j}. Marca: {producto["marca"]}, Precio: {producto["costo"]}, Stock: {producto["existencia"]}')
                        else:
                            for k, producto in enumerate(productos_categoria, 1):
                                print(f'{k}. Combo: {producto["nombre"]}')

                        select = input("Desea seleccionar alguna prenda (si/no): ").lower()

                        while select == "si":
                            
                            print("\n**** --Seleccione un producto-- ****")
                            if categoria_seleccionada != "combo":
                                for j, producto in enumerate(productos_categoria, 1):
                                    print(f'{j}. Marca: {producto["marca"]}, Precio: {producto["costo"]}, Stock: {producto["existencia"]}')
                            else:
                                for k, producto in enumerate(productos_categoria, 1):
                                    print(f'{k}. Combo: {producto["nombre"]}')

                            try:
                                seleccion = int(input("Seleccione el número de la prenda a comprar: "))
                                cantidad_comprar = int(input("Ingrese la cantidad a comprar: "))
                            except ValueError:
                                print("\n--Opción No Válida. Inténtelo de nuevo.--")
                            else:
                                
                                if 1 <= seleccion <= len(productos_categoria) and cantidad_comprar > 0:
                                    producto_seleccionado = productos_categoria[seleccion - 1]

                                    if cantidad_comprar <= int(producto_seleccionado["existencia"]):
                                        # Añadir la cantidad a comprar al carrito
                                        producto_seleccionado["existencia_carrito"] = cantidad_comprar
                                        self.carrito.append(producto_seleccionado)
                                        print(f"\n--Producto añadido al carrito: {producto_seleccionado['marca']}--")

                                        # Actualizar existencias en el catálogo original
                                        producto_original = self.lista_productos_original.get(categoria_seleccionada, {}).get(seleccion - 1)
                                        if producto_original is not None:
                                            producto_original['existencia'] -= cantidad_comprar

                                        # Actualizar existencias en el catálogo actual
                                        lista_productos[categoria_seleccionada][seleccion-1]['existencia'] -= cantidad_comprar
                                        with open(file_path,'w') as file:
                                            json.dump(lista_productos,file,indent=4)
                                    else:
                                        print("\n--No hay suficiente stock para la cantidad seleccionada.--")
                                
                                else:
                                    print("\n--Número De Prenda o cantidad a comprar No válidos. Inténtelo de nuevo.--")

                                # Pregunta si desea seguir comprando
                                select = input(f"\n¿Desea seguir comprando {categoria_seleccionada}s? (si/no): ").lower()

                    else:
                        print("\n--Opción No Válida. Inténtelo de nuevo.--")


    def carrito_compras(self):

        if not self.carrito:
            print("\n--El carrito está vacío. Favor agregar productos.--")
            return

        print("Detalles de su carrito de compras: ")
        for producto in self.carrito:
            print(f'Marca: {producto["marca"]}, Precio: {producto["costo"]}, Cantidad: {producto["existencia_carrito"]}')

        total = sum(producto["costo"] * producto["existencia_carrito"] for producto in self.carrito)
        print(f'Total de la compra: ${total}')

        select = input("Desea regresar al menú principal (si/no): ").lower()
        if select == 'si':
            Menu_Cliente.menu(self)
        else:
            Cliente.enviar_carrito(self)  # Llamada a la función de enviar_carrito

    def enviar_carrito(self):

        if not self.carrito:
            print("\n--El carrito está vacío. Agregue productos antes de enviar a facturar.--")
            return

        print("Detalles de su carrito de compras: ")
        for producto in self.carrito:
            print(f'Marca: {producto["marca"]}, Precio: {producto["costo"]}, Cantidad: {producto["existencia_carrito"]}')

        total = sum(producto["costo"] * producto["existencia_carrito"] for producto in self.carrito)
        print(f'Total de la compra: ${total}')

        # Solicitar datos del cliente
        print("\n**** --Datos del cliente-- ****")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        identidad = input("Ingrese su ID: ")
        telefono = input("Ingrese su número de teléfono: ")
        correo = input("Ingrese su correo electrónico: ")
        cliente = Cliente(nombre, apellido, identidad, telefono, correo)

        # Solicitar información de envío
        envio_opcion = input("¿Desea envío a domicilio? (si/no): ").lower()
        if envio_opcion == "si":
            direccion_envio = input("Ingrese su dirección de envío: ")
            estado_envio = "Pendiente"  # Puedes establecer un estado inicial, por ejemplo, "Pendiente"
        else:
            direccion_envio = "Recoger en tienda"
            estado_envio = "No aplica"

        # Confirmar y enviar a facturar
        confirmar_factura = input("¿Desea enviar a facturar? (si/no): ").lower()
        if confirmar_factura == "si":
            orden_compra = OrdenCompra(cliente, self.carrito, envio_opcion, direccion_envio, estado_envio)
            OrdenCompra.agregar_orden(orden_compra)  # Agregar la orden a la lista de órdenes en la clase OrdenCompra
            self.carrito = []  # Limpiar el carrito después de enviar a facturar
            print("\nSu orden esta siendo procesada. Gracias por su compra!")
        else:
            print("\nCompra no procesada. Puede seguir agregando productos al carrito.")

class Menu_Cliente():

    def __init__(self):
        self.carrito = []
        self.lista_productos_original = {}  # Inicializa el catálogo original

    def menu(self):
        
        seguir = True
        while(seguir):
            print("\n**** --Menú de Cliente-- ****")
            print("1. Realizar Compra")
            print("2. Ver carrito")
            print("3. Enviar a facturar")
            print("4. Salir")

            try:
                option = int(input("Ingrese la opción: "))
            except ValueError:
                print("\n--Opción No Válida. Inténtelo de nuevo.--")
            else:
                
                match option:
                    
                    case 1:
                        Cliente.realizar_compra(self)
                    
                    case 2:
                        Cliente.carrito_compras(self)
                    
                    case 3:
                        Cliente.enviar_carrito(self)
                    
                    case 4:
                        return True         
                    
                    case default:
                        print("\n--Opción No Válida. Inténtelo de nuevo.--")

