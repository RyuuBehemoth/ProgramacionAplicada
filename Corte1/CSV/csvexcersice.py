import csv
import random
with open('text.csv', 'w') as csvfile:
    csv_writer = csv.writer(csvfile,delimiter=' ')
    
    while True:
        number = random.uniform(0,1)
        number = str(number)
        csv_writer.writerow(number)
