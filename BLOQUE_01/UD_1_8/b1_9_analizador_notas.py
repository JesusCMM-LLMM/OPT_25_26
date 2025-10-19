"""
Crea un script que:

Pida tres notas al usuario.
Calcule el promedio ( [n1 + n2 + n3] / 3 ).
Introduzca a propósito un error: usa n1 + n2 + n3 / 3 en lugar de lo anterior.
Ejecútalo en modo depuración en IntelliJ y observa qué valores toman las variables en cada paso.

"""

n1 = int(input("Introduce la primera nota: "))
n2 = int(input("Introduce la segunda nota: "))
n3 = int(input("Introduce la tercera nota: "))

# print(f"El promedio de las notas de {n1} y {n2} y {n3} es {n1 + n2 + n3 / 3}")
"""
 El comentario anterior es el promedio pero con un error lógico, abajo está corregido
 
"""
print(f"El promedio de las notas de {n1} y {n2} y {n3} es {(n1 + n2 + n3) / 3}")

