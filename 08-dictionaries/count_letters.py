
sentence = input("Type a sentence: ")
sentence = sentence.lower()

letters = {}

for i in range(len(sentence)):
    ch = sentence[i]
    if ch == ' ':
        continue
    if ch in letters:
        letters[ch] += 1
    else:
        letters[ch] = 1

for key in letters:
    print(key, letters[key])
