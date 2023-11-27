## Proporciona una interfaz para interactuar con el OS en el que se está ejecutando el script.
import os
import json

from .persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, identidad, telefono, correo):
        super().__init__(nombre, apellido, identidad, telefono, correo)

    def realizar_compra(self):
        try:
            script_dir = os.path.dirname(__file__)
            file_path = os.path.join(script_dir, "../Credenciales/productos.json")

            with open(file_path, 'r') as file:
                lista_productos = json.load(file)

            categorias_disponibles = list(lista_productos.keys())

            print("Seleccione la categoría que desea visualizar:")
            for i, categoria in enumerate(categorias_disponibles, 1):
                print(f"{i}. {categoria}")

            try:
                opcion_categoria = int(input("Ingrese el número de la categoría: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                return

            if 1 <= opcion_categoria <= len(categorias_disponibles):
                categoria_seleccionada = categorias_disponibles[opcion_categoria - 1]
                productos_categoria = lista_productos[categoria_seleccionada]

                # Imprimir los productos de la categoría seleccionada
                print(f"\nLista de productos ({categoria_seleccionada}):")
                for j, producto in enumerate(productos_categoria, 1):
                    print(f'{j}. Marca: {producto["marca"]}, Precio: {producto["costo"]}, Stock: {producto["existencia"]}')
            else:
                print("Opción no válida.")
                return

            select = input("Desea seleccionar alguna prenda (si/no): ").lower()

            while select == "si":
                try:
                    for j, producto in enumerate(productos_categoria, 1):
                        print(f'{j}. Marca: {producto["marca"]}, Precio: {producto["costo"]}, Stock: {producto["existencia"]}')
                    
                    seleccion = int(input("Seleccione el número de la prenda a comprar: "))
                    cantidad_comprar = int(input("Ingrese la cantidad a comprar: "))
                    
                    if 1 <= seleccion <= len(productos_categoria) and cantidad_comprar > 0:
                        producto_seleccionado = productos_categoria[seleccion - 1]
                        
                        if cantidad_comprar <= producto_seleccionado["existencia"]:
                            producto_seleccionado["existencia"] -= cantidad_comprar
                            self.carrito.append(producto_seleccionado)
                            print(f"Producto añadido al carrito: {producto_seleccionado['marca']}")
                        else:
                            print("No hay suficiente stock para la cantidad seleccionada.")
                    else:
                        print("Selección no válida.")

                    # Pregunta si desea seguir comprando
                    select = input("¿Desea seguir comprando? (si/no): ").lower()
                    
                    if select != "si":
                        Menu_Cliente.menu(self)  # Sale del bucle si la respuesta no es "si"
                except ValueError:
                    print("Por favor, ingrese un número válido.")

        except FileNotFoundError:
            print("No se encontró el archivo JSON de productos.")
        except json.JSONDecodeError:
            print("Error al recorrer el archivo JSON de productos.")

    def carrito_compras(self):
        print("Productos en el carrito:")
        for producto in self.carrito:
            print(f'Marca: {producto["marca"]}, Precio: {producto["costo"]}, Cantidad: {producto["cantidad"]}')

        total = sum(producto["costo"] * producto["cantidad"] for producto in self.carrito)
        print(f'Total de la compra: ${total}')

class Menu_Cliente():
     
     def __init__(self):
        self.cliente = Cliente("Nombre", "Apellido", "ID", "Teléfono", "Correo")
        self.carrito = []
     
     def menu(self):
            
            print("Menú de Cliente")
            print("1. Realizar Compra")
            print("2. Ver carrito")
            print("3. Enviar a facturar")
            print("4. Salir")

            try:
                option = int(input("Ingrese la opción: "))
            except ValueError:
                print("Opción no válida, vuelva a intentar.")
            else:
                match option:
                    case 1:
                       Cliente.realizar_compra(self)
                    case 2:
                        Cliente.carrito_compras(self)
                    case 3:
                        pass
                    case 4:
                        return True         
                    case default:
                        print("Opción no válida.")



            