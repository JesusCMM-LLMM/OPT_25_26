"""
 Este es el menú sin funciones. Lo primero, para no usar funciones y que solo se cierre al usar la opcion 3, el menú está dentro de un while True.
 Segundo, los arrays vacíos van fuera del bucle para que no se reinicien en cada vuelta.
 NO HEMOS USADO FUNCIONES aunque venía así en la rúbrica de la entrega porque no estaban dentro de este bloque 01
"""

usu_reg = []
cont_reg = []

while True:
    print("|######################################|")
    print("|#############  MENÚ   ################|")
    print("|######################################|")
    print("| [1].- Registrarse                    |")
    print("| [2].- Iniciar sesión                 |")
    print("| [3].- Salir                          |")
    print("|######################################|")

    # La opción como una variable que va a leerse en el if/elif/else
    opt = int(input("       Introduce tu opción: "))

    if (opt == 1):
        username = input("Introduce usuario a registrar: ")
        car_no_perm = ['!', '#', '$', '%', '&', '*', '?']  # defino una variable con los caracteres no permitidos que
        # vamos a usar tanto en usuario como en contraseña
        while (  # he agrupado todas las condiciones a cumplir con el while
                len(username) <= 3 or
                '@' not in username or
                not (username.endswith('.com') or username.endswith('.es') or username.endswith('.net')) or
                any(c in username for c in car_no_perm)
        ):
            print(
                "El usuario debe tener más de 3 caracteres, contener '@', terminar en .com, .net o .es y no incluir caracteres especiales (!, #, $, %, &, *, ?)")
            username = input("Introduce un nombre de usuario válido: ")  # mensaje de que las condic son válidas

        print(f"Usuario {username} válido")
        password = input("Introduce la nueva contraseña: ")
        while (  # igual que en el usuario, agrupo las condiciones
                len(password) < 8 or
                not any(c.isupper() for c in password) or
                not any(c.isnumeric() for c in password) or
                not any(c in car_no_perm for c in password)
        ):
            print(
                "La contraseña debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula y un carácter especial (!, @, #, $, %, &, *, ?).")
            password = input("Introduce una nueva contraseña: ")
            print("Contraseña creada correctamente")
        # con el append unimos el usuario y la contraseña al array vacío que hemos declarado antes del while
        usu_reg.append(username)
        cont_reg.append(password)
        print(f"´{usu_reg} registrado correctamente.")

    elif (opt == 2):
        cont = 0
        while (cont <= 3):
            usu_comp = input("Introduce el usuario con el que quieres iniciar sesión: ")
            cont_comp = input("Introduce su contraseña: ")
            # vamos a comprobar que el usuario esté y después a comprobar en qué posición del array está
            # y que la contraseña de esa posición coincida
            if usu_comp in usu_reg:
                indice = usu_reg.index(
                    usu_comp)  # vamos a llamar al indice del array creado antes para comparar posiciones
                if cont_comp == cont_reg[indice]:
                    print("Acceso concedido")
                    break
                else:
                    cont += 1
                    print("Contraseña incorrecta. Inténtalo de nuevo.")
                    if cont == 3:
                        print("Demasiados intentos fallidos. Regresando al menú principal.")
            else:
                print("Usuario no encontrado. Acceso denegado")
                break
    elif (opt == 3):
        print("Saliendo..")
        exit()
    else:
        print("Opción incorrecta")
