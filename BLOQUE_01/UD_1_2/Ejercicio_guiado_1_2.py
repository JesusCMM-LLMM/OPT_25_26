nombre = input("¿Cómo te llamas? ")
edad = int(input("¿Cuántos años tienes? "))

altura = float(input("¿Cuánto mides? "))


estudia = input("¿Estudias actualmente? (y/n) ") # == "y"

if (estudia == "y"):
    resp = "sí"
elif (estudia == "n"):
    resp = "no"
else:
    resp = "no se si"

print(f"Me llamo {nombre}, tengo {edad} años, mido {altura} y actualmente {resp} estudio")


