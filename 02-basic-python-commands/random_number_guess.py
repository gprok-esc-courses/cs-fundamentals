import random

# generate random number 1-100
secret = random.randint(1, 100)
print(secret)

answer = 0
counter = 0
while answer != secret:
    if counter > 5:
        print("Not found. Exceed 5 guesses")
        break
    answer = int(input("Guess: "))
    # counter = counter + 1
    counter += 1
    if answer > secret:
        print("Go Down")
    elif answer < secret:
        print("Go Up")
    else:
        print("Found in", counter, "guesses")