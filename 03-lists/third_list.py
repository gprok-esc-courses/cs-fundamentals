
grades = [67, 45, 90, 34, 67, 48, 55, 60]

passed = True

for i in range(len(grades)):
    if grades[i] < 40:
        print("Failed")
        passed = False
        break

if passed:
    print("Passed")

total = 0
for i in range(len(grades)):
    # total = total + grades[i]
    total += grades[i]

print("Total", total)
print("Average", total / len(grades))

