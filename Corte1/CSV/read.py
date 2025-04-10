import csv

with open('leer_archivo.csv', mode='r', newline='') as archivo:
    lector = csv.reader(archivo)
    encabezado = next(lector)  # Leer la primera línea como encabezado
    for fila in lector:
        nombre, edad, ciudad = fila
        print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
