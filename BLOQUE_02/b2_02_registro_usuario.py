# He hecho este ejercicio algo más complejo de lo que podría para practicar basicamente
# He intentado que funcione el 100% de los casos y que además no haya que ejecutar el programa
# de nuevo para comprobar los tres ejemplos, por eso he definido la funcion reinicio

def reinicio():
    respuesta = input("¿Quieres reiniciar los ejemplos? S / N: " )
    if respuesta == "S":
        comprobacion()
    elif respuesta == "N":
        print("Cerrando programa...")
        exit()
    else: 
        print("Por favor, responde solo S o N")
        reinicio()


def registrar_usuario(nombre, edad, ciudad="Madrid"):
    """
    Se registra el usuario con datos como argumentos
    Acepta argumentos posicionales, nombrados y por defecto.
    """
    print(f"Usuario: {nombre}")
    print(f"Edad: {edad}")
    print(f"Ciudad: {ciudad}")
    reinicio()


# Ya que estamos, vamos a hacer las tres llamadas con un menú
def comprobacion():
    print("Selecciona una opción: ")
    print("1. Todos los argumentos posicionales.")
    print("2. Alguno omitido.")
    print("3. Nombrados en distinto orden.")
    opt = input("Opción? ")

    if opt == "1":
        # Se pasa nombre, edad y una ciudad específica
        registrar_usuario("Mario el delincuente", 20, "Moguer")
    elif opt == "2":
        # Solo se pasa nombre y edad; ciudad será "Madrid"
        registrar_usuario("Álvaro", 21)
    elif opt == "3":
        # Llamamos el nombre del parámetro
        registrar_usuario(ciudad="Sevilla", edad=36, nombre="Isco")
    else:
        print(f"Opción {opt} no válida.")
        comprobacion()


comprobacion()