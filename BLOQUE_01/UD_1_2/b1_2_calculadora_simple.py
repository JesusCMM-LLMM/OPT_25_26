#Uso el try-except para que el programa de un mensaje de error si el usuario ingresa un valor que no sea un número 
#(Tb evito que el programa falle)
#  
try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    print(f"Suma: {num1} + {num2} = {num1 + num2}")
    print(f"Resta: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplicación: {num1} * {num2} = {num1 * num2}")
    
    #Aquí saco error si el numero por el que se va a dividir es cero (div y modulo)
    if num2 != 0:
        print(f"División: {num1} / {num2} = {num1 / num2}")
        print(f"Módulo: {num1} % {num2} = {num1 % num2}")
    else:
        print("División: Error, no se puede dividir entre cero")
        print("Módulo: Error, no se puede calcular el módulo con divisor cero")
    
    print(f"Potencia: {num1} ** {num2} = {num1 ** num2}")

except ValueError:
    print("Error: Por favor, ingresa solo números.")
