
file = open('cities.csv')

lines = file.readlines()

states = {}

for i in range(1, len(lines)):
    line = lines[i]
    parts = line.split(' ')
    if len(parts) > 1:
        city = parts[-2].strip()
        city = city[1:-1]
        state = parts[-1].strip()
        if state in states:
            states[state].append(city)
        else:
            states[state] = [city]

s = input("State: ")
if s in states:
    print("Cities at", s, ":", states[s])
else:
    print("Invalid state")