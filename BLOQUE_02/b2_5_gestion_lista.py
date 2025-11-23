# Refinando el tema de la función reinicio, creo que para funciones trochas como estas va bien, pero
# en un codigo de mil funciones, si las llamo todo el rato voy a necesitar 100Gb de ram
# Así que he pensado que usar un bucle con una condicion verdadera es más optimo
# Como me dijiste que usar un while true no es reocmendado he usado una variable

seguir = True
compra = []


while seguir:
    print("Selecciona una opción: ")
    print("1. Añadir 5 productos a la lista de la compra.")
    print("2. Mostrar la lista.")
    print("3. Eliminar un producto.")
    print("4. Ordenar la lista alfabéticamente.")
    print("5. Salir.")

    opt = input("Opción? ")

    if opt == "1":
            print("Introduce los productos:")
            for i in range(5):
            #En vez de poner cinco prints, lo hago recorriendo con un for dándole rango de 5 prd máximo, repite todo lo que está debajo 5 veces
            #Como en el for se empieza por la posicion 0, le sumo 1 a cada posicion 
                producto = input(f"Producto {i + 1}: ").lower()  #El .lower() lo convierte todo a minusc y asi evito problemas al eliminar elementos despues
                compra.append(producto)   
            print("Productos añadidos a la lista")
    elif opt == "2":
        print("Mostrando la lista")
        print(compra)
    elif opt == "3":
        prod_eliminado = input("Señala el producto a eliminar de la lista: ").lower()
        if prod_eliminado in compra:
            compra.remove(prod_eliminado)
            print(f"El producto {prod_eliminado} ha sido eliminado de la lista.")
        else: 
            print("El producto no está en la lista.")
    elif opt == "4":
        print("Ordenando la lista alfabéticamente...")
        compra.sort()
        print(compra)
    elif opt == "5":
        print("Saliendo...")
        seguir = False
    else:
        print(f"Opción {opt} no válida. Selecciona una opción entre 1 - 5")



