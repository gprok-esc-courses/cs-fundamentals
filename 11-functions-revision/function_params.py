from typing import List

def sum(a: int, b: int) -> int:
    return a + b 

def sum_list(list: List) -> int:
    """
    Calculates the sum of all integer values containrd in the list.
    """
    total = 0
    for value in list:
        total += value
    return total

def sum_all(a, *args):
    print(a)
    print(args)
    return sum_list(args)

def named_params(**kwargs):
    print(kwargs)
    if kwargs['role'] == 'admin':
        print("Administrator")
    else:
        print("Regular user")

print(sum("A", "B"))
print(sum_list([2,3,4,5,6]))
print(sum_all(2, 3, 4, 5, 6, 7))
named_params(username='john', password='1111', role='admin')