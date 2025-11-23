nombres = ["Ana", "Luis", "Marta", "Carlos"]
#que lo recorra con un for y empiece el indice en 1
for indice, nomb in enumerate(nombres, start=1):
    print(indice, nomb)
#con list lo convertimos a lista de tuplas
tup = list(enumerate(nombres))
print(tup)