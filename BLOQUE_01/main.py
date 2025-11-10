# 🔹 CRUD Template — using ID (NIF) as the key

people = {}  # Main dictionary: {nif: {name, age, city, profession}}


def create_person(person):
    """Create a new person and add to the dictionary."""
    key = person.get("DNI")
    people[key] = person


def read_people():
    """Display all registered people."""
    buscar_dni = input('Introduce el dni a buscar: ')
    if buscar_dni == people["DNI"]:
        print('DNI encontrado')
    else:
        print('DNI no encontrado')


def update_person():
    """Update information of an existing person."""
    key = people.get("dni")
    value = ''
    if key in people:
        people[key] = value
    else:
        print(f'{key} no encontrada')


def delete_person():
    """Delete a person by ID."""

    # 🔸 Main menu


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
            person = {}
            dni = input('Introduce tu DNI: ')
            if len(dni) == 9 and dni[-1].isalpha() and dni[1 - 8].isnumeric():
                print('DNI correcto')
                nombre = input('Introduce tu nombre: ')
                edad = input('Introduce tu edad: ')
                ciudad = input('Introduce tu ciudad: ')
                prof = input('Introduce tu profesión: ')

                person = {
                    "DNI": dni,
                    "nombre": nombre,
                    "edad": edad,
                    "ciudad": ciudad,
                    "profesión": prof
                }
                print(f'Usuario {nombre} creado correctamente')
            else:
                print('DNI incorrecto. Pruebe de nuevo')
                create_person(person)

        case "2":

            read_people()
        case "3":
            update_person()
        case "4":
            delete_person()
        case "5":
            print("Exiting program...")
        case _:
            print("Invalid option. Please choose 1–5.")
