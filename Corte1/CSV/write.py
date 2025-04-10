import csv

datos = [
    ['nombre', 'edad', 'ciudad'],
    ['Carlos', 28, 'Sevilla'],
    ['Lucía', 32, 'Bilbao'],
    ['Jorge', 29, 'Zaragoza']
]

with open('escribir_archivo.csv', mode='w', newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

print("Archivo CSV escrito correctamente.")
