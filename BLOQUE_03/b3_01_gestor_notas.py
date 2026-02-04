"""
Programa: gestor_notas.py
Descripción: Aplicación de consola para gestionar un archivo de notas de texto.
Permite visualizar, añadir y eliminar notas con persistencia de datos.
"""
ARCHIVO = "notas.txt"

def ver_notas():
    # Lee el archivo y muestra las notas. Si no existe, lo crea.
    modo_lectura = "r"
    try:
        # Intentamos abrirlo directamente
        with open(ARCHIVO, modo_lectura) as f:
            lineas = f.readlines()
            if not lineas:
                print("El archivo está vacío.")
            else:
                print("\nNotas actuales:")
                for i, linea in enumerate(lineas, start=1): # El enumerate nos sirve para que, cuando borremos, no se queden numeros sueltos por ahí
                    print(f"{i}. {linea.strip()}")

    except FileNotFoundError:
        # Si el archivo no existe, lo creamos
        print(f"Archivo no encontrado. Creando {ARCHIVO}...")
        modo_escritura = "w"
        with open(ARCHIVO, modo_escritura) as f:
            pass # Solo lo abrimos en modo escritura para que se cree vacío
    except PermissionError:
        print("Error: No tienes permisos para acceder al archivo.")


def añadir_nota():
    """Pide texto al usuario y lo añade al final del archivo."""
    nueva_nota = input("Escribe la nueva nota: ")
    modo = "a"
    try:
        with open(ARCHIVO, modo) as f:
            f.write(nueva_nota + "\n")
        print("Nota guardada con éxito.")
    except PermissionError:
        print("Error: No tienes permisos para escribir en el archivo.")


def eliminar_nota():
    """Pide el índice de la nota y la elimina reescribiendo el archivo."""
    try:
        # Primero leemos las notas existentes en modo lectura y metemos lo que haya
        # (leído con f.readlines) en la lista lineas
        modo_lectura = "r"
        with open(ARCHIVO, modo_lectura) as f:
            lineas = f.readlines()
        
        if not lineas: # Si la lista lineas está vacía, te lo dice y sale
            print("No hay notas para eliminar.")
            return

        indice = int(input("Número de nota a eliminar: ")) - 1 # aquí capturamos el indice y le ponemos el -1 porque python empieza en el 0
        
        if 0 <= indice < len(lineas): # ESTO ASEGURA QUE EL NUMERO INTRODUCIDO COMO INDICE ESTÉ DENTRO DEL RANGO DE LA LISTA. ELEGANTE, ¿VERDAD?
            lineas.pop(indice)
            # Eliminamos de la lista lineas y reescribimos
            modo_escritura = "w"
            with open(ARCHIVO, modo_escritura) as f:
                f.writelines(lineas) # writelines es un método como write pero para listas, 
                                     #escribe cada elemento de la lista como una línea en el archivo. 
                                     # -> https://www.w3schools.com/python/ref_file_writelines.asp
            print("Nota eliminada correctamente.")
        else:
            print("Error: El número de nota no existe.")
            
    except ValueError:
        print("Error: Por favor, introduce un número válido.")
    except PermissionError:
        print("Error: No tienes permisos para modificar el archivo.")


def menu():
    """Ejecuta el bucle principal del programa."""
    print("Gestor de Notas")
    ver_notas()

    opcion = "" # Inicializamos la variable para que el while pueda leerla, ya que no te molan los while True

    while opcion != "4":
        print("\n--- Menú ---")
        print("1. Ver notas")
        print("2. Añadir nota")
        print("3. Eliminar nota")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            ver_notas()
        elif opcion == "2":
            añadir_nota()
        elif opcion == "3":
            eliminar_nota()
        elif opcion == "4":
            print("\nSaliendo..")
        else:
            print("Opción no válida, intenta de nuevo.")

menu()