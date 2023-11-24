from .persona import Persona 
import json
import os

class Consultor(Persona):
    def __init__(self,  nombre, apellido, identidad, telefono, correo):
        super().__init__(nombre, apellido, identidad, telefono, correo)
        self.nombre = nombre
        self.apellido = apellido
        self.identidad = identidad
        self.telefono = telefono
        self.correo = correo

    
    def ver_productos():
        try:
            script_dir = os.path.dirname(__file__)
            file_path = os.path.join(script_dir, "../Credenciales/productos.json")

            with open(file_path, 'r') as file:
                productos = json.load(file)

            if productos:
                print("Lista de productos:")
                for producto in productos:
                    print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Stock: {producto['stock']}")
                else:
                    print("No hay productos disponibles.")

        except FileNotFoundError:
                print("No se encontró el archivo JSON de productos.")
        except json.JSONDecodeError:
                print("Error al decodificar el archivo JSON de productos.")
