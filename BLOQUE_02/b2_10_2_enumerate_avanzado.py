#Declaramos las listas y resultado_final
estudiantes = ["Ana", "Luis", "Marta", "Carlos"]
notas_matematicas = [8, 7, 9, 6]
notas_fisica = [9, 6, 10, 7]
notas_quimica = [7, 8, 9, 5]
#Vamos a copiar mucho código del zip avanzado, dejando fuera la partte del diccionario
#Al desempaquetar, i captura el numero empezando por el 1
#y el parentesis sirve para para capturar la tupla interna del zip
for i, (nomb, mat, fis, quim) in enumerate(zip(estudiantes, notas_matematicas, notas_fisica, notas_quimica), start=1):
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
    #Ya pintamos cada elemento de la lista
    print(f"\n {i} {nomb} - Matemáticas: {mat}, Física: {fis}, Química: {quim}. Estado: {estado} \n")
