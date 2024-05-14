import csv

# Open the CSV file
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Output:
# ['Name', 'Age', 'Occupation']
# ['John', '30', 'Engineer']
# ['Jane', '28', 'Doctor']
