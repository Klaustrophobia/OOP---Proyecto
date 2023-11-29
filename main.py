from  Personal.administrador import Login_Admin 
from  Personal.vendedor import Login_Vendedor
from  Personal.consultor import Menu_Consultor
from  Personal.cliente import Menu_Cliente
from  Personal.comprador import Login_Comprador

def main():
    login_vendedor = Login_Vendedor()
    menu_consultor = Menu_Consultor()
    menu_cliente = Menu_Cliente()
    login_admin = Login_Admin()
    login_comprador = Login_Comprador()

    while True: 
        try:
            print("\nBienvenido")
            print("1. Administrador")
            print("2. Vendedor")
            print("3. Comprador")
            print("4. Consultor")
            print("5. Cliente")
            print("6. Salir")
        except:
            print("Opcion no valida, vuelva a intentar")
        else: 
                option = int(input("Ingrese la opcion: "))
                print()

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
                        break
                    case default:
                        print("ERROR DE OPCION NO EXISTENTE")

if __name__ == "__main__":
    main()
