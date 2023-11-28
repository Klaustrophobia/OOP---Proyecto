import os
import json
import getpass

from .comprador import Comprador
from .vendedor import Vendedor

class Login_Admin():

    @staticmethod
    def cargar_credenciales(personal):
        credencial = f"../Credenciales/{personal}.json"
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, credencial)
        
        with open(file_path, "r") as file:
            data = json.load(file)
            return data["users"]
        
    @staticmethod
    def actualizar_credenciales(self, personal, lista_personal):
        credencial = f"../Credenciales/{personal}.json"
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, credencial)
        
        with open(file_path, "w") as file:
            dicc = {"users": lista_personal}
            json.dump(dicc, file, indent=4)

    @staticmethod
    def verificar_credenciales(user, password, admin):
        for u in admin:
            if u["user"] == user and u["password"] == password :
                print(f'\n--Inicio de sesión exitoso. Bienvenido {u["nombre"]}.--')
                return True 
        return False   

    def login(self): 
        admin = Login_Admin.cargar_credenciales("admin")  ##Mandar a llamar al metodo estatico dentro de la clase
        print("\n**** --Login de Admnistrador-- ****")
        user = input("Ingrese su Usuario: ")
        password = getpass.getpass("Ingrese su Contrasena: ")

        if Login_Admin.verificar_credenciales(user, password, admin):
            Menu.menu(self)

        else:
            print("\n--Credenciales incorrectas. Inténtelo de nuevo.--")
            return False

class Administrador(Vendedor, Comprador):
    def __init__(self, metas_ventas, ventas_netas, proveedor, num_empleado, salario, nombre, apellido, identidad, telefono, correo):
        Vendedor.__init__(self, metas_ventas, ventas_netas, num_empleado, salario, nombre, apellido, identidad, telefono, correo)
        Comprador.__init__(self, proveedor, num_empleado, salario, nombre, apellido, identidad, telefono, correo)
    
    def add_empleado(self, personal):
        
        seguir = True
        while (seguir):
            print(f"\n**** --Agregar Nuevo Personal [{personal}]-- ****")
            print("A continuacion llenar los siguientes espacios de manera cautelosa: ")
            try:
                nombre = input("Ingrese el nombre de la persona: ")
                apellido = input("Ingrese el apellido de la persona: ")
                identidad = int(input("Ingrese la identidad de la persona: "))
                telefono = int(input("Telefono: "))
                correo = input("Correo: ")
                numEmpleado = int(input("Numero de Empleado: "))
                password = input("Password para ingreso al sistema: ")
                salario = int(input("Salario: "))
            except ValueError:
                print("\n--Opción No Válida. Inténtelo de nuevo.--")
            else:

                if personal == "Comprador":
                    proveedor = input("Ingrese el proveedor del comprador: ")

                    lista_personal = Login_Admin.cargar_credenciales("comprador")

                    nuevo_personal = {
                        "nombre": nombre,
                        "apellido": apellido,
                        "identidad": identidad,
                        "telefono": telefono,
                        "correo": correo,
                        "numEmpleado": numEmpleado,
                        "password": password,
                        "salario": salario,
                        "proveedor": proveedor
                    }
                    
                    lista_personal.append(nuevo_personal)
                    self.actualizar_credenciales(self, "comprador", lista_personal)
                    seguir = False
                
                else:
                    
                    try:
                        metas_ventas = int(input("Metas de venta que debe tener mensual el vendedor: "))
                    except ValueError:
                        print("\n--Opción No Válida. Inténtelo de nuevo.--")
                    else:
                    
                        lista_personal = Login_Admin.cargar_credenciales("vendedor")

                        nuevo_personal = {
                            "nombre": nombre,
                            "apellido": apellido,
                            "identidad": identidad,
                            "telefono": telefono,
                            "correo": correo,
                            "numEmpleado": numEmpleado,
                            "password": password,
                            "salario": salario,
                            "metas_ventas": metas_ventas,
                            "ventas_netas": 0
                        }
                        lista_personal.append(nuevo_personal)
                        self.actualizar_credenciales(self, "vendedor", lista_personal)
                        seguir = False

    
    def delete_empleado(self, personal):
        
        count = 1
        print(f"\n**** --Eliminar Personal [{personal}]-- ****")
        
        if personal == "Comprador":
            empleados = Login_Admin.cargar_credenciales("comprador")
            
            for empleado in empleados:
                print(f"Empleado ({count}):\n-No. Empleado: {empleado['numEmpleado']}:\n-Nombre: {empleado['nombre']} {empleado['apellido']}\n-Identidad: {empleado['identidad']}\n-Teléfono: {empleado['telefono']}\n-Correo: {empleado['correo']}\n-Password: {empleado['password']}\n-Salario: {empleado['salario']}\n-Proveedor: {empleado['proveedor']}\n")
                count +=1
        else:
            empleados = Login_Admin.cargar_credenciales("vendedor")

            for empleado in empleados:
                print(f"Empleado ({count}):\n-No. Empleado: {empleado['numEmpleado']}:\n-Nombre: {empleado['nombre']} {empleado['apellido']}\n-Identidad: {empleado['identidad']}\n-Teléfono: {empleado['telefono']}\n-Correo: {empleado['correo']}\n-Password: {empleado['password']}\n-Salario: {empleado['salario']}\n-Meta de Venta: {empleado['metas_ventas']}\n-Ventas Netas: {empleado['ventas_netas']}\n")
                count +=1

        try:
            _option = int(input("Ingrese la opción: "))
        except ValueError:
            print("\n--Opción No Válida. Inténtelo de nuevo.--")
        else:
            if ((len(empleados) > 0) & (_option > 0) & (_option <= (len(empleados)))):
                empleados.pop(_option-1)
                
                if personal == "Comprador": 
                    self.actualizar_credenciales(self, "comprador", empleados)
                else:
                    self.actualizar_credenciales(self, "vendedor", empleados)

                print("\n--Personal Eliminado con Éxito--")
            else:
                print("\n--Opción No Válida. Inténtelo de nuevo.--")

    def add_producto(self):
        print("Ingrese de manera cautelosa los siguientes espacios: ")

    def delete_producto(self):
        print("Seleccione la categoria que desea revisar: ")

