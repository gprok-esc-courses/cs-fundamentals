from cars import Car 

a = 5
b = 7

# print(id(a))
# print(id(b))

c = Car("golf", "ZAA9098", 140, 10)
d = Car("golf", "ZAA9098", 140, 10)

print(id(c))
print(id(d))