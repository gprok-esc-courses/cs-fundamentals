
data = [
    [1, 2, 3, 4],
    [5, 6, 7, 8], 
    [9, 10, 11, 12]
]

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=' ')
    print()