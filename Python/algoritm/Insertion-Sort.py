# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# def printArray(arr):
#     for i in range(len(arr)):
#         print(arr[i], end = " ")
#     print()

# if __name__ == "__main__":
#     arr = [12, 11, 13, 5, 6]
#     insertionSort(arr)
#     printArray(arr)

#  --------------------------------------------------------------

# my_array = [64, 34, 25, 12, 22, 11, 90, 5]

# n = len(my_array)
# for i in range(1, n):
#     insert_index = i
#     current_value = my_array.pop(i)
#     for j in range(i-1, -1, -1):
#         if my_array[j] > current_value:
#             insert_index = j
#     my_array.insert(insert_index, current_value)

# print("Sorted array: ", my_array)

#  -------------------------------------------------------------------------------------------

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(1, n):
    insert_index = i
    current_value = my_array[i]
    for j in range(i-1, -1, -1):
        if my_array[j] > current_value:
            my_array[j+1] = my_array[j]
            insert_index = j
        else:
            break
    my_array[insert_index] = current_value

print("Sorted array:", my_array )