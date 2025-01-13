scores = {
    'a': 3,
    'b': 1,
    'c': 2,
    'd': 7,
    'e': 5,
    'f': 4,
    'g': 1
}

ordered_list = list(sorted(scores.items(), key=lambda item: item[1], reverse=True))

for i in range(3):
    print(ordered_list[i])