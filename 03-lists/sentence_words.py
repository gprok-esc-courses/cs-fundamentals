# Ask user for a sentence
# Find how many words are in the sentence

flag = False
counter = 0

sentence = input("Give a sentence: ")

for i in range(len(sentence)):
    if sentence[i] == ' ':
        flag = False
    else: 
        if flag is False:
            counter += 1
        flag = True

print(counter)

# Same thing, pythonian way
words = sentence.split()
print(len(words))