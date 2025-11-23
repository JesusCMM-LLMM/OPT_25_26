agenda = {}
seguir = True

while seguir:
    print("Selecciona una opción: ")
    print("1. Añadir 3 contactos a la agenda.")
    print("2. Mostrar la agenda.")
    print("3. Buscar contacto por nombre.")
    print("4. Salir. \n")
    opt = int(input("Opción? "))

    if opt == 1:
        print("Por favor, introduce los datos de 3 contactos.")
        for i in range(3): #lo mismo que en el ejerc 5, hago la lista con un for
            print(f"\nContacto {i + 1}:")

            nombre = input("Nombre: ").title()  #el .title() convierte la primera letra de cada palabra a mayusc y el resto a minus
            telefono = input("Teléfono: ")

            # Se guarda como agenda[clave] = valor
            agenda[nombre] = telefono
        print("Contactos guardados. \n")   

    elif opt == 2:
        print("\n Mostrando los contactos: \n")
        # recorro el dict con un for
        for nombre, tlf in agenda.items():
            print(f"Nombre: {nombre} \t-> Teléfono: {tlf}") # el \t es una tabulación 

    elif opt == 3:
        buscar_nombre = input("\n ¿De quién buscas el número?: ").title()
        # vemos si el nombre está en la agenda, y si está devuelve el num
        if buscar_nombre in agenda:
            print(f"El teléfono de {buscar_nombre} es: {agenda[buscar_nombre]} \n ")
        else:
            print("Contacto no encontrado.")

    elif opt == 4:
        print("Saliendo..")
        seguir = False

    else:
        print("Opción incorrecta. Inténtalo de nuevo.")