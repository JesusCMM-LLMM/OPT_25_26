num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
op = str(input("Introduce el operador: "))

# Versión con switch-case 
match op:
    case "+":
        print(f"Suma: {num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"Resta: {num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"Suma: {num1} * {num2} = {num1 * num2}")
    case "/":
        print(f"Suma: {num1} / {num2} = {num1 / num2}")
    case _:
        print("El operador no es válido")
