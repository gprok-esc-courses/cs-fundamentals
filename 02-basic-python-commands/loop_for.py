# Count from 0 to 9

start = int(input("Start number: "))
stop = int(input("Stop number: "))

if start <= stop:
    step = 1
    stop = stop + 1
else:
    step = -1
    stop = stop - 1


for i in range(start, stop, step):
    print(i)