
# open the file
file = open('literature.txt')

# read the lines
lines = file.readlines()

# initialize a counter to zero
counter = 0
char_counter = 0

# for each line
for line in lines:
    # split the line into words 
    words = line.split()
    # add the number of words to the counter
    n = len(words)
    counter += n
    char_counter += len(line.strip())

# print the counter
print(counter)
print(char_counter)