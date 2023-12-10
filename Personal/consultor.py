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

            except FileNotFoundError:
                print("\n--No se encontró el archivo JSON de productos.--")
            except json.JSONDecodeError:
                print("\n--Error al recorrer el archivo JSON de productos.--")
            else:

                seguir = True        
                while (seguir):
                
                    print("\n**** --Lista de Productos-- ****")
                    for categoria, productos in lista_productos.items():
                        
                        print(f"\n-Productos ({categoria}):")
                        for producto in productos:
                                print(f'Marca: {producto["marca"]}, Precio: {producto["costo"]}, Stock: {producto["existencia"]}')

                    seguir = False
                            
class Menu_Consultor():

    def menu(self):
            
            seguir = True
            while(seguir):
                print("\n**** --Menú de Consultor-- ****")
                print("1. Ver listado de productos")
                print("2. Volver al menú principal")

                try:
                    option = int(input("Ingrese la opción: "))
                except ValueError:
                    print("\n--Opción No Válida. Inténtelo de nuevo.--")
                else:
                    
                    match option:
                        
                        case 1:
                            Consultor.ver_productos(self)
                        
                        case 2:
                            print("\n--Saliendo... Hasta Pronto.--")
                            seguir = False       
                        
                        case default:
                            print("\n--Opción No Válida. Inténtelo de nuevo.--")
