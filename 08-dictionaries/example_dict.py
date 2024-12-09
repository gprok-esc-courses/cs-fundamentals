
scores = {
    'a': 2, 'b': 0, 'c': 7, 'd': 4, 'e': 2
}

v = list(scores.values())
v.sort(reverse=True)

print(v)
top = v[0:2]

print(top)
