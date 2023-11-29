## Toma informacion de archivos JSON
import json
## Hace invisible en el CMD las contrasenas
import getpass
## Proporciona una interfaz para interactuar con el OS en el que se está ejecutando el script.
import os


from .personal import Personal
from  Producto.producto_generico import Producto_Generico

class Comprador(Personal):
    def __init__(self, proveedor, num_empleado, salario, nombre, apellido, identidad, telefono, correo):
        super().__init__(num_empleado, salario, nombre, apellido, identidad, telefono, correo)
        self.proveedor = proveedor

class Login_Comprador():
    @staticmethod
    def cargar_credenciales():
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "../Credenciales/comprador.json")
        
        with open(file_path, "r") as archivo:
            data = json.load(archivo)
            return data["users"]

    @staticmethod
    def verificar_credenciales(numEmpleado, password,comprador):
        for u in comprador:
            if u["numEmpleado"] == numEmpleado and u["password"] == password :
                print(f'Inicio de sesión exitoso para {u["nombre"]}')
                return True 
        return False 

    def login(self): 
        comprador = Login_Comprador.cargar_credenciales()  ##Mandar a llamar al metodo estatico dentro de la clase
        numEmpleado = input("Numero de Empleado: ")
        password = getpass.getpass("Contrasena: ")

        if Login_Comprador.verificar_credenciales(numEmpleado, password, comprador):
            Menu.menu(self)
        else:
            print("Credenciales incorrectas. Inténtelo de nuevo.")
            return False
        
    def mostrar_productos(añadir):
        try:
            script_dir = os.path.dirname(__file__)
            file_path = os.path.join(script_dir, "../Credenciales/productos.json")

            with open(file_path, 'r') as file:
                lista_productos = json.load(file)

            categorias_disponibles = list(lista_productos.keys())

            print("Categorias:")
            for i, categoria in enumerate(categorias_disponibles, 1):
                print(f"{i}. {categoria}")

            try:
                opcion_categoria = int(input("Ingrese el número de la categoría: "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                return
                                 
            if (1 <= opcion_categoria & opcion_categoria<= len(categorias_disponibles)):
                categoria_seleccionada = categorias_disponibles[opcion_categoria - 1]
                productos_categoria = lista_productos[categoria_seleccionada]

                # Imprimir los productos de la categoría seleccionada
                print(f"\nLista de productos ({categoria_seleccionada}):")
                for j, producto in enumerate(productos_categoria, 1):
                    print(f'{j}. Marca: {producto["marca"]}, Precio: {producto["costo"]}, Stock: {producto["existencia"]}')
                
                if añadir:
                    seleccion = int(input("Seleccione Prenda para abastecer: "))
                    producto_seleccionado=productos_categoria[seleccion-1]

                    compra=int(input("Ingrese la cantiadad a comprar: ")) 
                    
                    producto_seleccionado["existencia"]+=compra

                    
                    #inventario del producto aumenta existencia. 
                    lista_productos[categoria_seleccionada][seleccion-1]["existencia"]=producto_seleccionado["existencia"]
                    
                    with open(file_path,'w') as file:
                        json.dump(lista_productos, file ,indent=4)               
            
            else:
                print("Opción no válida.")
                return
        except:
            print("Opcion invalida:")
    #crea un producto nuevo
    def producto_nuevo():
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "../Credenciales/productos.json")
        with open(file_path, 'r') as file:
            lista_productos = json.load(file)
        producto_generico={}
        producto_generico['codigo']=input("Ingrese un Codigo: ")
        producto_generico['marca']=input("Ingrese la Marca: ")
        producto_generico['material']=input("Ingrese el material: ")
        producto_generico['costo']=input("Ingrese el costo: ")
        producto_generico['existencia']=input("Ingrese la existencia: ")
        producto_generico['tamano']=input("Ingrese el tamano: ")
        lista_productos["otrosProductos"].append(producto_generico)
        with open(file_path, 'w') as file:
            json.dump(lista_productos,file,indent=4)
        print("Producto añadido con exito")    
        pass
         
      
class Menu():
    def menu(self):
        while True:
            print("Menú de Comprador")
            print("1. Rebastecer Inventario")
            print("2. Añadir Producto Nuevo")
            print("3. Mostrar Inventario")
            print("4. Salir")
            
            try:
                option = int(input("Ingrese la opción: "))
            except ValueError:
                print("Opción no válida, vuelva a intentar.")
            else:
                match option:
                    case 1:
                       Login_Comprador.mostrar_productos(True) 
                    case 2:                
                        Login_Comprador.producto_nuevo()
                    case 3:
                        Login_Comprador.mostrar_productos(False)
                    case 4:
                        break
                    case default:
                        print("Opción no válida.")
