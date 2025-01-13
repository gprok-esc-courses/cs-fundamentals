from functools import reduce 

test = lambda x, y : x + y 

print(test(4, 5))

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

increased = map(lambda v : v + 1, data)

print(list(increased))

even = filter(lambda v : v % 2 == 0, data)

print(list(even))

product = reduce(lambda x, y : x + y, data)
print(product)