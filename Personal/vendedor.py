## Toma informacion de archivos JSON
import json
## Hace invisible en el CMD las contrasenas
import getpass
## Proporciona una interfaz para interactuar con el OS en el que se está ejecutando el script.
import os

from Personal.personal import Personal

class Login():
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
                return True
        return False   

    def login(self): 
        vendedor = Login.cargar_credenciales()  ##Mandar a llamar al metodo estatico dentro de la clase
        numEmpleado = input("Numero de Empleado: ")
        password = getpass.getpass("Contrasena: ")
        ##Hacer que imprima el nombre del vendedor que esta ingresado

        if Login.verificar_credenciales(numEmpleado, password, vendedor):
            print(f"Inicio de sesión exitoso para!")
            return True
        else:
            print("Credenciales incorrectas. Inténtelo de nuevo.")
            return False


class Vendedor(Personal):
    def __init__(self, metas_ventas, ventas_netas, num_empleado, salario, nombre, apellido, identidad, telefono, correo):
        super().__init__(num_empleado, salario, nombre, apellido, identidad, telefono, correo)
        self.metas_ventas = metas_ventas
        self.ventas_netas = ventas_netas

    def realizar_venta(self):
        pass

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
                    self.realizar_venta()  # Puedes llamar a otros métodos de la instancia si es necesario
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case default:
                    print("Opción no válida.")
