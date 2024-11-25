
file = open('document.txt')

lines = file.readlines() 

print(lines)
for line in lines:
    line = line.strip()
    print(line)