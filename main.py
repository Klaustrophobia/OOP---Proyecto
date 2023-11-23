from  Personal.vendedor import Login

def main():
    login_vendedor = Login()

    try:
        print("Bienvenido")
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

        match option: 
            case 1:
                pass
            case 2:
                if login_vendedor.login():
                    pass
            case 3: 
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case default:
                print("ERROR DE OPCION NO EXISTENTE")

if __name__ == "__main__":
    main()
