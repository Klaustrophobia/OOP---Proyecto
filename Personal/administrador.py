import os
import json
import getpass

from .comprador import Comprador
from .vendedor import Vendedor

class Login_Admin():

    @staticmethod
    def cargar_credenciales():
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "../Credenciales/admin.json")
        
        with open(file_path, "r") as archivo:
            data = json.load(archivo)
            return data["users"]

    @staticmethod
    def verificar_credenciales(user, password, admin):
        for u in admin:
            if u["user"] == user and u["password"] == password :
                print(f'Inicio de sesión exitoso para {u["nombre"]}')
                return True 
        return False   

    def login(self): 
        admin = Login_Admin.cargar_credenciales()  ##Mandar a llamar al metodo estatico dentro de la clase
        user = input("Usuario: ")
        password = getpass.getpass("Contrasena: ")

        if Login_Admin.verificar_credenciales(user, password, admin):
            Menu.menu(self)
        else:
            print("Credenciales incorrectas. Inténtelo de nuevo.")
            return False


class Admnistrador (Comprador, Vendedor):
    def __init__(self):
        pass
    
    def add_empleado(self):
        pass

    def delete_empleado(self):
        pass
    
    def add_producto(self):
        pass

    def delete_producto(self):
        pass

class Menu():

    def menu(self):
        print("Menú de Admnistrador")
        print("1. Agregar Empleado")
        print("2. Eliminar Empleado")
        print("3. Agregar Producto")
        print("4. Eliminar Producto")
        print("5. Salir")

        try:
            option = int(input("Ingrese la opción: "))
        except ValueError:
            print("Opción no válida, vuelva a intentar.")
        else:
            match option:
                case 1:
                    pass
                case 2:                
                    pass
                case 3:
                    pass
                case 5:
                    return True
                case default:
                    print("Opción no válida.")