
# ask user for a filename
filename = input("Give filename: ")
# open the file for writing
file = open(filename, 'a')

# LOOP
while True:
    # Ask user for a sentence (END to stop)
    sentence = input("Type a senetnce (END to stop): ")
    # if user typed END, stop
    if sentence == 'END':
        break
    # else, write the sentence into the file
    else:
        file.write(sentence + '\n')