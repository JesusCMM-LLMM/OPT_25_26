import math
import os
# Hay que acordarse de hacer pip install requests en la terminal
import requests

"""Todos los errores de cada función los he sacado haciendo que se rompa el programa y cogiendo el código de error que me da """


def calculos_matematicos():
    try:
        num = int(input("Introduce un número entero: "))
        print(f"Raíz cuadrada: {math.sqrt(num)}")
        print(f"Factorial: {math.factorial(num)}")
        print(f"Potencia al cuadrado: {math.pow(num, 2)}") # bendito w3schools -> https://www.w3schools.com/python/module_math.asp
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")

def explorador_directorios():
    ruta_actual = os.getcwd()
    print(f"Directorio actual: {ruta_actual}")
    print("Archivos y carpetas:", os.listdir(ruta_actual))
    
    crear = input("¿Quieres crear una nueva carpeta? (si/no): ").lower()
    if crear == "si":
        n_carp = input("Nombre de la carpeta: ")
        try:
            os.mkdir(n_carp)
            print(f"Carpeta '{n_carp}' creada con éxito.")
        except FileExistsError:
            print("La carpeta ya existe.")
            
def consulta_api():
    url = "https://api.github.com"
    try:
        respuesta = requests.get(url)

        print(f"Código de estado: {respuesta.status_code}")
        print(f"Tamaño de la respuesta: {len(respuesta.text)} caracteres")
        print(f"Primeros 200 caracteres: {respuesta.text[:200]}")
    except requests.exceptions.ConnectionError:
        print("No hay conexión")

def menu():
    opcion = ""
    while opcion != "4":
        print("\n--- Menú de Herramientas ---")
        print("1. Cálculos matemáticos")
        print("2. Explorador de directorios")
        print("3. Consulta a API (requests)")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            calculos_matematicos()
        elif opcion == "2":
            explorador_directorios()
        elif opcion == "3":
            consulta_api()
        elif opcion == "4":
            print("Saliendo del programa.")
        else:
            print("Opción no válida. Intenta de nuevo.")

menu()