class Menu():

    def menu(self):        
        seguir = True
        while (seguir):
            print("\n**** --Menú de Admnistrador-- ****")
            print("1. Agregar Empleado")
            print("2. Eliminar Empleado")
            print("3. Agregar Producto")
            print("4. Eliminar Producto")
            print("5. Salir")

            try:
                option = int(input("Ingrese la opción: "))
            except ValueError:
                print("--Opción No Válida. Inténtelo de nuevo.--")
            else:
                
                match option:
                    
                    case 1:
                        _seguir = True
                        while (_seguir):
                            print("\n**** --Agregar Empleado-- ****")
                            print("1. Agregar Comprador")
                            print("2. Agregar Vendedor")
                            print("3. Cancelar")
                            
                            try:
                                _option = int(input("Ingrese la opción: "))
                            except ValueError:
                                print("--Opción No Válida. Inténtelo de nuevo.--")
                            else:
                                
                                match _option:
                                    
                                    case 1:
                                        Administrador.add_empleado(self, "Comprador")
                                        print("\n--Personal Agregado con Éxito--")
                                        _seguir = False
                                    
                                    case 2:
                                        Administrador.add_empleado(self, "Vendedor")
                                        print("\n--Personal Agregado con Éxito--")
                                        _seguir = False
                                    
                                    case 3:
                                        _seguir = False

                                    case default:
                                        print("--Opción No Válida. Inténtelo de nuevo.--")
                    
                    case 2:                
                        _seguir = True
                        while (_seguir):
                            print("\n**** --Eliminar Empleado-- ****")
                            print("1. Eliminar Comprador")
                            print("2. Eliminar Vendedor")
                            print("3. Cancelar")
                            
                            try:
                                _option = int(input("Ingrese la opción: "))
                            except ValueError:
                                print("--Opción No Válida. Inténtelo de nuevo.--")
                            else:
                                
                                match _option:
                                    
                                    case 1:
                                        Administrador.delete_empleado(self, "Comprador")
                                        _seguir = False
                                    
                                    case 2:
                                        Administrador.delete_empleado(self, "Vendedor")
                                        _seguir = False
                                    
                                    case 3:
                                        _seguir = False

                                    case default:
                                        print("--Opción No Válida. Inténtelo de nuevo.--")
                    
                    case 3:
                        pass
                    case 4:
                        pass

                    case 5:
                        print("\n--Sesion Cerrada Correctamente. Hasta Pronto.--")
                        seguir = False
                    
                    case default:
                        print("\n--Opción No Válida. Inténtelo de nuevo.--")