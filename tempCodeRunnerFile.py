admin = cargar_credenciales()
    user = input("Usuario: ")
    password = getpass.getpass("Contrasena: ") ## Getpass es para volver invisible la contrasena

    if verificar_credenciales(user, password, admin):
        print("¡Inicio de sesión exitoso!")
    else:
        print("Credenciales incorrectas. Inténtelo de nuevo.")
