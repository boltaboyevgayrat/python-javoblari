numbers = [1, 3, 5, 3, 7, 1, 9, 5]

def find_duplicates(arr):
    num = []
    dup = []
    for i in arr:
        if i in num:
            dup.append(i)
        
        num.append(i)

    return set(dup)

print(find_duplicates(numbers))
# Natija: [3, 1, 5]  (yoki istalgan tartibda)