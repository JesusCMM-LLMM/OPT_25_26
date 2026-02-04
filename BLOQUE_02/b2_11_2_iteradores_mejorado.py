estudiantes = {
    "Ana": [8, 7, 9],
    "Luis": [7, 6, 8],
    "Marta": [9, 10, 9],
    "Carlos": [6, 7, 5],
    "Laura": [10, 9, 10]
}

#Creamos el iterador y se recorre usando next() dentro de un while True
iterador_estudiantes = iter(estudiantes)
while True:
    # Obtenemos el siguiente nombre (clave)
    nombre = next(iterador_estudiantes, None)
    if nombre is None: #me daba error "KeyError" al llegar al None porque None no existe como clave en el diccionario
        break          #esto lo soluciona
    # Recuperamos las notas y calculamos la media
    notas = estudiantes[nombre]
    nota_media = round(sum(notas) / 3, 2)
        
   #Con esto vamos a decir si esta aprobado, en rec o suspenso, metiendo el resultado del if en una variable 
   #No hace falta declarar una variable vacía antes, pensaba que sí
    if nota_media >= 6.5:
        estado = "Aprobado"
    elif nota_media >= 5:
        estado = "En recuperación"
    else:
        estado = "Suspenso"
        
   #mostramos por pantalla
    print(f"{nombre} - Notas: {notas}, Media: {nota_media}, Estado: {estado}")