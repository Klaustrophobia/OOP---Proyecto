## Toma informacion de archivos JSON
import json
## Hace invisible en el CMD las contrasenas
import getpass
## Proporciona una interfaz para interactuar con el OS en el que se está ejecutando el script.
import os

from Personal.personal import Personal
from  Producto.producto_generico import Producto_Generico

class Comprador(Personal):
    def __init__(self, proveedor, num_empleado, salario, nombre, apellido, identidad, telefono, correo):
        super().__init__(num_empleado, salario, nombre, apellido, identidad, telefono, correo)
        self.proveedor = proveedor
    
    def mostrar_productos(añadir):
        
        try:
            script_dir = os.path.dirname(__file__)
            file_path = os.path.join(script_dir, "../Credenciales/productos.json")

            with open(file_path, 'r') as file:
                lista_productos = json.load(file)
            categorias_disponibles = list(lista_productos.keys())

            #Productos existentes que conforman el combo
            cant_max_combos = []
            cant_max_combos.append(lista_productos["camisa"][0]["existencia"])
            cant_max_combos.append(lista_productos["sueter"][0]["existencia"])
            cant_max_combos.append(lista_productos["otrosProductos"][0]["existencia"])
            cant_max_combos.sort()
            #Remplaza el valor en existencia del combo con la cantidad del producto con menor exintencia.
            lista_productos["combo"][0]["existencia"] = cant_max_combos[0]
            
            with open(file_path,'w') as file:
                json.dump(lista_productos, file ,indent=4)               
            #Existencia de combos actualizada.

        except FileNotFoundError:
                print("\n--No se encontró el archivo JSON de productos.--")
        except json.JSONDecodeError:
                print("\n--Error al recorrer el archivo JSON de productos.--")
        else:

            seguir = True
            while (seguir):
                
                print("\n**** --Categorias Disponibles-- ****")
                for i, categoria in enumerate(categorias_disponibles, 1):
                    print(f"{i}. {categoria}")
                print(f"{len(categorias_disponibles) + 1}. salir")

                try:
                    opcion_categoria = int(input("Ingrese el número de la categoría: "))
                except ValueError:
                    print("\n--Opción No Válida. Inténtelo de nuevo.--")
                else:
                                    
                    if opcion_categoria == (len(categorias_disponibles) + 1):
                            seguir = False
                        
                    elif (1 <= opcion_categoria & opcion_categoria<= len(categorias_disponibles)):
                        categoria_seleccionada = categorias_disponibles[opcion_categoria - 1]
                        productos_categoria = lista_productos[categoria_seleccionada]

                        # Imprimir los productos de la categoría seleccionada
                        print(f"\n**** --Lista de productos ({categoria_seleccionada})-- ****")
                        
                        for j, producto in enumerate(productos_categoria, 1):
                                print(f'{j}. Marca: {producto["marca"]}, Precio: {producto["costo"]}, Stock: {producto["existencia"]}')

                        if añadir:
                            try:
                                seleccion = int(input("Seleccione Prenda para abastecer: "))
                                compra=int(input("Ingrese la cantiadad a comprar: ")) 
                            except ValueError:
                                print("\n--Opción No Válida. Inténtelo de nuevo.--")
                            else:
                                
                                if 1 <= seleccion <= len(productos_categoria) and compra >= 0:
                                    
                                    if categoria_seleccionada != "combo":
                                        lista_productos[categoria_seleccionada][seleccion-1]['existencia'] += compra
                                            
                                    else:
                                        #Se cambian tanto los combos como los demas productos.
                                        lista_productos[categoria_seleccionada][seleccion-1]['existencia'] += compra
                                        lista_productos["camisa"][0]["existencia"] += compra
                                        lista_productos["sueter"][0]["existencia"] += compra
                                        lista_productos["otrosProductos"][0]["existencia"] += compra
                                    
                                    with open(file_path,'w') as file:
                                        json.dump(lista_productos, file ,indent=4)               
                                    #Existencias de productos actualizada.
                                    
                                    print("\n--Producto Agregado con Éxito--")
                                    seguir = False
                                
                                else:
                                    print("\n--Opción No Válida. Inténtelo de nuevo.--")
                                
                    else:
                        print("\n--Opción No Válida. Inténtelo de nuevo.--")
        

    #crea un producto nuevo
    def producto_nuevo():
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, "../Credenciales/productos.json")
        with open(file_path, 'r') as file:
            lista_productos = json.load(file)
        
        producto_generico={}
        
        try:
            print(f"\n**** --Agregar Nuevo Producto-- ****")
            producto_generico['codigo']=input("Ingrese un Codigo: ")
            producto_generico['marca']=input("Ingrese la Marca: ")
            producto_generico['material']=input("Ingrese el material: ")
            producto_generico['costo']=int(input("Ingrese el costo: "))
            producto_generico['existencia']=int(input("Ingrese la existencia: "))
            producto_generico['tamano']=input("Ingrese el tamano: ")
        except ValueError:
            print("\n--Opción No Válida. Inténtelo de nuevo.--")
        else:
            lista_productos["otrosProductos"].append(producto_generico)
            with open(file_path, 'w') as file:
                json.dump(lista_productos,file,indent=4)

            print("\n--Producto Agregado con Éxito--")
   
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
                print(f'\n--Inicio de sesión exitoso. Bienvenido {u["nombre"]}.--')
                return True 
        return False 

    def login(self): 
        comprador = Login_Comprador.cargar_credenciales()  ##Mandar a llamar al metodo estatico dentro de la clase
        print("\n**** --Login de Comprador-- ****")
        numEmpleado = input("Numero de Empleado: ")
        password = getpass.getpass("Contrasena: ")

        if Login_Comprador.verificar_credenciales(numEmpleado, password, comprador):
            Menu.menu(self)
        else:
            print("\n--Credenciales incorrectas. Inténtelo de nuevo.--")
            return False
  
class Menu():
    def menu(self):
        seguir = True
        while (seguir):
            
            print("\n**** --Menú de Comprador-- ****")
            print("1. Rebastecer Inventario")
            print("2. Añadir Producto Nuevo")
            print("3. Mostrar Inventario")
            print("4. Salir")
            
            try:
                option = int(input("Ingrese la opción: "))
            except ValueError:
                print("\n--Opción No Válida. Inténtelo de nuevo.--")
            else:
                
                match option:
                    
                    case 1:
                       Comprador.mostrar_productos(True) 
                    
                    case 2:                
                        Comprador.producto_nuevo()
                    
                    case 3:
                        Comprador.mostrar_productos(False)
                    
                    case 4:
                        print("\n--Saliendo... Hasta Pronto.--")
                        seguir = False
                    
                    case default:
                        print("\n--Opción No Válida. Inténtelo de nuevo.--")
