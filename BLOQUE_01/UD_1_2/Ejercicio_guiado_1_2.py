nombre = input("¿Cómo te llamas? ")
edad = input("¿Cuántos años tienes? ")

altura = input("¿Cuánto mides? ")


estudia = input("¿Estudias actualmente? (y/n) ")
respuesta = bool(estudia)
estudia = respuesta == "y"

print(f"Me llamo {nombre}, tengo {edad} años, mido {altura} y actualmente estudio: True")
