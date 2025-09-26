usuario_correcto = "admin"
contrasena_correcta = "1234"

usuario = input("Nombre de usuario ")
contrasena = input("Contraseña ")

if (usuario == usuario_correcto) and (contrasena == contrasena_correcta):
    print("Acceso concedido")
else:
    print("Acceso denegado")
