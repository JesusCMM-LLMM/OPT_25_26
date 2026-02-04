#Declaramos las listas y resultado_final
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]
resultado_final = {}

#Hacemos las operaciones con el zip antes de meterlo al dicc
for nomb, mat, fis, quim in zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica):
    #Calculamos la media
    nota_media = round((mat + fis + quim) / 3, 2)
    #Con esto vamos a decir si esta aprobado, en rec o suspenso, metiendo el resultado del if en la variable vacía
    estado = ""
    if nota_media >= 6.5:
        estado = "Aprobado"
    elif nota_media >= 5:
        estado = "En recuperación"
    else:
        estado = "Suspenso"
    #metemos cada valor en el diccionario anidado
    resultado_final[nomb] = {
        "Matemáticas": mat,
        "Física": fis,
        "Química": quim,
        "Media": nota_media,
        "Estado": estado
    }

#Y ya lo pintamos con un for
for nombre, notas in resultado_final.items():
    print(f"{nombre} - Matemáticas: {notas['Matemáticas']}, Física: {notas['Física']}, Química: {notas['Química']}, Media: {notas['Media']}, Estado: {notas['Estado']}")