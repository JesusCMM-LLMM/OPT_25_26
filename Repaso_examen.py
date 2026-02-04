# Primer ejercicio: supuestamente algo de contar SIN USAR input()
# Funcion de contar con argumentos y una comprobación
"""
def contar(num1, num2):
    if num1 < num2:
        for n in range(num1, num2 + 1):
            print(n)
    else:
        for n in range(num2, num1 + 1):
            print(n)

contar(8, 2)
contar(2, 8)

# Calculadora:

def calc(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return None
        else:
            return num1 / num2
    else: 
        print("ERROR: OPERADOR DESCONOCIDO")

resultado = calc(3, "/", 0)

if resultado == None:
    print("No se puede dividir entre cero")
else:
    print(f"El resultado es {resultado}")
"""

"""
Define una función area_rectangulo(base, altura) que devuelva el área del rectángulo.

Define una función perimetro_rectangulo(base, altura) que devuelva el perímetro.

Desde el programa principal, pide al usuario la base y la altura, y muestra:

El área calculada.
El perímetro calculado.


def area_rectangulo(base, altura):
    base = int(base)
    altura = int(altura)
    return base * altura

def perimetro_rectangulo(base, altura):
    base = int(base)
    altura = int(altura)
    return 2 * base + 2 * altura


base = input("Introduce la base en cm: ")
altura = input("Introduce la altura en cm: ")
print(f" El area es {area_rectangulo(base, altura)}")
print(f" El perímetro es {perimetro_rectangulo(base, altura)}")

"""
"""
# Una lista con 6 frutas y vamos a modificar una, añadir una, borrar una

frutas = ["plátano", "uva", "manzana", "pera", "naranja", "melón"]

print(frutas)

#Añadir una fruta: 

frutas.append("ciruela")

print(frutas)
#Modificar una fruta:

frutas[0] = "sandía"
print(frutas)

# Borrar una 

frutas.remove("manzana")

print(frutas)
"""

#CRUD = Create, Read, Update y Delete - Repaso diccionarios
# Tenemos un diccionario vacío, y vamos a crear 4 funciones
# 1 Añade clientes
# 2 Lee el diccionario
# 3 Actualiza valores de un cliente en el diccionario
# 4 Borra un cliente 

clientes = {}
# Main dictionary: {nif: {name, age, city, profession}}

def crear_cliente():
    nif = input("Introduzca su DNI: ")
    nombre = input("Introduce tu nombre: ")
    edad = input("Introduce tu edad: ")
    ciudad = input("Introduce tu ciudad: ")
    
    clientes[nif] = {"Nombre": nombre, 
                     "Edad": edad, 
                     "Ciudad": ciudad}

def leer_cliente():
    for nif, datos in clientes.items():
        print(f"DNI: {nif} | Nombre: {datos["Nombre"]}, Edad: {datos["Edad"]}, Ciudad: {datos["Ciudad"]}")


def actu_cliente():
    nif = input("Introduzca el DNI a modificar: ")
    if nif in clientes: 
        print(f"El cliente con DNI {nif} es {clientes[nif]["Nombre"]}")
        nombre = input("Introduce el nuevo nombre: ")
        edad = input("Introduce la nueva edad: ")
        ciudad = input("Introduce la nueva ciudad: ")

        clientes[nif]["Nombre"] = nombre
        clientes[nif]["Edad"] = edad
        clientes[nif]["Ciudad"] = ciudad
    else: 
        print("El DNI no está registrado.")


def borrar_cliente():
    nif = input("Introduzca el DNI del cliente a borrar: ")
    if nif in clientes:
        del clientes[nif]
        print("Usuario eliminado correctamente.")
    else: 
        print("El DNI no está registrado.")



option = ""

while option != "5":
    print("\n=== PEOPLE CRUD MENU ===")
    print("1. Create person")
    print("2. Read people")
    print("3. Update person")
    print("4. Delete person")
    print("5. Exit")

    option = input("Choose an option: ")

    match option:
        case "1":
            crear_cliente()  
        case "2":
            leer_cliente()
        case "3":
            actu_cliente()
        case "4":
            borrar_cliente()
        case "5":
            print("Exiting program...")
        case _:
            print("Invalid option. Please choose 1–5.")


