"""
Crea un script que:

Pida dos números al usuario.
Calcule la división de ambos.
Introduzca a propósito un error: usa num1 + num2 / 2 en lugar de (num1 + num2) / 2.
Ejecútalo en modo depuración en IntelliJ y observa qué valores toman las variables en cada paso.

"""

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

print(f"La división de la suma de {num1} y {num2} es {num1 + num2 / 2}")

