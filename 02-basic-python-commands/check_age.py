print('Restricted entry app')

age = input("Give your age: ")
age = int(age)
print(age)

if age < 18:
    print("No pass, too young")
elif age < 50:
    print("OK")
    print("Go on")
else:
    print("No pass, too old")

print('End off app')