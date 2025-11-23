numeros = [num for num in range(1,21)]
seguir = True
# print(numeros)
# Como de costumbre, lo voy a hacer un menú para que comprobarlo sea fácil

while seguir:
    print("Selecciona una opción: ")
    print("1. Lista con los cuadrados de todos los números.")
    print("2. Lista con solo los números pares.")
    print("3. Lista con los números mayores que 10.")
    print("4. Diccionario que relacione cada número con su doble")
    print("5. Salir. \n")
    opt = input("Opción? ")

    if opt == "1":
        cuadrados = [n ** 2 for n in numeros]
        print(cuadrados) 
    elif opt == "2":
        pares = [n for n in numeros if n % 2 == 0]
        print(pares)
    elif opt == "3":
        mayores = [n for n in numeros if n > 10]
        print(mayores)
    elif opt == "4":
        dobles = {n: n * 2 for n in numeros}
        print(dobles) 
    elif opt == "5":
        print("Saliendo..")
        seguir = False
    else:
        print("Opción incorrecta. Inténtalo de nuevo.")
