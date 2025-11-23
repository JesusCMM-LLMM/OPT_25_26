contador = 0

def incrementar():
    #Llamamos a la variable global contador y la incrementamos en 1
    global contador
    contador += 1


def decrementar():
    #Llamamos a la variable global contador y le restamos 1
    global contador
    contador -=1


def mostrar_contador():
    #Pintamos el valor actual de contador
    print(f"El valor actual del contador es: {contador}")

print("Ejecutando la función incrementar dos veces")
incrementar()
incrementar()

print("Ejecutando la función decrementar una vez")
decrementar()

print("Mostrando resultado")
mostrar_contador()

