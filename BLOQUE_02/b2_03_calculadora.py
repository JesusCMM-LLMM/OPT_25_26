"""
Igual que antes, he definido la funcion de reinicio para evitar el viaje al boton cada vez que petaba
Cada operación devuelve un resultado numérico, y por esto me ha causado dudas si poner en la funcion de division
el control de la division entre 0 o en el momento de pintarla 
[¿Podría hacerse con un while?]
"""

def sumar(a, b):
    return a + b


def restar(a, b):
    return a -b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return None 
    else:
        return a / b


def reinicio():
    respuesta = input("¿Quieres reiniciar los ejemplos? S / N: " )
    if respuesta == "S":
        calc()
    elif respuesta == "N":
        print("Cerrando programa...")
        exit()
    else: 
        print("Por favor, responde solo S o N")
        reinicio()


def calc():
    print("--- CALCULADORA BÁSICA ---")
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    # Los casteo a float para poder tener decimales
    print("---- RESULTADOS ----")
    print(f"Suma:           {sumar(num1, num2)}")
    print(f"Resta:          {restar(num1, num2)}")
    print(f"Multiplicación: {multiplicar(num1, num2)}")
    if dividir(num1, num2) == None:
        print(f"División:       No se puede realizar una división entre 0")
    else:
        print(f"División:       {dividir(num1, num2)}")
    reinicio()


calc()