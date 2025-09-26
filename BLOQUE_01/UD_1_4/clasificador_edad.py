try:
    edad = int(input("Introduce tu edad "))

    if (edad < 18):
        print("Eres menor de edad")
    elif (edad < 65):
        print("Eres adulto")
    else:
        print("Eres senior")

except ValueError:
    print("Error: Por favor, ingresa exclusivamente tu edad.")