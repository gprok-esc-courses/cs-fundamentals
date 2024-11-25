
file = open('document.txt')
destination = open('document_copy.txt', 'w')

lines = file.readlines()

for line in lines:
    destination.write(line)