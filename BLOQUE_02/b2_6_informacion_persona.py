#Creación de la tupla
persona = ("Ana", 27, "Isla")

#Desempaquetamiento de la tupla
nombre, edad, ciudad = persona

#Salida de la información (he aprendido a usar saltos de líneas)

print("\n--- Información de la Persona ---\n")
print(f"Nombre: {nombre}\n")
print(f"Edad:   {edad} años\n")
print(f"Ciudad: {ciudad}\n")

#También podemos recorrer los datos al porrón con un for

for info in persona:
    print(info)