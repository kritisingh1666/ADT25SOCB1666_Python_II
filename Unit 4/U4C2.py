import csv

count = 0

with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    
    for row in reader:
        count += 1

print("Total number of rows in CSV file:", count)
