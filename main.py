from  Personal.administrador import Login_Admin 
from  Personal.vendedor import Login_Vendedor
from  Personal.comprador import Login_Comprador
from  Personal.consultor import Menu_Consultor
from  Personal.cliente import Menu_Cliente

def main():

    login_admin = Login_Admin()
    login_vendedor = Login_Vendedor()
    login_comprador = Login_Comprador()
    menu_consultor = Menu_Consultor()
    menu_cliente = Menu_Cliente()

    seguir = True
    while (seguir): 
        
        print("\n**** --Bienvenido al Sistema, ¿Quién desea ingresar?-- ****")
        print("1. Administrador.")
        print("2. Vendedor.")
        print("3. Comprador.")
        print("4. Consultor.")
        print("5. Cliente.")
        print("6. Salir.")
        
        try:
            option = int(input("Ingrese la opcion: "))
        except:
            print("\n--Opción No Válida. Inténtelo de nuevo.--")
        else: 
                
                match option: 
                    
                    case 1:
                        login_admin.login()
                    
                    case 2:
                        login_vendedor.login()
                    
                    case 3: 
                        login_comprador.login()
                    
                    case 4:
                        menu_consultor.menu()
                    
                    case 5:
                        menu_cliente.menu()
                    
                    case 6:
                        print("\n--Saliendo... Hasta Pronto.--")
                        seguir = False
                    
                    case default:
                        print("\n--Opción No Válida. Inténtelo de nuevo.--")

if __name__ == "__main__":
    main()