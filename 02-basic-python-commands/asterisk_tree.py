
def print_line(spaces, ch, char_times):
    """
    Prints a line with spaces and some character after the spaces  
    spaces: Number of leading spaces  
    ch: Character to print after the spaces  
    char_times: How many time to print ch
    """
    for i in range(spaces):
        print(' ', end=' ')
    for i in range(char_times):
        print(ch, end=' ')
    print()

n = int(input("Give an odd number: "))
c = input("Give me the char to print: ")

if n % 2 == 0:
    print("Not odd, increased by 1")
    n += 1

spaces = n // 2
asterisks = 1 

for i in range(spaces, -1, -1):
    print_line(i, c, asterisks)
    asterisks += 2

print_line(spaces, '#', 1)
