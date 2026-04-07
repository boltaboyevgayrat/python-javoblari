students = [
    {"name": "Ali", "age": 22, "gpa": 3.5},
    {"name": "Zuhra", "age": 19, "gpa": 4.0},
    {"name": "Olim", "age": 21, "gpa": 3.2},
    {"name": "Botir", "age": 20, "gpa": 3.8}
]

def bubble_sort(arr, field):
    n = len(arr)
    new_list = arr[:]
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if new_list[j][field] > new_list[j + 1][field]:
                new_list[j], new_list[j + 1] = new_list[j + 1], new_list[j]
                
    return new_list

print(bubble_sort(students, "name"))
print(bubble_sort(students, "age"))
print(bubble_sort(students, "gpa"))

sorted_by_gpa = sorted(students, key=lambda x: x['gpa'])

sorted_by_age = sorted(students, key=lambda x: x['age'], reverse=True)