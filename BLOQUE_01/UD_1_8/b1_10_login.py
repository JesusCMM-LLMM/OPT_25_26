"""
Programa de registro, no podemos usar funciones, ni diccionarios, ni arrays, ni tuplas.
Solo va a recibir un usuario con su contraseña y comprobaremos si se loguea o no

"""
username = "" #El motivo de que estén declaradas vacías aquí es para despues usarlas de comprobacion en el login
password = "" #Por si alguien se salta el paso 1

while True:
    print("|######################################|")
    print("|#############   MENÚ   ################|")
    print("|######################################|")
    print("| [1].- Registrarse                    |")
    print("| [2].- Iniciar sesión                 |")
    print("| [3].- Salir                          |")
    print("|######################################|")

    # Meto el input, la opcion, en un try-except por si el usuario escribe cualquier otra cosa en vez de un número.
    try:
        opt = int(input("        Introduce tu opción: "))
    except ValueError:
        print("Opción no válida. Introduce solo un número (1, 2 o 3).")
        continue # Esto nos manda al inicio del while True

    if (opt == 1):
        username = input("Introduce usuario a registrar: ")
        car_no_perm_usu = ['!', '#', '$', '%', '&', '*', '?'] # Caracteres no permitidos en el usuario

        while ( #agrupo todas las condiciones con or aunque no sea lo más óptimo
            len(username) <= 3 or
            '@' not in username or
            not (username.endswith('.com') or username.endswith('.es') or username.endswith('.net')) or
            any(c in username for c in car_no_perm_usu)
        ):
            print("El usuario debe tener más de 3 caracteres, contener '@', terminar en .com, .net o .es y no incluir caracteres especiales (!, #, $, %, &, *, ?)")
            username = input("Introduce un nombre de usuario válido: ")

        print(f"Usuario {username} válido")
        
        # Ahora pasariamos a los requisitos d econtraseña
        car_esp_permitidos = ['!', '#', '$', '%', '&', '*', '?', '@'] # Caracteres especiales que si se permiten para la contraseña        
        password = input("Introduce la nueva contraseña: ")
        
        while ( #de nuevo se que quizá no es lo más óptimo, pero creo que la función any() actúa como un flag y no recorre todos los caracteres si no es necesario.
            len(password) < 8 or
            not any(c.isupper() for c in password) or 
            not any(c.isnumeric() for c in password) or
            not any(c in car_esp_permitidos for c in password) 
        ):
            print("La contraseña debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula, un número y un carácter especial (!, @, #, $, %, &, *, ?).")
            password = input("Introduce una nueva contraseña: ")
        
        print("Contraseña creada correctamente") 
        print(f"Usuario {username} registrado correctamente.") 

    elif (opt == 2):
        if not username: # Comprueba si la variable username está vacía
            print("No hay ningún usuario registrado. Por favor, regístrese primero (Opción 1).")
        else: # Si hay usuario, ya te lo pide
            usu_comp = input("Introduce tu usuario: ")
            if usu_comp == username:
                cont = 0 #el contador que cuando a llegue a 3 te dejará sin intentos
                acceso_concedido = False # flag de acceso                
                while (cont < 3):
                    cont_comp = input("Usuario correcto. Introduce tu contraseña: ")
                    if cont_comp == password:
                        print("Acceso concedido")
                        acceso_concedido = True
                        break # Rompe el bucle de intentos porque se concede acceso
                    else: # La contraseña es incorrecta, se suma 1 al contador y vuelta al bucle
                        cont += 1
                        print(f"Contraseña incorrecta. Te quedan {3 - cont} intentos.")
                if acceso_concedido == False and cont == 3: #Si no se ha accedido y el contador ya está en 3, patrás
                    print("Demasiados intentos fallidos. Regresando al menú principal.")
            
            else:
                print("Usuario no encontrado. Acceso denegado")

    elif (opt == 3):
        print("Saliendo..")
        exit()
    else:
        print("Opción incorrecta. Introduce 1, 2 o 3.")
