import random

data = []

for i in range(10):
    value = random.randint(1, 100)
    data.append(value)

for i in range(len(data)):
    print(data[i])
