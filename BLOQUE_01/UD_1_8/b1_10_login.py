"""
 Requisitos del programa
El programa debe mostrar un menú principal con tres opciones:

[1]. Registrarse → El usuario crea un nuevo nombre de usuario y contraseña.
[2]. Iniciar sesión → El usuario introduce su nombre y contraseña para acceder.
[3]. Salir → Finaliza el programa.
Registro de usuario:

La información del usuario se almacenará en variables:

identifier es el email del usuario de usuario.
password es la contraseña asociada.

Antes de aceptar el identificador, debes validarla con estas reglas:
    Mínimo 3 caracteres.
    Contener al menos @.
    Contener al menos alguna de las siguientes extensiones .com, .es, .net.
    No debe contener símbolos especiales como (!@#$%&*?, etc.).


Antes de aceptar la contraseña, debes validarla con estas reglas:
    Mínimo 8 caracteres.
    Contener al menos una mayúscula.
    Contener al menos un número.
    Contener al menos un símbolo especial (!@#$%&*?, etc.).
        Si no cumple las reglas → muestra un mensaje de error y vuelve a pedir el usuario o la contraseña.

Inicio de sesión:

Verifica si el usuario (email) existe.

Si existe y la contraseña es correcta → muestra “Acceso concedido ✅”.

Si el usuario no existe o la contraseña es incorrecta → muestra “Acceso denegado ⛔”.

El usuario tendrá un máximo de 3 intentos para introducir su contraseña correctamente.

Si falla las 3 veces seguidas → mostrar “Demasiados intentos fallidos 🚫. Regresando al menú principal.” y volver al menú.
El programa debe ejecutarse en bucle hasta que el usuario elija la opción Salir.

"""
print("|######################################|")
print("|#############  MENÚ   ################|")
print("|######################################|")
print("| [1].- Registrarse                    |")
print("| [2].- Iniciar sesión                 |")
print("| [3].- Salir                          |")
print("|######################################|")

opt = int(input("       Introduce tu opción: "))

if (opt == 1):
    username = input("Introduce usuario a registrar: ")
    if len(username) < 3 :
        print(f"El usuario debe tener más de 3 caracteres")
    elif '@' not in username:
        print(f"El usuario debe contener una @")
    elif not (username.endswith('.com') or username.endswith('.es') or username.endswith('.net')):
        print(f"El usuario debe terminar en .com, .es o .net")
    elif re.search(r'[!#\$%&\*\?]', username):  # símbolos especiales no permitidos
        print(f"El usuario no debe tener caracteres especiales")
    else:
        print(f"Usuario {username} creado correctamente")
else:
    print("Te queda código por hacer, chaval")









