nombres = ["Ana", "Pedro", "Alba", "Lucía", "Rafa", "Mario", "Álvaro"]

"""
Este programa recorre una lista de nombres y muestra en pantalla
solo aquellos que NO comienzan con la letra 'A' o 'a'.
Se utiliza un bucle for para iterar por la lista y la sentencia
'continue' para omitir los nombres que comienzan con 'A' o 'a'.
"""
# recorre la lista de nombres comprobando cada elemento
for n in nombres:
    if n.lower().startswith("a") or n.lower().startswith("á"):  # Convertimos el nombre a minúsculas (lower()) y comprobamos si empieza (startswith()) por 'a' o por 'á'
      # Si el nombre comienza con 'A' o 'a', se omite y se continúa con el siguiente
      continue                                                 
    print(f"Nombres válidos: {n}")