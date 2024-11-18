import random

# Generate a random word
word_list = ["synchronize", "debugging", "inheritance",
             "polymorphism", "compiler", "interpreter",
             "microprocessor", "portability",
             "accessibility", "usability"]
rnd = random.randint(0, len(word_list)-1)
secret = word_list[rnd]

print(secret)

# Create the display (user word)
user_word = secret[0]
for i in range(len(secret) - 2):
    user_word = user_word + "-"
user_word = user_word + secret[-1]

print(user_word)

wrong = []
correct = []

print("HANGMAN GAME")
# Loop until user is hanged or word is found
while True:

    # Display word with underscores (user word)
    print(user_word)

    # Ask user to guess 
    letter = input("Guess next letter: ")

    # If guess is in the word add to a correct list 
    # and update the display word
    if letter in secret:
        correct.append(letter)
        user_word = secret[0]
        for i in range(1, len(secret) - 1):
            if secret[i] in correct:
                user_word = user_word + secret[i]
            else:
                user_word = user_word + "-"
        user_word = user_word + secret[-1]

    # Else add it to the wrong list
    else:
        if letter not in wrong:
            wrong.append(letter)

    # If wrong letters are 6, HANGED
    if len(wrong) == 6:
        print("Game Over: HANGED")
        break


    # If user word equals to the random word, FOUND
    if user_word == secret:
        print("Game Over: FOUND")
        break