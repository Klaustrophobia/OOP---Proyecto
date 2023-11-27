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

class Login():
    @staticmethod
    def cargar_credenciales():
        script_dir = os.path.join(__file__)
        file_path = os.path.join(script_dir, "../Credenciales/comprador.json")

        with open(file_path, "r") as archivo:
            data = json.load(archivo)
            return data["users"]
        
    @staticmethod
    def verificar_credenciales(numEmpleado, password, vendedor):
        for credencial in vendedor:
            if credencial["numEmpleado"] == numEmpleado and credencial["password"] == password:
                return True
        return False   
    
    @staticmethod
    def login():
        vendedor = Login.cargar_credenciales()  ##Mandar a llamar al metodo estatico dentro de la clase
        numEmpleado = input("Numero de Empleado: ")
        password = getpass.getpass("Contrasena: ")

        if Login.verificar_credenciales(numEmpleado, password, vendedor):
            print(f"Inicio de sesión exitoso!")
        else:
            print("Credenciales incorrectas. Inténtelo de nuevo.")


class Menu():
    pass
