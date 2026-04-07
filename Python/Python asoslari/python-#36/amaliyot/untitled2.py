# def bubble_sort(arr):
#     n = len(arr)
    
#     for i in range(n - 1):          # n-1 marta o'tish
#         for j in range(n - i - 1):  # har o'tishda oxirgi i ta element allaqachon joyida
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]  # almashtiramiz
    
#     return arr

# # Ishlatish
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print("Asl:", numbers)
# print("Tartiblangan:", bubble_sort(numbers))

# # Chiqish:
# # Asl: [64, 34, 25, 12, 22, 11, 90]
# # Tartiblangan: [11, 12, 22, 25, 34, 64, 90]


# def bubble_sort_optimized(arr):
#     n = len(arr)
    
#     for i in range(n - 1):
#         swapped = False  # bu o'tishda almashish bo'ldimi?
        
#         for j in range(n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
        
#         if not swapped:   # almashish bo'lmasa — massiv tayyor!
#             break
    
#     return arr

# # Ishlatish
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print("Asl:", numbers)
# print("Tartiblangan:", bubble_sort_optimized(numbers))

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     # 1. Bo'lish
#     mid = len(arr) // 2
#     left  = merge_sort(arr[:mid])   # chap yarmini tartibla
#     right = merge_sort(arr[mid:])   # o'ng yarmini tartibla
    
#     # 2. Birlashtirish
#     return merge(left, right)


# def merge(left, right):
#     result = []
#     i = j = 0
    
#     # kichigini tanlayveramiz
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
    
#     # qolganlarini qo'shamiz
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


# # Ishlatish
# numbers = [38, 27, 43, 3, 9, 82, 10]
# print("Asl:", numbers)
# print("Tartiblangan:", merge_sort(numbers))

# # Chiqish:
# # Asl: [38, 27, 43, 3, 9, 82, 10]
# # Tartiblangan: [3, 9, 10, 27, 38, 43, 82]

# import time
# import random

# # Katta massiv yasaymiz
# big_list = random.sample(range(10_000), 5000)

# # Bubble Sort vaqti
# arr1 = big_list.copy()
# t1 = time.time()
# bubble_sort(arr1)
# t2 = time.time()
# print(f"Bubble Sort: {t2 - t1:.4f} sekund")

# # Merge Sort vaqti
# arr2 = big_list.copy()
# t3 = time.time()
# merge_sort(arr2)
# t4 = time.time()
# print(f"Merge Sort:  {t4 - t3:.4f} sekund")

# # Natija (taxminan):
# # Bubble Sort: 4.2000 sekund
# # Merge Sort:  0.0300 sekund  ← ~140x tezroq!

# def bubble_sort(arr):
#     n = len(arr)
    
#     for i in range(len(arr)-1):        # 1. bu yerga nima yoziladi?
#         for j in range(len(arr)-i-1):    # 2. bu yerga nima yoziladi?
#             if arr[j] > arr[j+1]:          # 3. qaysi belgi?
#                 arr[j], arr[j+1] = arr[j+1], arr[j]  # 4. almashtiramiz

#     return arr

# # Tekshirish:
# print(bubble_sort([5, 3, 8, 1, 9, 2]))
# # Natija: [1, 2, 3, 5, 8, 9] bo'lishi kerak


def merge_sort(arr):
    if len(arr) <= 1:     
        return arr
    
    mid = len(arr) // 2     
    
    left  = merge_sort(arr[:mid])    
    right = merge_sort(arr[mid:])    
    
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            result.append(left[i])   
            i += 1
        elif left[i] == right[j]:
            result.append(left[i])  
            i += 1

        elif len(left[i]) == len(right[j]):
            
            while left[i][k] == right[j][k]:
                k += 1

            if left[i][k] < right[j][k]:
                result.append[left[i]]
                i += 1

            else:
                result.append(right[j])
                j += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# # Tekshirish:
# print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
# # Natija: [3, 9, 10, 27, 38, 43, 82] bo'lishi kerak

# def sort_evens(arr):
#     # 1. Merge Sort bilan arrni tartibla
#     # 2. Faqat juft sonlarni qaytar
#     array = merge_sort(arr)
#     return [i  for i in array  if i % 2 == 0]


# # Tekshirish:
# print(sort_evens([7, 2, 5, 8, 1, 4, 3, 6]))
# # Natija: [2, 4, 6, 8]

# print(sort_evens([9, 3, 10, 1, 4, 7, 2]))
# # Natija: [2, 4, 10]

# def custom_sort(arr):
#     # Misol uchun: [4, 1, 6, 3, 2, 7, 8, 5]
#     # Natija:      [1, 3, 5, 7, 2, 4, 6, 8]
#     #               ^toqlar^   ^juftlar^
#     array = merge_sort(arr)
#     return [i for i in array if i % 2 == 1] + [i for i in array if i % 2 == 0]


# # Tekshirish:
# print(custom_sort([4, 1, 6, 3, 2, 7, 8, 5]))
# # Natija: [1, 3, 5, 7, 2, 4, 6, 8]

# print(custom_sort([10, 3, 7, 2, 5, 8]))
# # Natija: [3, 5, 7, 2, 8, 10]

# print(custom_sort([1, 2, 3, 4, 5]))
# # Natija: [1, 3, 5, 2, 4]

def sort_strings(arr):
    return merge_sort(arr)


# Tekshirish:
print(sort_strings(["banan", "olma", "o", "gilos", "nok", "anor"]))
# Natija: ["o", "nok", "olma", "anor", "banan", "gilos"]
#          1     3      4       4       5        5
#                       ^alifbo^        ^alifbo^

print(sort_strings(["python", "c", "java", "go", "rust"]))
# Natija: ["c", "go", "rust", "java", "python"]

print(sort_strings(["z", "a", "m", "b"]))
# Natija: ["a", "b", "m", "z"]