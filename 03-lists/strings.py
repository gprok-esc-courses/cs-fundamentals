
s = "This is a string"
s_lower = s.lower()

# Ask user for a character
c = input("Give a character: ")

# Find how many times character is in the string
counter = 0
for i in range(len(s)):
    if s_lower[i] == c:
        counter += 1

# print the result
print(counter)