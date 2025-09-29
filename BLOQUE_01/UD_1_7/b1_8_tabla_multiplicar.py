"""
Este programa pide al usuario un número y t devuelve su tabla de multiplicar
He añadido además el metodo try/except para el manejo de errores.

"""

try: # Try para manejo de errores
    num = int(input("Introduce el número: ")) # pide el numero por teclado
    for i in range (1,11): # Con esto recorremos todos los números entre el 1 y el 11, sin incluir este último
        print(f"({num} multiplicado por {i} es {num * i})")  # mostramos por pantalla la operación del numero introducido por cada numero del rango

except ValueError: # Esto impide que el programa crashee si le introducimos un tipo de dato incorrecto; en su lugar nos da un mensaje de error
    print("Necesito un valor numérico")