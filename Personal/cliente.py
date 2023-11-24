## Proporciona una interfaz para interactuar con el OS en el que se está ejecutando el script.
import os

from .persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, identidad, telefono, correo):
        super().__init__(nombre, apellido, identidad, telefono, correo)
        
    
    def menu(self):
        while True:
            print("Menú de Cliente")
            print("1. Ver Producto")
            print("2. Enviar a facturar")
            print("3. Salir")
            