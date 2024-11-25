
file = open('data.csv')
lines = file.readlines()

for i in range(1, len(lines)):
    line = lines[i]
    parts = line.split(',')
    print(parts[1])