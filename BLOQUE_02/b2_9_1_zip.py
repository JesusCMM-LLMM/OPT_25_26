#Primero declaramos las tres listas
nombres = ["Ana", "Luis", "Marta"]
notas_matematicas = [8, 7, 9]
notas_fisica = [9, 6, 10]
#Luego usamos un for para recorrer cada posicion de cada lista
for nomb, mat, fis in zip(nombres, notas_matematicas, notas_fisica):
    print(f"{nomb} - Matemáticas: {mat}, Física: {fis}")