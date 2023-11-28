## Toma informacion de archivos JSON
import json
## Hace invisible en el CMD las contrasenas
import getpass
## Proporciona una interfaz para interactuar con el OS en el que se está ejecutando el script.
import os

from .personal import Personal

class Comprador(Personal):
    def __init__(self, proveedor, num_empleado, salario, nombre, apellido, identidad, telefono, correo):
        super().__init__(num_empleado, salario, nombre, apellido, identidad, telefono, correo)
        self.proveedor = proveedor

class Menu():
    pass
