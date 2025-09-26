try:
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    op = str(input("Introduce el operador: "))

    if (op == "+"):
        print(f"Suma: {num1} + {num2} = {num1 + num2}")
    elif (op == "-"):
        print(f"Resta: {num1} - {num2} = {num1 - num2}")
    elif (op == "*"):
        print(f"Suma: {num1} * {num2} = {num1 * num2}")
    elif (op == "/"):
        print(f"Suma: {num1} / {num2} = {num1 / num2}")
    else:
        print("El operador no es válido")

except ValueError:
    print("Introduce valores válidos")
