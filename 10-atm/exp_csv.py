import csv 

file = open('accounts.csv')

reader = csv.DictReader(file) 

for row in reader:
    print(row)