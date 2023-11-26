from .persona import Persona
import os
import json 

class Consultor(Persona):
    def __init__(self,  nombre, apellido, identidad, telefono, correo):
        super().__init__(nombre, apellido, identidad, telefono, correo)
        self.nombre = nombre
        self.apellido = apellido
        self.identidad = identidad
        self.telefono = telefono
        self.correo = correo

    def ver_productos(self):
            try:
                script_dir = os.path.dirname(__file__)
                file_path = os.path.join(script_dir, "../Credenciales/productos.json")

                with open(file_path, 'r') as file:
                    lista_productos = json.load(file)

                for categoria, productos in lista_productos.items():
                    print(f"\nLista de productos ({categoria}):")
                    print() #Salto de linea
                    for producto in productos:
                        print(f'Nombre: {producto["codigo"]}, Marca: {producto["marca"]}, Precio: {producto["costo"]}, Stock: {producto["existencia"]}')
                    print() 

            except FileNotFoundError:
                print("No se encontró el archivo JSON de productos.")
            except json.JSONDecodeError:
                print("Error al recorrer el archivo JSON de productos.")

            # Pregunta al usuario si desea volver al menú principal
            volver = input("Desea volver al menú principal? (Si/No): ").lower()
            if volver == "si":
                print()
                Menu.menu(self)  # Llama al método menu dentro de la clase Menu
            elif volver != "no":
                print("Opción no válida. Volviendo al menú principal.")
                Menu.menu(self)

class Menu():

    def menu(self):
            print("Consulta de productos")
            print("1. Ver listado de productos")
            print("2. Volver al menú principal")

            try:
                option = int(input("Ingrese la opción: "))
            except ValueError:
                print("Opción no válida, vuelva a intentar.")
            else:
                match option:
                    case 1:
                        Consultor.ver_productos(self)
                    case 2:
                        return True         
                    case default:
                        print("Opción no válida.")
