
students = {
    178: {'id': 178,
           'name': 'John', 
           'major': 'Computing',
           'grades': {'math': 65, 'python': 76, 'os': 55}, 
           'phone': '699393873'},
    179: {'id': 179,
           'name': 'Peter', 
           'major': 'Management',
           'grades': {'math': 45, 'excel': 30, 'adv': 85}, 
           'phone': '695412342'},
    204: {'id': 204,
           'name': 'Ann', 
           'major': 'Psychology',
           'grades': {'math': 52}, 
           'phone': '6954009876'},
}

id = int(input("Give id: "))
if id in students:
    student = students[id]
    print(student)
else: 
    print("Not found")